from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.utils import timezone

from .models import UserProfile, Guestbook
from .forms import UserGuestBookForm

def index(request):
    guestbook = Guestbook.objects.order_by('-create_date')
    context = {'guestbook': guestbook}
    return render(request, 'portfolio/main.html', context)

def guestbook_create(request):
    guestbook = Guestbook.objects.order_by('-create_date')
    if request.method == "POST":
        form = UserGuestBookForm(request.POST)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.create_date = timezone.now()
            guest.author = request.user
            guest.save()
            return redirect('portfolio:index')
    else:
        form=UserGuestBookForm()
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'guestbook': guestbook, 'form': form}
    return render(request, 'portfolio/main.html', context)


def who(request):
    return render(request, 'portfolio/profile.html')

def where(request):
    return render(request, 'portfolio/hometown.html')

def what(request):
    return render(request, 'portfolio/ability.html')