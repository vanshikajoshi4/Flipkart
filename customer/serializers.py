from customer.models import *
from rest_framework import serializers
class GetCustomerSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = customers
        fields = "_all_"
   
class GetCustomerAddressSerializers(serializers.ModelSerializer):
      
    class Meta:
        model = CustomerAddress
        fields = "_all_" 
 
class CustomerDetailsAddressSerializer(serializers.ModelSerializer):      
  customers_address = GetCustomerAddressSerializers(many=True)
     
  class Meta:
        model = CustomerAddress
    
    
        fields = ('first_name', 'last_name','mobile','address','age','country_name','city_name','dob','pincode' )