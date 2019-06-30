from django.urls import path
from .views import ListLevelsView, IsUpToDate
urlpatterns = [
    path('all-levels/', ListLevelsView.as_view()),
    path('is-up-to-date/', IsUpToDate.as_view())
]
