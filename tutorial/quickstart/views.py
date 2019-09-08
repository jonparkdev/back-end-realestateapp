from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np

# Create your views here.
@api_view()
def transaction(request):
    trans=[]
    type_list = ['Condo', 'Townhouse', 'Detached']
    for i in range(200):
 #randomly chose property type
        property_type = np.random.choice(type_list)

 #Choose random number from 500,000 to 2,000,000
        price = np.random.random_integers(500000,2000000)

 #Generate random number from range of latitude and longitudes
 #Rotate vectors so they are horizontal with Toronto lakeshore
        x = round(np.random.uniform(-69.66666, -69.323423),6)

        trans.append({'product_id': i,
                    'property_type': property_type,
                    'price': price,
                    'location':
                    {"lat": x, "lng": x}})
    return Response(trans)
