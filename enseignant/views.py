from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse , HttpResponseRedirect
from .models import NonDispoEnseignant , ListeBinomes


# Create your views here.



def enseignant(request): 
    return HttpResponse("enseignant")


def nondispo(request): 
    if request.method == 'GET': 
        try: 
            nondispo = NonDispoEnseignant.objects.all() 

            serialized_data = []

            for nondispo in nondispo:
                serialized_data.append(
                    {
                        'id' : nondispo.id,
                        'date' : nondispo.Date,
                        'heure' : nondispo.Heure,
                    }
                )

            return JsonResponse({'success': True, 'data': serialized_data})

        except json.JSONDecodeError:
            # Gérer les erreurs si les données ne peuvent pas être analysées en JSON
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)

    else:
        # Gérer les autres méthodes HTTP
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'}, status=405)



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
