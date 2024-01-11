from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f"Message from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage: {message}",
                # Use the authenticated email address here
                from_email='pralhad.ranjit@aicence.com',
                # Specify the recipient
                recipient_list=['pralhad.ranjit@aicence.com'],
                fail_silently=False,
            )

            # Redirect or display a success message
            return HttpResponse("Thank you for your message.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
