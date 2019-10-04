from django.contrib import admin
from .models import *

admin.site.register(Level)
admin.site.register(LevelPackage)
admin.site.register(PackageUserRelation)
admin.site.register(UserProfile)