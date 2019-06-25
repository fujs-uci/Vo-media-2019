from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import *


def mysite_home(request):
    banners = HomeBanner.objects.all()
    context = {"test{}".format(banners[0].id): banners[0],
               "test{}".format(banners[1].id): banners[1],
               "test{}".format(banners[2].id): banners[2], }
    template = 'mysite/home.html'
    return render(request, template, context)


def mysite_gallery(request):
    gallery_all = GalleryImage.objects.all()
    context = {'gallery': gallery_all, }
    template = 'mysite/gallery.html'
    return render(request, template, context)


def mysite_view_image(request, image_slug):
    un_slug = " ".join(image_slug.split("-"))
    image_view = GalleryImage.objects.get(title=un_slug)
    context = {'image_view': image_view, }
    template = 'mysite/view_image.html'
    return render(request, template, context)


def mysite_contact_me(request):
    title = 'Contact'
    form = ContactForm(request.POST or None)
    confirm_message = None
    contact_me = CustomText.objects.get(type=2)
    if form.is_valid():
        name = form.cleaned_data['name']
        text = form.cleaned_data['text']
        subject = 'Message from mysite'
        email_from = form.cleaned_data['email']
        message = 'name:\t{}\nemail:\t{}\nmessage:\t{}'.format(name, email_from, text)
        email_to = [settings.EMAIL_HOST_USER]

        send_mail(
            subject,
            message,
            email_from,
            [email_to, ],
            fail_silently=False,
        )

        title = 'Message sent.'
        confirm_message = 'Thank you for messaging us. We will reply shortly.'
        form = None

    context = {'title': title,
               'contact_me': contact_me,
               'form': form,
               'confirm_message': confirm_message, }

    template = 'mysite/contact_me.html'
    return render(request, template, context)
