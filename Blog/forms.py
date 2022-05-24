from django import forms
import models as mod


class UploadImageForm(forms.ModelForm):

    class Meta:
        model = mod.BlogPicture
        fields = ['entrada', 'imagen']