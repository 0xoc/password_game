from rest_framework import serializers
from .models import Level, LevelPackage, PackageUserRelation


class LevelDetailedRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = [
            'id', 'name', 'time',
            'date', 'singer', 'song_name',
            'msg_count', 'code', 'notif_sender',
            'notif_msg', 'default_phone_number',
            'hint_msg', 'incoming_call_number',
            'incoming_call_name', 'clipboard_msg',
            'second_name', 'second_text', 'hint_1',
            'hint_2', 'type', 'image', 'cover',
            'incoming_call_image', 'hint_count',
            'pin_count', 'index', 'notif',
            'hint', 'passed', 'incoming_call', 'clipboard',
            'second_notif', 'contact_name', 'contact_number',
        ]


class LevelSimpleRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = [
            'id', 'name', 'image', 'cover',
        ]


class PackageSimpleRetrieveSerializer(serializers.ModelSerializer):
    levels = LevelSimpleRetrieveSerializer(many=True)

    class Meta:
        model = LevelPackage
        fields = ['pk', 'name', 'price', 'image', 'levels']


class PackageDetailedRetrieveSerializer(serializers.ModelSerializer):
    levels = LevelDetailedRetrieveSerializer(many=True)

    class Meta:
        model = LevelPackage
        fields = ['pk', 'name', 'price', 'image', 'levels']


class UserPackageDetailSerializer(serializers.ModelSerializer):

    package = PackageDetailedRetrieveSerializer()

    class Meta:
        model = PackageUserRelation
        fields = ['pk', 'user_profile', 'package', ]


class UserPackageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PackageUserRelation
        fields = ['package', ]

    def create(self, validated_data):
        pur = PackageUserRelation(user_profile=self.context.get('user_profile'), package=validated_data.get('package'))
        pur.save()

        return pur

