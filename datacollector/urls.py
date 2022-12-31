from django.urls import path
from datacollector.views import customerFormSubmission, show_message_form_condition
from datacollector.forms import  CustomerTypeForm, CustomerInfoForm, CustomerDocumentForm
from . import views



app_name = 'datacollector'
form_list = [CustomerTypeForm, CustomerInfoForm, CustomerDocumentForm]




urlpatterns = [
    path('', customerFormSubmission.as_view(), name = 'application'),
]


#form_list, condition_dict={'1':show_message_form_condition}