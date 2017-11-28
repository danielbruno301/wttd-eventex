from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})

    # Send email
    _send_email('Confirmação de inscrição',
                settings.DEFAULT_FROM_EMAIL,
                form.cleaned_data['email'],
                'subscriptions/subscription_email.txt',
                form.cleaned_data)

    # Success feedback
    messages.success(request, 'Inscrição realizada com sucesso!')
    return HttpResponseRedirect('/inscricao/')


def _send_email(subject, from_, to, template_name, content):
    body = render_to_string(template_name, content)
    mail.send_mail(subject, body, from_, [from_, to])






