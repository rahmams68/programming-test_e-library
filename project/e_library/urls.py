from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('book/favorites/', views.favorite_book, name='favorite-book'),
    path('book/add/', views.add_book, name='add-book'),
    path('book/edit/<id>/', views.edit_book, name='edit-book'),
    path('book/delete/<id>', views.delete_book, name='delete-book'),
    path('book/<id>/', views.book_detail, name='book-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)