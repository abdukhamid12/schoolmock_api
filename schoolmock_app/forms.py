from django import formsfrom .models import *class StudentForm(forms.ModelForm):    class Meta:        model = StudentInput        fields = ['test_id']        widgets = {            'test_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write Id'}),        }