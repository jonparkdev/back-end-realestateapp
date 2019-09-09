from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np
import math

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
        zero_x = -79.546811
        zero_y = 43.615780
        x = round(np.random.uniform(zero_x, -79.212679),6)
        y = round(np.random.uniform(zero_y, 43.693207),6)

        diff_x = x - zero_x
        diff_y = y - zero_y

        lat = diff_x * math.cos(math.radians(70.5)) - diff_y * math.sin(math.radians(70.5))
        lng = diff_x * math.sin(math.radians(70.5)) + diff_y * math.cos(math.radians(70.5))
    
        trans.append({'property_id': i,
                    'property_type': property_type,
                    'price': price,
                    'location':
                    {"lat": lat + zero_y + 0.065 , "lng": lng + zero_x - .025}})
    return Response(trans)
