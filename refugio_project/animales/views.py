from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Animal, SolicitudAdopcion
from .forms import AnimalForm

# 1. Vistas de CRUD para Animales (Clases)

class ListaAnimales(ListView): #muestra el listado de animales diponibles
                                #si el animal fue adoptado lo suprime
    model = Animal
    template_name = 'animales/animal_list.html'
    context_object_name = 'animales'
    ordering = ['-fecha_publicacion']
    
    def get_queryset(self):
        # 1 Filtra animales que están disponibles
        # Esto oculta los animales cuya solicitud fue aprobada
        queryset = Animal.objects.filter(disponible=True)
        
        # 2 Lógica de visibilidad si el usuario está logueado:
        if self.request.user.is_authenticated:
            current_user = self.request.user
            # 2 Incluir el animal aprobado solo si el usuario es el adoptante
            # Buscamos los IDs de los animales que el usuario actual tiene aprobados
            solicitudes_aprobadas_ids = SolicitudAdopcion.objects.filter(
                adoptante=current_user,
                estado='APROBADA'
            ).values_list('animal_id', flat=True)
            
            queryset_aprobado = Animal.objects.filter(pk__in=solicitudes_aprobadas_ids)
            
            # 2 Excluye animales publicados por el propio usuario para no ver sus propias publicaciones
            queryset = queryset.exclude(subido_por=current_user)
            
            # 3 Combina el queryset de disponibles con el animal aprobado para el usuario.
            # Usamos '|' para combinar.
            queryset = queryset | queryset_aprobado
            
        return queryset.distinct()


class DetalleAnimal(DetailView):#muestra info detallada de un solo animal
    
    model = Animal
    template_name = 'animales/animal_detail.html'
    context_object_name = 'animal'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        animal = self.get_object()
        
        context['puede_adoptar'] = True
        context['solicitud_aprobada'] = False

        if self.request.user.is_authenticated:
            # Si el usuario es el dueño, no puede adoptar.
            if animal.subido_por == self.request.user:
                context['puede_adoptar'] = False
            
            # Verificar si ya tiene una solicitud aprobada o pendiente para el animal
            aprobada = SolicitudAdopcion.objects.filter(
                animal=animal,
                adoptante=self.request.user,
                estado='APROBADA'
            ).exists()
            
            if aprobada:
                context['puede_adoptar'] = False
                context['solicitud_aprobada'] = True #usamos bandera para el mensaje
                
        #verificamos si el animal ya no está disponible
        if not animal.disponible and not context['solicitud_aprobada']:
             context['puede_adoptar'] = False

        return context


class PublicarAnimal(LoginRequiredMixin, CreateView):#Permite a un usuario publicar un animal para adopción
    
    model = Animal
    form_class = AnimalForm
    template_name = 'animales/animal_form.html'
    success_url = reverse_lazy('animales:lista_animales')

    def form_valid(self, form):
        form.instance.subido_por = self.request.user
        messages.success(self.request, '¡Animal publicado con éxito!')
        return super().form_valid(form)


class ModificarAnimalView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):#permite al dueño modificar su publicacion
    
    model = Animal
    form_class = AnimalForm 
    template_name = 'animales/animal_form.html' 
    success_url = reverse_lazy('animales:lista_animales') 
    context_object_name = 'animal'

    def test_func(self):
        animal = self.get_object()
        return animal.subido_por == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, "Solo el dueño de la publicación puede modificarla.")
        return redirect('animales:detalle_animal', pk=self.kwargs['pk'])


class EliminarAnimalView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):#permite al usuario eliminar su publicacion
    
    model = Animal
    template_name = 'animales/animal_confirm_delete.html' 
    success_url = reverse_lazy('animales:lista_animales')

    def test_func(self):
        animal = self.get_object()
        return animal.subido_por == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, "Solo el dueño de la publicación puede eliminarla.")
        return redirect('animales:detalle_animal', pk=self.kwargs['pk'])


# 2. Vistas de Adopción (Funciones)

