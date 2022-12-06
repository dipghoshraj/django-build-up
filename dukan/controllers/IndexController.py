from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView 
from rest_framework.response import Response 

class IndexController(APIView):

    def get(self, request, *args, **kwargs):
        return Response({'status': 'success', "students":{"name": "dip"}}, status=200)  