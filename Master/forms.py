from django import forms
from django.forms import ModelForm
from Master.models import *
from django.core import validators

class MobileForm(ModelForm):
    brand = forms.CharField(max_length=200, label = 'brand', widget=forms.TextInput(attrs={'class':'form-control'}))
    model = forms.CharField(max_length=200, label = 'model', widget=forms.TextInput(attrs={'class':'form-control'}))
    color = forms.CharField(max_length=200, label = 'color', widget=forms.TextInput(attrs={'class':'form-control'}))
    jan = forms.CharField(max_length=13, label = 'JAN Code', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Mobiles
        fields = [ 'brand', 'model', 'color', 'jan', 'image',]

    
    # def clean(self):
    #     # data = self.cleaned_data
    #     # if  len(data['jan']) <13:
    #     #     raise forms.ValidationError('JAN Code must be of 13 digits')

    


    def clean(self):
        jan = self.cleaned_data.get('jan')
        model = self.cleaned_data.get('model')
        color = self.cleaned_data.get('color')
        
        
        
        if len(jan) <13:
                
                raise forms.ValidationError('JAN Code must be of 13 digits')
        
        for instance in Mobiles.objects.all():
            
                
            if instance.jan == jan:
                
                raise forms.ValidationError(jan + ' JAN Code already exists')
           
        
        

        for instance in Mobiles.objects.all():
            if instance.model == model:
                if instance.color == color:
                    raise forms.ValidationError(model + ' with ' + color + ' color already exists')

    
    def __init__(self, *args, **kwargs):
        super(MobileForm, self).__init__(*args, **kwargs)

        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['image'].label = 'image'