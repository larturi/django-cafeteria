from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid:
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Envio de correo
            email_message = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto',
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content),
                'noreply@inbox.io',
                ['lea.arturi@gmail.com'],
                reply_to=[email]
            )

            try:
                email_message.send()
                return redirect(reverse('contact') + '?ok')
            except Exception as ex:
                return redirect(reverse('contact') + '?fail')

    return render(request, 'contact/contact.html', {'form': contact_form})
