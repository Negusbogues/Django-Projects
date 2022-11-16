from django.urls import path
from . import views
app_name = 'first_app'
urlpatterns = [
    path('',views.HomeView.as_view(), name = 'home'),
    path('contact/',views.contact_view, name = 'contact'),
    path('reviews/',views.reviews_view, name = 'reviews'),
    path('services/',views.services_view,name = 'services'),
    path('thank_you/',views.thank_you_view,name = 'thank_you'),
    path('about/',views.about_view,name = 'about'),
    path('cart/',views.cart_view,name = 'cart'),
    path('checkout/',views.checkout_view,name = 'checkout'),

    ]