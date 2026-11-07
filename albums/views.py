
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Album


def home(request):
    return render(request, 'albums/home.html')

@login_required
def add_album(request):

    if request.method == 'POST':

        album_name = request.POST.get('album_name')
        artist = request.POST.get('artist')
        genre = request.POST.get('genre')
        year = request.POST.get('year')

        Album.objects.create(
            album_name=album_name,
            artist=artist,
            genre=genre,
            year=year
        )

        return redirect('view_albums')

    return render(request, 'albums/add.html')

@login_required
def view_albums(request):

    albums = Album.objects.all()

    return render(
        request,
        'albums/view.html',
        {'albums': albums}
    )


@login_required
def edit_album(request, id):

    album = Album.objects.get(id=id)

    if request.method == 'POST':

        album.album_name = request.POST.get('album_name')
        album.artist = request.POST.get('artist')
        album.genre = request.POST.get('genre')
        album.year = request.POST.get('year')

        album.save()

        return redirect('view_albums')

    return render(request, 'albums/edit.html', {
        'album': album
    })


@login_required
def delete_album(request, id):

    if request.method == 'POST':

        album = Album.objects.get(id=id)
        album.delete()

    return redirect('view_albums')



def signup(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    else:

        form = UserCreationForm()

    return render(request, 'albums/signup.html', {
        'form': form
    })
