
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *
from django.utils.translation import gettext_lazy as _
from .forms import *
from django.shortcuts import render
from django.http import JsonResponse 
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.db import transaction
from django.http import HttpResponse
from .signals import log_reservation_save, log_reservation_delete

def create_reservation(request):
    with transaction.atomic():
        reservation = Reservation.objects.create(
            name=request.POST['name'],
            date=request.POST['date']
        )
        log_reservation_save(Reservation, reservation, created=True, request=request)
    return HttpResponse("Réservation créée")

def update_reservation(request, pk):
    with transaction.atomic():
        reservation = Reservation.objects.get(pk=pk)
        reservation.name = request.POST['name']
        reservation.date = request.POST['date']
        reservation.save()
        log_reservation_save(Reservation, reservation, created=False, request=request)
    return HttpResponse("Réservation mise à jour")

def delete_reservation(request, pk):
    with transaction.atomic():
        reservation = Reservation.objects.get(pk=pk)
        log_reservation_delete(Reservation, reservation, request=request)
        reservation.delete()
    return HttpResponse("Réservation supprimée")

@login_required(login_url='guesthouse/connexion/')
def salle_form_view(request):
    form = RessalleForm()  
    
    if request.method == 'POST':
        form = RessalleForm(request.POST)
        if form.is_valid():
            form.save()
            GuestHouseEvent.objects.create(
                title=form.cleaned_data['etablissement'],#cleaned chniye fonction te3ha 
                start_time=form.cleaned_data['dateEntrée'],  
                end_time=form.cleaned_data['dateSortie'] 
            )
            return redirect('RessalleForm')
        else:
       
        
        # Requête SQL brute pour obtenir les salles disponibles
            salle.objects.raw(
           'Select type from salle where type NOT IN (select salle from ressalle where '"+checkin+"' between dateEntrée and datesortie and '"+checkout+"' between dateEntrée and datesortie '
            )
        
      
          
    return render(request, 'salle.html', {'form': form})

def home(request):
    context = {'role': None}
    user = request.user
    if user and user.is_authenticated:
        role = Role.objects.filter(user=user).first()
        context = {'role': role}
    return render(request, 'home.html', context=context)
@login_required(login_url='guesthouse/connexion/')
def reservation(request):
    user = request.user

    try:
        role = Role.objects.get(user=user)
    except Role.DoesNotExist:
        role = None


    if role:
        if role.is_chefreception:
            show_all = True
            show_lists = True
            show_calendar=True
        
    return render(request, 'reservation.html', {
        'show_all': show_all,
        'show_lists': show_lists,
        'show_calendar':show_calendar,
    })

@login_required(login_url='guesthouse/connexion/')
def directeurs(request):
    user = request.user

    try:
        role = Role.objects.get(user=user)
    except Role.DoesNotExist:
        role = None


    if role:
        if role.is_directeur :
            show_calendar = True
            
    return render(request, 'directeurs.html', {
        'show_calendar': show_calendar,
      
    })


@login_required(login_url='guesthouse/connexion/')
def payement(request):
    user = request.user

    # Obtenir le rôle de l'utilisateur
    try:
        role = Role.objects.get(user=user)
    except Role.DoesNotExist:
        role = None
        

    if role:
        if role.is_financier :
            show_calendar = False
            show_lists = False
            show_flistefinancier=True
            show_listefinancier=True
    return render(request, 'payement.html', {
        'show_calendar': show_calendar,
        'show_lists': show_lists,
        'show_flistefinancier':show_flistefinancier,
        'show_listefinancier':show_listefinancier,
    })

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:

            return render(request, 'connexion.html', {'error': 'Identifiants invalides'})
    return render(request, 'connexion.html')

def deconnexion(request):
    logout(request)
    return redirect('home')

