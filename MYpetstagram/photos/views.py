from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from MYpetstagram.common.forms import CommentForm
from MYpetstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from MYpetstagram.photos.models import Photo


# Create your views here.
@login_required
def photo_add(request):
    form = PhotoCreateForm(request.POST, request.FILES or None)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.user = request.user
        photo.save()
        form.save()

        return redirect('home-page')

    context = {
        'form': form,
    }

    return render(request, template_name='photos/photo-add-page.html', context=context)


@login_required
def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    comment_form = CommentForm()
    photo_is_liked_by_user = likes.filter(user=request.user)

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form,
        'photo_is_liked_by_user': photo_is_liked_by_user,
    }

    return render(request, template_name='photos/photo-details-page.html', context=context)


@login_required
def photo_edit(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'GET':
        form = PhotoEditForm(instance=photo, initial=photo.__dict__)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo-details', pk)

    context = {
        'form': form,
    }
    return render(request, template_name='photos/photo-edit-page.html', context=context)


@login_required
def photo_delete(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home-page')