from django import forms
from ais.models import ais,admin_login,production_login,quality_login,hod_login,oparator_login


class admin_loginForm(forms.ModelForm):
    class Meta:
        model=admin_login
        fields="__all__"
class production_loginForm(forms.ModelForm):
    class Meta:
        model=production_login
        fields="__all__"
class quality_loginForm(forms.ModelForm):
    class Meta:
        model=quality_login
        fields="__all__"
class hod_loginForm(forms.ModelForm):
    class Meta:
        model=hod_login
        fields="__all__"
class aisForm(forms.ModelForm):
    class Meta:
        model=ais
        fields="__all__"
class operator_loginForm(forms.ModelForm):
    class Meta:
        model=oparator_login
        fields="__all__"