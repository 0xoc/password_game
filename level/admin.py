from django.contrib import admin
from .models import *


class LevelPackageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price']


class PackageUserRelationAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'package__name', 'package__price']


admin.site.register(Level)
admin.site.register(LevelPackage,  LevelPackageAdmin)
admin.site.register(PackageUserRelation, PackageUserRelationAdmin)
admin.site.register(UserProfile)