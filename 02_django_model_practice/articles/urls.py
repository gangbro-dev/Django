from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
<<<<<<< HEAD
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit', views.edit, name='edit'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:aa>/delete', views.delete, name='delete'),
=======
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete', views.delete, name='delete')
>>>>>>> 4e59eac205cc821d21b2a8a957f741db3d61c8e8
]
