from django import forms
from .models import Doctor
from django.utils import timezone

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
        'ad', 'soyad', 'email', 'telefon','eser1','eser_türü1',"eser2","eser_türü2", 'makale', 'makale_türü', 'doktora_tezi','tez_türü','yds_belge','sözlü','upload_date']
        widgets= {
            "ad": forms.TextInput(attrs={"class": "form-control"}),
            "soyad": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "telefon": forms.TextInput(attrs={"class": "form-control"}),
            "eser1":forms.ClearableFileInput(attrs={"class" : "form-control"}),
            "eser_türü1": forms.Select(attrs={"class": "form-control"}),
            "eser2": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "eser_türü2": forms.Select(attrs={"class": "form-control"}),
            "makale": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "makale_türü": forms.Select(attrs={"class": "form-control"}),
            "doktora_tezi": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "tez_türü": forms.Select(attrs={"class": "form-control"}),
            "yds_belge": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "sözlü":forms.ClearableFileInput(attrs={"class":"form-control"}),
            "uploaddate": forms.DateTimeField(initial=timezone.now, widget=forms.HiddenInput()),

     }