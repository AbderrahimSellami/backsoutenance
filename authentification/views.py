from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse , HttpResponseRedirect
from .models import Admin , Teacher , Student


# Create your views here.

def authentification(request): 
    return HttpResponse("AUTH")

def form_submission(request):
    if request.method == 'POST':
        try:
            # Décoder la chaîne JSON
            data = request.body.decode('utf-8')
            
            # Convertir la chaîne JSON en un objet Python
            json_data = json.loads(data)
            
            # Accéder aux champs
            email = json_data.get('email')
            password = json_data.get('password')
            userType = json_data.get('userType')

            # Afficher les données dans la console du serveur
            print("Email:", email)
            print("Password:", password)
            print("UserType:", userType)
            
            # Checker la base de données selon le type du user
            if (userType == "admin") : 
                print("Admin Authentification")
                try:
                    admin = Admin.objects.get(email=email, password=password)
                except Admin.DoesNotExist:
                    admin = None
        
                if admin:
                    # Analyser les données JSON envoyées avec le formulaire
                    response_data = {
                        'AuthAdmin' : 'OK'
                    }
                    # Retourner une réponse JSON avec les données reçues
                    return JsonResponse(response_data)
                else:
                    response_data = {
                        'AuthAdmin' : 'KO'
                    }
                    return JsonResponse(response_data)
                
            if (userType == "teacher") : 
                print("Teacher Authentification")
                try:
                    teacher = Teacher.objects.get(email=email, password=password)
                except Teacher.DoesNotExist:
                    teacher = None
        
                if teacher:
                    # Analyser les données JSON envoyées avec le formulaire
                    response_data = {
                        'AuthTeacher' : 'OK'
                    }
                    # Retourner une réponse JSON avec les données reçues
                    return JsonResponse(response_data)
                else:
                    response_data = {
                        'AuthTeacher' : 'KO'
                    }
                    return JsonResponse(response_data)
                
            if (userType == "student") : 
                print("Student Authentification")
                try:
                    student = Student.objects.get(email=email, password=password)
                except Student.DoesNotExist:
                    student = None
        
                if student:
                    # Analyser les données JSON envoyées avec le formulaire
                    response_data = {
                        'AuthStudent' : 'OK'
                    }
                    # Retourner une réponse JSON avec les données reçues
                    return JsonResponse(response_data)
                else:
                    response_data = {
                        'AuthStudent' : 'KO'
                    }
                    return JsonResponse(response_data)
                
        except json.JSONDecodeError:
            # Gérer les erreurs si les données ne peuvent pas être analysées en JSON
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)
    else:
        # Gérer les autres méthodes HTTP
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'}, status=405)