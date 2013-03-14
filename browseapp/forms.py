from django import forms
import models

class BrowseForm(forms.Form):
    TF = forms.ModelChoiceField(queryset=models.TF.objects.all(),
                                label="TF",
                                initial=0)
    species = forms.ModelChoiceField(queryset=models.Strain.objects.all(),
                                     label="species",
                                     initial=0)
