from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('frapi/maires/', views.MaireList.as_view()),
    path('frapi/regions/', views.RegionList.as_view()),
    path('frapi/maires/<int:pk>/', views.MaireDetails.as_view()),
    path('frapi/regions/<int:pk>/', views.RegionDetails.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
