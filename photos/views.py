# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.db.models import Q


class PhotosQuerySet(object):

    def get_photos_queryset(self, req):
        if not req.user.is_authenticated():
            photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
        elif req.user.is_superuser: # es super admin
            photos = Photo.objects.all()
        else:
            photos = Photo.objects.filter(Q(owner=req.user) | Q(visibility=PUBLIC))

        return photos

# Create your views here.
class HomeView(View):

    def get(self, req):
        photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
        context = {
            # 'photo_list': photos[:5]
            'photo_list': photos
        }
        return render(req, 'photos/home.html', context)

class PhotoDetailView(View, PhotosQuerySet):
    def get(self, req, id):
        """
        Carga página de detalle de foto
        :param req: HttpRequest
        :param id: id de la foto
        :return: HttpResponse
        """
        # inner join select_related / prefetch_related
        posible_photos = self.get_photos_queryset(req).filter(id=id).select_related('owner')
        photo = posible_photos[0] if len(posible_photos) == 1 else None
        if photo is not None:
            # load detail
            context = {
                'photo': photo
            }
            return render(req, 'photos/detail.html', context)
        else:
            return HttpResponseNotFound('Detail not found')  # 404 not found

class PhotoCreateView(View):
    @method_decorator(login_required())
    def get(self, req):
        """
        Muestra un form para crear una foto y la crea si la peticion es POST
        :param req: HttpRequest
        :return: HttpResponse
        """
        error_messages = []
        form = PhotoForm()

        context = {
            'form': form
        }
        return render(req, 'photos/new_photo.html', context)

    @method_decorator(login_required())
    def post(self, req):
        """
        Muestra un form para crear una foto y la crea si la peticion es POST
        :param req: HttpRequest
        :return: HttpResponse
        """
        error_messages = []
        success_message = ''

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

        context = {
            'form': form,
            'success_message': success_message
        }
        return render(req, 'photos/new_photo.html', context)

class PhotoListView(View, PhotosQuerySet):
    def get(self, req):
        """
        Dev fotos publicas a guest
        Dev fotos usuario auth
        Dev fotos usuario pub y pub de otro
        Superadmin = todo
        :param req:
        :return:
        """

        context = {
            'photos': self.get_photos_queryset(req)
        }

        return render(req, 'photos/photos_list.html', context)


class UserPhotosView(ListView):
    """
    Usando ListView para ahorrar curro  
    """
    model = Photo
    template_name = 'photos/user_photos.html'

    def get_queryset(self):
        queryset = super(UserPhotosView, self).get_queryset()
        return queryset.filter(owner=self.request.user)