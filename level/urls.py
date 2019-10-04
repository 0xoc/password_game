from django.urls import path
from .views import ListLevelsView, IsUpToDate, ListPacksView, ListUserPackage, AddUserPack

urlpatterns = [
    path('all-levels/', ListLevelsView.as_view()),
    path('all-packs/', ListPacksView.as_view()),
    path('user-packs/', ListUserPackage.as_view()),
    path('add-user-pack/', AddUserPack.as_view()),
    path('is-up-to-date/', IsUpToDate.as_view())
]
