from django.db import models
from django.utils import timezone


class CustomPage(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(verbose_name="Page",
                            max_length=50,
                            unique=True)

    def __str__(self):
        return self.text


class CustomText(models.Model):
    type = models.OneToOneField(CustomPage,
                                on_delete=models.CASCADE, )
    text = models.TextField(verbose_name="Description")


def gallery_image_path(file, filename):
    date = timezone.datetime.now()
    file_path = 'gallery\\{year}\\{month}\\{name}'.format(
        year=date.year,
        month=date.month,
        name=filename, )
    return file_path


class GalleryImage(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.ImageField(upload_to=gallery_image_path)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(default=None,
                                   null=True)

    def __str__(self):
        return self.title

    @property
    def slug_me(self):
        return "-".join(self.title.split())


class GalleryVideo(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=400)


def home_banner_path(file, filename):
    date = timezone.datetime.now()
    file_path = 'home_banner\\{year}\\{month}\\{name}'.format(
        year=date.year,
        month=date.month,
        name=filename, )
    return file_path


class HomeBanner(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.ImageField(upload_to=home_banner_path)
    alt = models.CharField(max_length=100)

    def __str__(self):
        return self.alt