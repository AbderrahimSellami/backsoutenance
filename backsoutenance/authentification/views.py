from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse , HttpResponseRedirect

# Create your views here.

def authentification(request): 
    return HttpResponse("AUTH")


def form_submission(request):
    if request.method == 'POST':
        try:
            # Analyser les données JSON envoyées avec le formulaire
            form_data = json.loads(request.body)
            # Vous pouvez maintenant traiter les données comme vous le souhaitez
            # Par exemple, enregistrer les données dans une base de données ou effectuer d'autres opérations
            # Ici, nous retournons simplement les données en réponse
            return JsonResponse({'success': True, 'data': form_data})
        except json.JSONDecodeError:
            # Gérer les erreurs si les données ne peuvent pas être analysées en JSON
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)
    else:
        # Gérer les autres méthodes HTTP
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'}, status=405)
    