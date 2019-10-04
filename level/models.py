from django.db import models
from django.contrib.auth.models import User

type_choices = (('0', 'PIN'),
                ('1', 'PASSWORD'))


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    coins = models.IntegerField(default=0)


class PackageUserRelation(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name="pur", on_delete=models.CASCADE)
    package = models.ForeignKey("LevelPackage", on_delete=models.CASCADE, related_name="pur")


class Level(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    singer = models.CharField(max_length=255, blank=True, null=True)
    song_name = models.CharField(max_length=255, blank=True, null=True)
    msg_count = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    notif_sender = models.CharField(max_length=255, blank=True, null=True)
    notif_msg = models.CharField(max_length=255, blank=True, null=True)
    default_phone_number = models.CharField(max_length=255, blank=True, null=True)
    hint_msg = models.CharField(max_length=255, blank=True, null=True)
    incoming_call_number = models.CharField(max_length=255, blank=True, null=True)
    incoming_call_name = models.CharField(max_length=255, blank=True, null=True)
    clipboard_msg = models.CharField(max_length=255, blank=True, null=True)
    second_name = models.CharField(max_length=255, blank=True, null=True)
    second_text = models.CharField(max_length=255, blank=True, null=True)

    hint_1 = models.CharField(max_length=255, blank=True, null=True)
    hint_2 = models.CharField(max_length=255, blank=True, null=True)

    hint1farsi = models.CharField(max_length=255, blank=True, null=True)
    hint2farsi = models.CharField(max_length=255, blank=True, null=True)

    type = models.CharField(max_length=1, choices=type_choices, default='0')
    image = models.ImageField(max_length=255, blank=True, null=True)
    cover = models.ImageField(max_length=255, blank=True, null=True)
    incoming_call_image = models.ImageField(max_length=255, blank=True, null=True)

    hint_count = models.IntegerField(blank=True, null=True, default=0)
    pin_count = models.IntegerField(blank=True, null=True, default=4)
    index = models.IntegerField(blank=True, null=True, default=4)

    notif = models.BooleanField(default=False)
    hint = models.BooleanField(default=False)
    passed = models.BooleanField(default=False)
    incoming_call = models.BooleanField(default=False)
    clipboard = models.BooleanField(default=False)

    second_notif = models.BooleanField(default=False)

    contact_name = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class LevelPackage(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(max_length=255)
    levels = models.ManyToManyField(Level, related_name="pack")