def adoptar_animal_confirmacion(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'animales/animal_confirm_adopcion.html', {'animal': animal})


def enviar_solicitud_adopcion(request, pk):
    """Crea la solicitud de adopción, vinculando al adoptante y al animal."""
    if not request.user.is_authenticated:
        messages.error(request, 'Debes iniciar sesión para enviar una solicitud.')
        return redirect('login')
        
    animal = get_object_or_404(Animal, pk=pk)
    
    
    if animal.subido_por == request.user:#evita que el dueño se adopte a sí mismo
        messages.error(request, 'No puedes adoptar un animal que tú mismo publicaste.')
        return redirect('animales:detalle_animal', pk=animal.pk)
        
    #verifica si ya existe una solicitud activa
    if SolicitudAdopcion.objects.filter(animal=animal, adoptante=request.user, estado__in=['PENDIENTE', 'APROBADA']).exists():
        messages.warning(request, 'Ya tienes una solicitud pendiente o aprobada para este animal.')
        return redirect('animales:mis_solicitudes')

    #crea la nueva solicitud
    solicitud = SolicitudAdopcion.objects.create(
        animal=animal,
        adoptante=request.user,
        estado='PENDIENTE'
    )
    messages.success(request, f'¡Solicitud enviada para {animal.nombre} con éxito! El dueño será notificado.')
    return redirect('animales:mis_solicitudes')

# 3. Paneles de Gestión (Funciones protegidas por @login_required)

@login_required 
def gestionar_publicaciones(request):#para mostrar la lista de animales publicados por el usuario actual
    
    animales = Animal.objects.filter(subido_por=request.user)
    return render(request, 'animales/mis_publicaciones.html', {'animales': animales})

@login_required 
def gestionar_solicitudes(request):#Mostrar todas las solicitudes de adopción recibidas por las publicaciones del usuario
    
    #filtra animales publicados por el usuario actual
    animales_publicados = Animal.objects.filter(subido_por=request.user)
    
    #obtiene solicitudes para esos animales que estén pendientes
    # aca limpia el panel del dueño tan pronto como una solicitud es resuelta.
    solicitudes = SolicitudAdopcion.objects.filter(
        animal__in=animales_publicados,
        estado='PENDIENTE'
    ).order_by('-fecha_solicitud')
    
    return render(request, 'animales/gestionar_solicitudes.html', {'solicitudes': solicitudes})


@login_required 
def ver_mis_solicitudes(request):
    """Muestra todas las solicitudes de adopción hechas por el usuario actual."""
    solicitudes = SolicitudAdopcion.objects.filter(adoptante=request.user).order_by('estado', '-fecha_solicitud')
    return render(request, 'animales/mis_solicitudes.html', {'solicitudes': solicitudes})


@login_required 
def aceptar_solicitud(request, pk):
    """Cambia el estado de una solicitud a APROBADA y marca el animal como no disponible."""
    solicitud = get_object_or_404(SolicitudAdopcion, pk=pk)
    animal = solicitud.animal #obtenemos el animal

    #solo el dueño del animal puede aceptar la solicitud
    if animal.subido_por != request.user:
        messages.error(request, "No tienes permiso para gestionar esta solicitud.")
        return redirect('animales:gestionar_solicitudes')
        
    if solicitud.estado == 'PENDIENTE':
        # cambiar estado de la solicitud
        solicitud.estado = 'APROBADA'
        solicitud.save()
        
        #marca el animal como no disponible
        animal.disponible = False 
        animal.save()
        
        #marca otras solicitudes como rechazadas
        SolicitudAdopcion.objects.filter(animal=animal).exclude(pk=solicitud.pk).update(estado='RECHAZADA')

        messages.success(request, f'Solicitud de {solicitud.adoptante.username} para {solicitud.animal.nombre} ha sido aprobada. El animal ya no está disponible.')
    else:
        messages.warning(request, f'La solicitud ya está en estado {solicitud.estado}.')
        
    return redirect('animales:gestionar_solicitudes')