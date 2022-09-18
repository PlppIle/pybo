from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator

from .models import UserProfile, Guestbook, FileUpload
from .forms import UserGuestBookForm, FileUploadForm

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
        form = UserGuestBookForm()
    context = {'guestbook': guestbook, 'form': form}
    return render(request, 'portfolio/main.html', context)

"""
def guestbook_modify(request, guestbook_id):
    guestbook = get_object_or_404(Guestbook, pk=guestbook_id)
    if request.user != guestbook.author:
        messages.error(request, '수정권한이 없습니다!')
        return redirect('portfolio:index')
    if request.method == "POST":
        form = UserGuestBookForm(request.POST, instance=guestbook)
        if form.is_valid():
            guestbook = form.save(commit=False)
            guestbook.create_date = timezone.now()
            guestbook.save()
            return redirect('portfolio:index')
    else:
        form = UserGuestBookForm(instance=guestbook)
    context = {'guestbook': guestbook, 'form': form}
    return render(request, 'portfolio/main.html', context)
"""

"""
def guestbook_delete(request):
    guestbook = Guestbook.objects.get()
    if not request.user.is_superuser:
        messages.error(request, '권한이 없습니다.')
    else:
        guestbook.delete()
        return redirect('portfolio:index')
    return redirect('portfolio:index')
"""

def who(request):
    return render(request, 'portfolio/profile.html')

def where(request):
    return render(request, 'portfolio/hometown.html')

def File_Upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST)
        if form.is_valid():
            fileupload = form.save(commit=True)
            fileupload.create_date = timezone.now()
            fileupload.author = request.user
            fileupload.save()
            return redirect('portfolio:what')
    else:
        form = FileUploadForm()
    context = {'form': form}
    return render(request, 'portfolio/fileupload.html', context)

def what(request):
    page = request.GET.get('page','1')
    file_list = FileUpload.objects.all()
    paginator = Paginator(file_list, 10)
    page_obj = paginator.get_page(page)
    context = {'file_list': page_obj}
    return render(request, 'portfolio/ability.html', context)