from django.shortcuts import render
from customer.models import *
from customer.serializers import *

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated

class GetCustomerView(APIView):
    
    def get(self,request):
        instance = customers.objects.all()
        serializers =GetCustomerSerializer(instance,many=True)
        return Response(serializers.data)

    def post(self,request):
        params = request.data
        print("data-",params)
        ser = GetCustomerSerializer(data=params)
        ser.is_valid(raise_exception = True)
        ser.save()
        return Response({"message":"Save Sucessfully"})

class GetAddressview(APIView):
    def get(self,request):
        instance = CustomerAddress.objects.all()
        serializers=GetCustomerAddressSerializers(instance,many=True)
        return Response(serializers.data)
        
class CustomerDetialAddressView(APIView):
    
    def get(self,request,pk):
        instance = customers.objects.filter(id=pk)
        serializers = GetCustomerAddressSerializers(instance,many=True)
        return Response(serializers.data)