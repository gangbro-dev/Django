from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
<<<<<<< HEAD
=======
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    
>>>>>>> 453aefd82c356c5398bc0fedd06718d41e3455c2
]
