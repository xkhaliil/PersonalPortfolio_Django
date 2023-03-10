from django import forms



class FormConnexion(forms.Form):
  login= forms.CharField(max_length=30)
  Mot_de_passe = forms.CharField (widget=forms.PasswordInput)