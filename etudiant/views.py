from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import ListeThemesEtudiant
from django.http import JsonResponse

# Create your views here.


def etudiant(request): 
    return HttpResponse("etudiant")


def liste_themes(request):
    if request.method == 'GET':
        # Récupérer la liste des thèmes depuis la base de données
        themes = ListeThemesEtudiant.objects.all().values('id','Theme', 'Enseignant','Specialite')
        return JsonResponse({'success': True, 'themes': list(themes)})
    else:
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)