from django.urls import path
from assets import views

urlpatterns = [
    path('assets/', views.AssetList.as_view()),
    path('assets/<int:pk>/', views.AssetDetail.as_view()),
]
