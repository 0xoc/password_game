from rest_framework import serializers
from .models import Level, LevelPackage


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
