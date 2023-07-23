from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from MYpetstagram.accounts.models import PetstagramUser
from MYpetstagram.common.forms import CommentForm
from MYpetstagram.pets.forms import PetForm, PetDeleteForm
from MYpetstagram.pets.models import Pet
from MYpetstagram.photos.models import Photo


# Create your views here.
@login_required
def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user = request.user
        pet.save()
        return redirect('profile-details', pk=request.user.pk)

    context = {
        'form': form,
    }

    return render(request, template_name='pets/pet-add-page.html', context=context)


@login_required
def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()
    is_owner = PetstagramUser.objects.get(username=username)

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
        'is_owner': is_owner,
    }

    return render(request, template_name='pets/pet-details-page.html', context=context)


@login_required
def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details-pet', username, pet_slug)

    context = {
        'form': form,
    }

    return render(request, template_name='pets/pet-edit-page.html', context=context)


@login_required
def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)
    form = PetDeleteForm(initial=pet.__dict__)

    context = {
        'form': form,
    }

    return render(request, template_name='pets/pet-delete-page.html', context=context)