@login_required(login_url='guesthouse/connexion/')
def hebergement_form_view(request):
    form = ReshebergementForm()  
    
    if request.method == 'POST':
        form = ReshebergementForm(request.POST)
        if form.is_valid():
            form.save()
            GuestHouseEvent.objects.create(
                title=form.cleaned_data['etablissement'],
                start_time=form.cleaned_data['DateEntre'],  
                end_time=form.cleaned_data['DateSortie'] 
            )
            return redirect('ReshebergementForm')
        else:
         form = ReshebergementForm()
        if 'dateEntrée' in request.GET and 'dateSortie' in request.GET:
            dateEntrée = request.GET['dateEntrée']
            dateSortie = request.GET['dateSortie']
            # Filtrer les hebergement disponibles
            hebergement_occupees = Ressalle.objects.filter(
                Q(dateEntrée__lte=dateSortie) & Q(dateSortie__gte=dateEntrée)
            ).values_list('hebergement', flat=True)
            hebergement_disponibles = Hebergement.objects.exclude(id__in=hebergement_occupees)
            form.fields['hebergement'].queryset = hebergement_disponibles
          
    return render(request, 'hebergement.html', {'form': form})
@login_required(login_url='guesthouse/connexion/')
def listeh(request):
    listeh= Reshebergement.objects.all()
    return render(request, "listepayheb.html",{'listeh': listeh})
@login_required(login_url='guesthouse/connexion/')
def liste(request):
    liste= Ressalle.objects.all()
    return render(request, "listepaysall.html",{'liste': liste})
@login_required(login_url='guesthouse/connexion/')
def suivi(request):
    suivi= Facture.objects.all()
    return render(request, "suivipayement.html",{'suivi': suivi})
@login_required(login_url='guesthouse/connexion/')
def liste_attributs(request):
    liste_attributs = Ressalle.objects.all()
    return render(request, "liste.html",{'liste_attributs': liste_attributs})

@login_required(login_url='guesthouse/connexion/')
def liste_chambre(request):
    liste_chambre = Reshebergement.objects.all()
    return render(request, "listehebergement.html", {'liste_chambre': liste_chambre})

@login_required(login_url='guesthouse/connexion/')
def delete_reshebergement(request, idhebergement):
    obj = get_object_or_404(Reshebergement, idhebergement=idhebergement)
    
    if request.method == "POST":
        obj.delete()
        return redirect('liste_chambre')  

    return render(request, 'confirm.html', {'object': obj})

@login_required(login_url='guesthouse/connexion/')
def delete_ressalle(request, idressalle):
    obj = get_object_or_404(Ressalle, idressalle=idressalle)
    
    if request.method == "POST":
        obj.delete()
        return redirect('liste_attributs') 

    return render(request, 'confirm.html', {'object': obj})
@login_required(login_url='guesthouse/connexion/')
def modifier(request):
    obj = Ressalle.objects.get(idressalle=8)
    form = RessalleForm(request.POST or None, instance=obj)  
    message = ''  # Renommé messages à message

    if form.is_valid():
        form.save()
        form = RessalleForm()
        message = "Modification avec succès"  # Modifié le message
    
    return render(request, 'edit.html', {'form': form, 'message': message})  
@login_required(login_url='guesthouse/connexion/')
def modification(request):
    obj = Reshebergement.objects.get(idhebergement=6)
    form = ReshebergementForm(request.POST or None, instance=obj)  
    message = ''  # Renommé messages à message

    if form.is_valid():
        form.save()
        form = ReshebergementForm()
        message = "Modification avec succès"  # Modifié le message
    
    return render(request, 'editt.html', {'form': form, 'message': message}) 
