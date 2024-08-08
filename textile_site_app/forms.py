from django import forms
from django.forms import Form, ImageField, TextInput, SelectMultiple, ClearableFileInput
from textile_site_app.models import Item, Category, Size

class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        labels = {
            "title": "Item Title",
            "fabric" : "Fabric",
            "description": "Description",
            "date": "Date",
            "color": "Color",
            "price": "Price",
            "stock": "Stock"
        }
        widgets = {  
            "title": TextInput(attrs={"class": "form-control"}),
            "fabric": TextInput(attrs={"class": "form-control"}),
            "category": SelectMultiple(attrs={"class": "form-control"}),
            "size": SelectMultiple(attrs={"class": "form-control"}),
            "description": TextInput(attrs={"class": "form-control"}),
            "color": TextInput(attrs={"class": "form-control"}),
            "price": TextInput(attrs={"class": "form-control"}),
            "image": ClearableFileInput(attrs={"class": "form-control"}),
            "stock": TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(ItemCreateForm, self).__init__(*args, **kwargs)
        self.fields['customer'].queryset = Category.objects.all()

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError("This field is required.")
        return category
    
    def __init__(self, *args, **kwargs):
        super(ItemCreateForm, self).__init__(*args, **kwargs)
        self.fields['size'].queryset = Size.objects.all()

    def clean_size(self):
        size = self.cleaned_data.get('size')
        if not size:
            raise forms.ValidationError("This field is required.")
        return size

class UploadForm(Form):
    image = ImageField()