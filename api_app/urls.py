from django.urls import path
from .views import ScannersViews

urlpatterns = [
    path ('listItem', ScannersViews.as_view()),
    # path ('listItem/<str:sn>', ScannersViews.as_view()),
]