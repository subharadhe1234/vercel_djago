from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request,"index.html")
@csrf_exempt  # Disable CSRF for this endpoint


def register_user(request):
    if request.method =='POST':
        data= json.loads(request.body.decode('utf-8'))
        user_address=data.get('address')
        NetId=data.get('netID')
        print({user_address,NetId})

        return JsonResponse({'result': "Radhe Radhe"})

    
    return JsonResponse({"error": "Invalid request method"}, status=405)
    