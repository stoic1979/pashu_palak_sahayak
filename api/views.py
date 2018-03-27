from django.shortcuts import render

from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets

from api.models import UserProfile
from .serializers import UserProfileSerializer,AddAnimalSerializer

import json

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from api.utils import rand_str
import api.utils as number

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows userprofile to be viewed.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def create(self,request):
        resp = {'success': True}
        mobile_no = request.POST['mobile_no']
        state = request.POST['state']
        village = request.POST['village']
        district = request.POST['district']
        tehsil = request.POST['tehsil']
        profile = UserProfile(mobile_no=mobile_no, state=state,village=village,district=district, tehsil=tehsil)
        profile.save()

        if profile:
            otp_number =number.rand_str()
            print(otp_number)
            resp['msg'] = 'Record added successfully'
       
        else:
            resp['success'] = False
            resp['msg'] = 'Failed to create record'
        return HttpResponse(json.dumps(resp), content_type="application/json")