@login_required(login_url='guesthouse/connexion/')
def codesalle(request):
    form = ResSalleForm()  # Initialisation de la variable form
    if request.method == 'POST':
        form = ResSalleForm(request.POST)
        if form.is_valid():
            # Récupérez les données du formulaire
            etablissement = form.cleaned_data['etablissement']
            demandeur = form.cleaned_data['demandeur']
            courrier = form.cleaned_data['courrier']
            dateEntrée = form.cleaned_data['dateEntrée']
            dateSortie = form.cleaned_data['dateSortie']
            codefacture = form.cleaned_data['codefacture']

           
            facture = Facture.objects.create(
                etablissement=etablissement,
                demandeur=demandeur,
                courrier=courrier,
                dateEntrée=dateEntrée,
                dateSortie=dateSortie,
                codefacture=codefacture
            )
            
            facture.save()
            return redirect('codesalle')
           
    else:
     
        res_salle_data = Ressalle.objects.all().first()  

        form = ResSalleForm(initial={'etablissement': res_salle_data.etablissement,
                                     'demandeur': res_salle_data.demandeur,
                                     'courrier': res_salle_data.courrier,
                                     'dateEntrée': res_salle_data.dateEntrée,
                                     'dateSortie': res_salle_data.dateSortie})

    return render(request, 'codesalle.html', {'form': form})


@login_required(login_url='guesthouse/connexion/')
def codehebergement(request):
    form = ResSalleForm()  # Initialisation de la variable form
    if request.method == 'POST':
        form = ResSalleForm(request.POST)
        if form.is_valid():
            # Récupérez les données du formulaire
            etablissement = form.cleaned_data['etablissement']
            demandeur = form.cleaned_data['demandeur']
            courrier = form.cleaned_data['courrier']
            dateEntre = form.cleaned_data['dateEntre']
            dateSortie = form.cleaned_data['dateSortie']
            codefacture = form.cleaned_data['codefacture']

           
            facture = Facture.objects.create(
                etablissement=etablissement,
                demandeur=demandeur,
                courrier=courrier,
                dateEntrée=dateEntre,
                dateSortie=dateSortie,
                codefacture=codefacture
            )
            
            facture.save()
            return redirect('codehebergement')
           
    else:
     
        res_salle_data = Reshebergement.objects.all().first()  

        form = ResSalleForm(initial={'etablissement': res_salle_data.etablissement,
                                     'Demandeur': res_salle_data.Demandeur,
                                     'Courrier': res_salle_data.Courrier,
                                     'DateEntre': res_salle_data.DateEntre,
                                     'DateSortie': res_salle_data.DateSortie})

    return render(request, 'codehebergement.html', {'form': form})


@login_required(login_url='guesthouse/connexion/')
def salle_view(request):
    form = SalleForm() 
    
    if request.method == 'POST':
       
        form = SalleForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('SalleForm')
    return render(request, 'ajoutSalle.html', {'form': form})

@login_required(login_url='guesthouse/connexion/')
def hebergement_view(request):
    form = HebergementForm()  
    
    if request.method == 'POST':
        form = HebergementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HebergementForm')
    return render(request, 'ajoutChambre.html', {'form': form})

@login_required(login_url='guesthouse/connexion/')
def calendrier(request):  
    all_events = GuestHouseEvent.objects.all()
    context = {
        "event":all_events,
    }
    return render(request,'calendrier.html',context)

@login_required(login_url='guesthouse/connexion/')
def all_events(request):                                                                                                 
    all_events = GuestHouseEvent.objects.all()
    print(f"all_events: {all_events}")
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({    
            'id': event.id,                                                                                                  
            'title': event.title,                                                                                                                                                                                    
            'start':event.start_time.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end_time.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 
@login_required(login_url='guesthouse/connexion/') 
def add_event(request):
    start_time = request.GET.get("start", None)
    end_time = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event= GuestHouseEvent(title=str(title), start_time=start_time, end_time=end_time)
    event.save()
    data = {}
    return JsonResponse(data)
@login_required(login_url='guesthouse/connexion/')
def update(request):
    start_time = request.GET.get("start", None)
    end_time= request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event= GuestHouseEvent.objects.get(id=id)
    event.start_time= start_time
    event.end_time = end_time
    event.title = title
    event.save()
    data = {}
    return JsonResponse(data)
@login_required(login_url='guesthouse/connexion/')
def remove(request):
    id = request.GET.get("id", None)
    event = GuestHouseEvent.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)


