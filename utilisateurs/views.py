from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse , HttpResponseRedirect
from .models import utilisateurs

# Create your views here.

def utilisateurs(request): 
    return HttpResponse("Liste des Utilisateurs")


def comptes(request):
    if request.method == 'GET': 
        try:
            # Décoder la chaîne JSON
            utilisateurs = utilisateurs.objects.all()

            serialized_data = []

            for utilisateurs in utilisateurs:
                serialized_data.append({
                    'id': utilisateurs.id,
                    'Utilisateur': utilisateurs.Utilisateur,
                    'Login': utilisateurs.Login,
                    'MDP': utilisateurs.MDP,
                })
            
            return JsonResponse({'success': True, 'data': serialized_data})
        
        except json.JSONDecodeError:
            # Gérer les erreurs si les données ne peuvent pas être analysées en JSON
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)
    else:
        # Gérer les autres méthodes HTTP
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'}, status=405)