from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse , HttpResponseRedirect
from authentification.models import Admin , Teacher , Student
from itertools import chain

def utilisateurs(request): 
    return HttpResponse("Liste des Utilisateurs")


def comptes(request):
    if request.method == 'GET': 
        try:
            # Décoder la chaîne JSON
            admins = Admin.objects.all()
            teachers = Teacher.objects.all()
            students = Student.objects.all()

            combined_users = list(chain(admins, teachers, students))

            context = {
                 'combined_users': combined_users,
            }

            serialized_data = []

            for users in combined_users:
                serialized_data.append({
                    'email': users.email,
                    'nom': users.nom,
                    'prenom': users.prenom,
                })
            
            return JsonResponse({'success': True, 'data': serialized_data})
        
        except json.JSONDecodeError:
            # Gérer les erreurs si les données ne peuvent pas être analysées en JSON
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)
    else:
        # Gérer les autres méthodes HTTP
        return JsonResponse({'success': False, 'error': 'Only GET requests are allowed'}, status=405)
    

def ajout_user(request):
    if request.method == 'POST':
        try:
            data = request.body.decode('utf-8')
            json_data = json.loads(data)

            grade = json_data.get('grade') 
            nom = json_data.get('nom')
            prenom = json_data.get('prenom')
            email = json_data.get('login')
            password = json_data.get('password')


            if (grade=='Admin'):

                new_admin = Admin.objects.create(
                email=email,
                nom=nom,
                prenom=prenom,
                password=password
                )
                new_admin.save()

            if (grade=='Enseignant'):

                new_enseignant = Teacher.objects.create(
                email=email,
                nom=nom,
                prenom=prenom,
                password=password
                )
                new_enseignant.save()

            if (grade=='Etudiant'):

                new_etudiant = Student.objects.create(
                email=email,
                nom=nom,
                prenom=prenom,
                password=password
                )
                new_etudiant.save()

            return JsonResponse({'success': True, 'message': 'utilisateur ajouté'})
        except json.JSONDecodeError:
            # Gérer les erreurs si les données ne peuvent pas être analysées en JSON
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)
    else:
        # Gérer les autres méthodes HTTP
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'}, status=405)
    

@csrf_exempt
def delete_user(request, user_id):
    if request.method == 'DELETE':
        try:
            user = None
            if Admin.objects.filter(id=user_id).exists():
                user = Admin.objects.get(id=user_id)
            elif Teacher.objects.filter(id=user_id).exists():
                user = Teacher.objects.get(id=user_id)
            elif Student.objects.filter(id=user_id).exists():
                user = Student.objects.get(id=user_id)

            if user:
                user.delete()
                return JsonResponse({'success': True, 'message': 'Utilisateur supprimé avec succès'}, status=200)
            else:
                return JsonResponse({'success': False, 'message': 'Utilisateur non trouvé'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    
