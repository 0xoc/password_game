from django.urls import path
from .views import ListLevelsView
urlpatterns = [
    path('all-levels/', ListLevelsView.as_view()),
]
