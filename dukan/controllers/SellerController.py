from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView 
from rest_framework.response import Response
from dukan.components.seller import SellerModel

class SellerController(APIView):

    def get(self, request, *args, **kwargs):

        name = request.query_params.get('name')
        seller = SellerModel().filter_sellers_by_name(name)
        return Response({'status': 'success', "students": seller}, status=200)  
