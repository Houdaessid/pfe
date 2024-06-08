import datetime
from django import forms
from django.forms import ModelForm
from .models import Facture, Hebergement, Reshebergement,Ressalle, Salle


class ReshebergementForm(forms.ModelForm):
    hebergement = forms.ModelChoiceField(
        queryset=Hebergement.objects.all(),
        label="Hebergement",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Reshebergement
        fields = [
            'idhebergement', 'etablissement', 'Demandeur', 'Courrier', 'DateEntre', 'DateSortie',
            'Capacite', 'hebergement', 'PriseenCharge', 'Type', 'Moyen', 'Statut'
        ]
        widgets = {
            'Courrier': forms.NumberInput(attrs={'class': 'form-control'}),
            'etablissement': forms.TextInput(attrs={'class': 'form-control'}),
            'Demandeur': forms.TextInput(attrs={'class': 'form-control'}),
            'Capacite': forms.NumberInput(attrs={'class': 'form-control'}),
            'DateEntre': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'DateSortie': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'PriseenCharge': forms.TextInput(attrs={'class': 'form-control'}),
            'Moyen': forms.TextInput(attrs={'class': 'form-control'}),
            'Statut': forms.TextInput(attrs={'class': 'form-control'}),
            'Type': forms.TextInput(attrs={'class': 'form-control'}),
        }
        hebergement = forms.ModelChoiceField(queryset=Salle.objects.all(), label="hebergement")
class RessalleForm(forms.ModelForm):
    class Meta:
        model = Ressalle
        fields =['idressalle','etablissement','priseEnCharge', 'demandeur', 'dateEntrée', 'dateSortie', 'Salle', 'nombrePersonne', 'sujet', 'dejeuner', 'pauseCafe', 'courrier', 'moyen', 'statut', 'commentaire']
        widgets = {
            'dateEntrée': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
            'dateSortie': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  
            'etablissement': forms.TextInput(attrs={'class': 'form-control'}),
            'demandeur': forms.TextInput(attrs={'class': 'form-control'}),
            'nombrePersonne': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control'}),
            'dejeuner': forms.Select(choices=Ressalle.DEJEUNER_CHOICES),
            'pauseCafe': forms.Select(choices=Ressalle.PAUSE_CAFE_CHOICES),
            'courrier': forms.NumberInput(attrs={'class': 'form-control'}),
            'moyen': forms.TextInput(attrs={'class': 'form-control'}),
            'priseEnCharge': forms.TextInput(attrs={'class': 'form-control'}),
           'statut': forms.Select(choices=Ressalle.STATUT_CHOICES, attrs={'class': 'form-control'}),
            'commentaire': forms.TextInput(attrs={'class': 'form-control'}),
        }                                          
def __init__(self, *args, **kwargs):
        super(RessalleForm, self).__init__(*args, **kwargs)
        if 'dateEntrée' in self.data and 'dateSortie' in self.data:
            try:
                dateEntrée = datetime.strptime(self.data.get('dateEntrée'), '%Y-%m-%d')
                dateSortie = datetime.strptime(self.data.get('dateSortie'), '%Y-%m-%d')
                self.fields['salle'].queryset = Salle.objects.exclude(
                    dateEntrée=dateSortie,
                    ressalle__dateSortie__gt=dateEntrée
                )
            except ValueError:
                self.fields['salle'].queryset = Salle.objects.none()
        else:
            self.fields['salle'].queryset = Salle.objects.none()
salle = forms.ModelChoiceField(queryset=Salle.objects.all(), label="Salle de réunion")
class SalleForm(ModelForm):
    class Meta:
        model=Salle
        fields="__all__"  
        exclude=['idsalle']   

class HebergementForm(ModelForm):
    class Meta:
        model=Hebergement
        fields="__all__"
        exclude=['idchambre']   
class ResSalleForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['etablissement', 'demandeur', 'courrier', 'dateEntrée', 'dateSortie', 'codefacture']
        