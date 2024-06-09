from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse , HttpResponseRedirect
from .models import Planning , Plateforme

# Create your views here.

def planning(request): 
    return HttpResponse("planning")


def get_planning(request):
    if request.method == 'GET': 
        try:
            # Décoder la chaîne JSON
            planning_objects = Planning.objects.all()

            serialized_data = []

            for planning in planning_objects:
                serialized_data.append({
                    'id': planning.id,
                    'theme': planning.Theme,
                    'date': planning.Date,
                    'local': planning.Local,
                    'binome': planning.Binome,
                    'encadreur': planning.Encadreur,
                    'jury': planning.Jury,
                })
            
            return JsonResponse({'success': True, 'data': serialized_data})
        
        except json.JSONDecodeError:
            # Gérer les erreurs si les données ne peuvent pas être analysées en JSON
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)
    else:
        # Gérer les autres méthodes HTTP
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'}, status=405)
    

import json

def plateforme(request):
    if request.method == 'POST':
        try:
            data = request.body.decode('utf-8')
            json_data = json.loads(data)

            Date_debut = json_data.get('Date_debut') 
            Date_fin = json_data.get('Date_fin')
            heure_debut = json_data.get('heure_debut')
            heure_fin = json_data.get('heure_fin')
            duree = json_data.get('duree')
            salle = json_data.get('salle')

            plateforme = Plateforme.objects.create(
                Date_debut = Date_debut,
                Date_fin = Date_fin,
                heure_debut = heure_debut,
                heure_fin = heure_fin,
                duree = duree,
                salle = salle
            )

            return JsonResponse({'success': True, 'message': 'plateforme lancé'})
        except json.JSONDecodeError:
            # Gérer les erreurs si les données ne peuvent pas être analysées en JSON
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)
    else:
        # Gérer les autres méthodes HTTP
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'}, status=405)
