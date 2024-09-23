
from django.shortcuts import render
from .forms import ContactForm

def sendMessage(request):
    template_name = 'contactapp/contact.html'
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            contact_form = ContactForm()
    context = {
        'contact_form': contact_form
    }
    return render(request, template_name=template_name, context=context)
