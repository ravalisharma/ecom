"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.views.generic import TemplateView
from carts.views import cart_home


from ecommerce_app.views import home_page,about_page,contact_page,login_page,register_page
urlpatterns = [
    path('', home_page,name='home'),
    path('about/', about_page,name='about'),
    path('contact/', contact_page,name='contact'),
    path('admin/', admin.site.urls,name='admin'),
    path('login/', login_page,name='login'),
    path('cart/', cart_home,name='cart'),
    path('bootstrap/',TemplateView.as_view(template_name='bootstrap/example.html')),
    path('register/',register_page,name='register'),
    path('products/',include("products.urls"), name='products'),
    path('search/',include("search.urls"), name='search'),
   
]




if settings.DEBUG:
    urlpatterns =urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns =urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

