from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from chatData.models import People
from chatData.serializers import PeopleSerializer

# Create your views here.
@csrf_exempt
def login(request):
    """
    Login 
    """

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PeopleSerializer(data=data)
        try:
            user = People.objects.get(username=data['username'])
        except People.DoesNotExist:
            user = None
        if user:
            if user.password == data['password']:
                userserializer = PeopleSerializer(user)
                return JsonResponse({"Status": "True"}, status=201)
            return JsonResponse({"Status": "False"}, status=400)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
