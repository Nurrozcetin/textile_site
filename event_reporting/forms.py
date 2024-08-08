from django import forms
from django.forms import Form, ImageField, TextInput, SelectMultiple, ClearableFileInput
from event_reporting.models import Event, Customer

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        labels = {
            "date": "Event Date",
            "user" : "User",
            "orderNo": "Order No",
            "model": "Model",
            "error": "Error",
            "supplier": "Supplier",
            "errorSource": "Error Source",
            "detectionMethod": "Detection Method",
            "action": "Action",
            "result": "Result",
            "actionForRepeat": "Action For Repeat"
        }
        widgets = {  
            "orderNo": TextInput(attrs={"class": "form-control"}),
            "user": TextInput(attrs={"class": "form-control"}),
            "customer": SelectMultiple(attrs={"class": "form-control"}),
            "model": TextInput(attrs={"class": "form-control"}),
            "error": TextInput(attrs={"class": "form-control"}),
            "supplier": TextInput(attrs={"class": "form-control"}),
            "image": ClearableFileInput(attrs={"class": "form-control"}),
            "errorSource": TextInput(attrs={"class": "form-control"}),
            "detectionMethod": TextInput(attrs={"class": "form-control"}),
            "action": TextInput(attrs={"class": "form-control"}),
            "result": TextInput(attrs={"class": "form-control"}),
            "actionForRepeat": TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(EventCreateForm, self).__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.all()

    def clean_customer(self):
        customer = self.cleaned_data.get('customer')
        if not customer:
            raise forms.ValidationError("Bu alan zorunludur.")
        return customer

class UploadForm(Form):
    image = ImageField()