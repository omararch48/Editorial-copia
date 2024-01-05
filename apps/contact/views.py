from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import ContactMessage
from .forms import ContactMessageForm


# Create your views here.
class ContactFormView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactMessageForm
    success_url = reverse_lazy('contact:contact')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']

        if email.strip() == '' and phone.strip() == '':
            # return HttpResponseRedirect(self.get_success_url() + '?error')
            error_context = {'error_message': 'Por favor, proporciona al menos un correo electrónico o un número de teléfono'}
            return render(self.request, self.template_name, {'form': form, **error_context})

        ContactMessage.objects.create(
            name = form.cleaned_data['name'],
            email = email,
            subject = form.cleaned_data['subject'],
            phone = phone,
            message = form.cleaned_data['message']
        )

        return HttpResponseRedirect(self.get_success_url() + '?ok')