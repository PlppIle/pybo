from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name='portfolio'

urlpatterns = [
    path('', views.index, name="index"),
    path('guestbook/create/', views.guestbook_create, name='guestbook_create'),
    path('Who_is_Mori?/', views.who, name="who"),
    path('Where_is_Mori?/', views.where, name="where"),
    path('What_Mori_can_do/', views.what, name="what"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)