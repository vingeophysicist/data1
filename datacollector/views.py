from django.shortcuts import render
from formtools.wizard.views import CookieWizardView, SessionWizardView
from datacollector.forms import  CustomerTypeForm, CustomerInfoForm, CustomerDocumentForm
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings




def show_message_form_condition(wizard):
    return cleaned_data.get('CustomerTypeform', True)


class customerFormSubmission(CookieWizardView):
    template_name = 'dataform/forms.html'
    form_list = [CustomerTypeForm, CustomerInfoForm, CustomerDocumentForm]
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'photos'))
    
    
    def done(self, form_list, **kwargs):
        return render(self.request, 'dataform/home.html', {'form_data': [form.cleaned_data for form in form_list],})
