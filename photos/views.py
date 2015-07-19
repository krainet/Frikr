# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC
from django.contrib.auth.decorators import login_required
from django.views.generic import View

# Create your views here.
class HomeView(View):

    def get(self, req):
        photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
        context = {
            # 'photo_list': photos[:5]
            'photo_list': photos
        }
        return render(req, 'photos/home.html', context)

class PhotoDetailView(View):
    def get(self,req,id):
        """
        Carga página de detalle de foto
        :param req: HttpRequest
        :param id: id de la foto
        :return: HttpResponse
        """
        # inner join select_related / prefetch_related
        posible_photo = Photo.objects.filter(id=id).select_related('owner')
        photo = posible_photo[0] if len(posible_photo) == 1 else None
        if photo is not None:
            # load detail
            context = {
                'photo': photo
            }
            return render(req, 'photos/detail.html', context)
        else:
            return HttpResponseNotFound('Detail not found')  # 404 not found

@login_required()
def create(req):
    """
    Muestra un form para crear una foto y la crea si la peticion es POST
    :param req: HttpRequest
    :return: HttpResponse
    """
    error_messages = []
    success_message = ''
    if req.method == 'POST':
        # Creamos owner y se lo pasamos al form con un objeto pre-establecido
        photo_with_owner = Photo()
        photo_with_owner.owner = req.user

        form = PhotoForm(req.POST, instance=photo_with_owner)
        if form.is_valid():
            new_photo = form.save()
            form = PhotoForm()
            success_message = 'Foto guardada con éxito! '
            success_message += '<a href="{0}">'.format(reverse('photos_detail', args=[new_photo.pk]))
            success_message += '(ver foto)</a>'
        else:
            error_messages.append('Formulario incompleto.')
    else:
        form = PhotoForm()

    context = {
        'form': form,
        'success_message': success_message
    }
    return render(req, 'photos/new_photo.html', context)