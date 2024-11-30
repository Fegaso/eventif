from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from contact.forms import ContactForm
from contact.models import Contacts
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings


def contact_us(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return render(request, 'contact/contact_form.html', {'form': form})

    contacts = Contacts.objects.create(**form.cleaned_data)

    _send_mail(
        'contact/contact_email.txt',
        {'contacts': contacts},
        'Confirmação de contato!',
        settings.DEFAULT_FROM_EMAIL,
        contacts.email)

    return HttpResponseRedirect(r('contact:detail', contacts.pk))


def new(request):
    return render(request, 'contact/contact_form.html', {'form': ContactForm()})


def detail(request, pk):
    try:
        contacts = Contacts.objects.get(pk=pk)
    except Contacts.DoesNotExist:
        raise Http404

    return render(request,
                  'contact/contact_detail.html',
                  {'contacts': contacts})


def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])