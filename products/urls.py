
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ProductListView,ProductDetailSlugView
from .utils import unique_slug_generator
#ProductDetailView,product_detail_view,ProductFeaturedListView,ProductFeaturedDetailView,ProductDetailSlugView

urlpatterns = [
   
   


   
    path('', ProductListView.as_view()),

    path('<slug:slug>/', ProductDetailSlugView.as_view(),name='detail'),
  
 
    
    
]
