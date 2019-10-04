from django.contrib import admin
from .models import *


class LevelPackageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price']


class PackageUserRelationAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'package_name', ]

    @staticmethod
    def username(instance):
        return instance.user_profile.user.username

    @staticmethod
    def package_name(instance):
        return instance.package.name


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'coins']


admin.site.register(Level)
admin.site.register(LevelPackage, LevelPackageAdmin)
admin.site.register(PackageUserRelation, PackageUserRelationAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
