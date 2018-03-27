from django.shortcuts import render

from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets

from api.models import UserProfile,AddAnimal
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
    API endpoint that allows userprofile to be viewed or edited.
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
            resp['msg'] = 'Registeration Successful'
       
        else:
            resp['success'] = False
            resp['msg'] = 'Registration Failed'
        return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    resp = {'success': True}
    if user:
        number ==otp_number
        resp['msg'] = 'Login successful'
    else:
        resp['success'] = False
        resp['msg'] = 'Invalid userame or password'
    return HttpResponse(json.dumps(resp), content_type="application/json")


class AddAnimalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows userprofile to be viewed or edited.
    """
    queryset = AddAnimal.objects.all()
    serializer_class = AddAnimalSerializer

    def create(self,request):
        resp = {'success': True}
        name = request.POST['name']
        animal_type = request.POST['animal_type']
        tag_no = request.POST['tag_no']
        dob = request.POST['dob']
        stage = request.POST['stage']
        add_animal = AddAnimal(name=name, animal_type=animal_type,tag_no=tag_no,dob=dob, stage=stage)
        add_animal.save()

        if add_animal:
            resp['msg'] = 'Animal added successfully'
       
        else:
            resp['success'] = False
            resp['msg'] = 'Failed to create record'
        return HttpResponse(json.dumps(resp), content_type="application/json")

