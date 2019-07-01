from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('level.urls'))
]

admin.site.site_header = 'Password administration'
admin.site.site_title = 'Password administration'
admin.site.index_title = 'Password administration'

