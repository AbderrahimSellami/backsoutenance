from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Planning , Plateforme

@csrf_exempt
def get_planning(request):
    if request.method == 'GET':
        planning = list(Planning.objects.values())
        return JsonResponse({'success': True, 'data': planning})
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)

@csrf_exempt
def add_theme(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            planning = Planning(
                Theme=data['Theme'],
                Date=data['Date'],
                Local=data['Local'],
                Binome=data['Binome'],
                Encadreur=data['Encadreur'],
                Jury=data['Jury']
            )
            planning.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)

@csrf_exempt
def delete_theme(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            Planning.objects.filter(id=data['id']).delete()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)

    

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
