from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse , HttpResponseRedirect
from .models import NonDispoEnseignant , ListeBinomes
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import NonDispoEnseignant
from django.views.decorators.http import require_POST
from .models import ListeThemes
from django.http import QueryDict

# Create your views here.

def enseignant(request): 
    return HttpResponse("enseignant")


def nondispo(request): 
    if request.method == 'GET': 
        try: 
            nondispo = NonDispoEnseignant.objects.all() 
            serialized_data = []

            for nd in nondispo:
                serialized_data.append({
                    'id': nd.id,
                    'date': nd.Date,
                    'heure': nd.Heure,
                })

            return JsonResponse({'success': True, 'data': serialized_data})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    elif request.method == 'POST':  # Ajout de cette partie pour supporter POST
        try:
            data = json.loads(request.body)
            new_non_dispo = NonDispoEnseignant.objects.create(
                Date=data['date'],
                Heure=data['heure']
            )
            return JsonResponse({'success': True, 'message': 'Non-disponibilité ajoutée avec succès.', 'id': new_non_dispo.id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    else:
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)


def binomes(request): 
    
    if request.method == 'GET': 

        try: 
            binomes = ListeBinomes.objects.all() 

            serialized_data = []

            for binomes in binomes:
                serialized_data.append(
                    {
                        'id' : binomes.id,
                        'binome' : binomes.Binome,
                        'theme' : binomes.Theme,
                    }
                )

            return JsonResponse({'success': True, 'data': serialized_data})

        except json.JSONDecodeError:
            # Gérer les erreurs si les données ne peuvent pas être analysées en JSON
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)

    else:
        # Gérer les autres méthodes HTTP
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'}, status=405)


from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["DELETE"])
def delete_non_dispo(request, id):
    try:
        non_dispo = NonDispoEnseignant.objects.get(pk=id)
        non_dispo.delete()
        return JsonResponse({"success": True, "message": "La non-disponibilité a été supprimée avec succès."})
    except NonDispoEnseignant.DoesNotExist:
        return JsonResponse({"success": False, "message": "La non-disponibilité n'existe pas."}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)}, status=500)


from django.views.decorators.http import require_POST
import json

@require_POST
def add_non_dispo(request):
    try:
        # Récupérer les données de la requête POST
        data = json.loads(request.body)
        # Créer une nouvelle instance de NonDispoEnseignant
        non_dispo = NonDispoEnseignant.objects.create(
            Date=data['date'],
            Heure=data['heure']
        )
        # Retourner une réponse JSON avec un message de succès
        return JsonResponse({'success': True, 'message': 'La non-disponibilité a été ajoutée avec succès.'})
    except Exception as e:
        # En cas d'erreur, retourner une réponse JSON avec un message d'erreur
        return JsonResponse({'success': False, 'error': str(e)})
    

def liste_themes(request):
    if request.method == 'GET':
        # Récupérer la liste des thèmes depuis la base de données
        themes = ListeThemes.objects.all().values('id','Theme', 'Specialite')
        return JsonResponse({'success': True, 'themes': list(themes)})
    else:
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)


from django.http import HttpResponseNotAllowed


def update_theme(request, id):
    try:
        data = request.body.decode('utf-8')
        json_data = json.loads(data)
        theme = ListeThemes.objects.get(pk=id)
        # Mettez à jour les données du thème en fonction des données reçues dans la requête
        theme.Theme = json_data.get('Theme')
        theme.Specialite = json_data.get('Specialite')
        theme.save()
        return JsonResponse({'success': True, 'message': 'Thème mis à jour avec succès'})
    except ListeThemes.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Thème non trouvé'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)


def delete_theme(request, id):
    try:
        theme = ListeThemes.objects.get(pk=id)
        theme.delete()
        return JsonResponse({'success': True, 'message': 'Thème supprimé avec succès'})
    except ListeThemes.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Thème non trouvé'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)
    

@require_POST
def proposer_theme(request):
    if request.method == 'POST':
        # Récupérer les données du thème proposé depuis la requête POST
        data = request.body.decode('utf-8')

        json_data = json.loads(data)

        Theme = json_data.get('Theme')
        Specialite = json_data.get('Specialite')
        
        # Créer une nouvelle instance de ListeThemes avec les données proposées
        new_theme = ListeThemes.objects.create(
            Theme=Theme,
            Specialite=Specialite
        )
        
        # Enregistrer le nouveau thème dans la base de données
        new_theme.save()
        
        # Répondre avec un message de succès
        return JsonResponse({'success': True, 'message': 'Thème proposé avec succès'})
    else:
        # Répondre avec une erreur si la méthode n'est pas autorisée
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)

