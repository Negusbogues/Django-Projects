from django.urls import path
from . import views
app_name = 'tabs'
urlpatterns = [
    path('',views.HomeView.as_view(), name = 'home'),
    path('about/',views.about_view, name = 'about'),
]