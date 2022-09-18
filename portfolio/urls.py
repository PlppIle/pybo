from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name='portfolio'

urlpatterns = [
    path('', views.index, name="index"),
    path('guestbook/create/', views.guestbook_create, name='guestbook_create'),
#    path('guestbook/modify/', views.guestbook_modify, name='guestbook_modify'),
#    path('guestbook/delete/', views.guestbook_delete, name='guestbook_delete'),
    path('Who_is_Mori?/', views.who, name="who"),
    path('Where_is_Mori?/', views.where, name="where"),
    path('What_Mori_can_do/', views.what, name="what"),
    path('FileUpload/', views.FileUpload, name='fileupload'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)