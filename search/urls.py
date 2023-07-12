
from django.urls import path
# from django.conf import settings

from search.views import SearchProductView

urlpatterns = [
    path('', SearchProductView.as_view(),name='query')
]
