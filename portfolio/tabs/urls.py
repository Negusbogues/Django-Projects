from django.urls import path
from . import views
app_name = 'tabs'
urlpatterns = [
    path('',views.HomeView.as_view(), name = 'home'),
    path('projects/',views.projects_view, name = 'projects'),
    path('contact/',views.contact_view, name = 'contact'),
    path('resume/',views.resume_view, name = 'resume'),
    path('thank_you/',views.thank_you_view, name = 'thank_you'),
]