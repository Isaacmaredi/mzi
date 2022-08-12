from django.urls import path
from .views import HomeView, AboutView, AuthorView, MyBookView

app_name = 'mziweb'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('author/',AuthorView.as_view(), name='author'),
    path('mybook/',MyBookView.as_view(), name='mybook'),
]