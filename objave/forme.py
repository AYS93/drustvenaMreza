from django import forms
from .models import Objava

MAX_LENGTH_OBJAVA = 12

class ObjavaForma(forms.ModelForm):
    class Meta:
        model = Objava
        polja = ['sadrzaj']
        exclude = ()
    
    def cist_sadrzaj(self):
        sadrzaj = self.cleaned_data.get("sadrzaj")
        if (len(sadrzaj) > MAX_LENGTH_OBJAVA):
            raise forms.ValidationError("Ova objava je preduga!")
        return sadrzaj
