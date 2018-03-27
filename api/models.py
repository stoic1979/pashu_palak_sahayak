from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User 

from django.db.models.signals import post_save
from django.dispatch import receiver


###############################################
#                                             #
#                                             #
#             UserProfile Model               #
#                                             #
#                                             #
##############################################


class UserProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	mobile_no = models.CharField(max_length=10, null=True, blank=True)
	otp_number = models.CharField(max_length=10, null=True,blank=True )
	state = models.CharField(max_length=100, null=True,blank=True)
	district = models.CharField(max_length=100,null=True,blank=True)
	tehsil = models.CharField(max_length=100,null=True,blank=True)
	village = models.CharField(max_length=100,null=True,blank=True)

	@receiver(post_save, sender=User)
	def create_profile_for_user(sender, instance=None, created=False, **kargs):
		if created:
			UserProfile.objects.get_or_create(user=instance)


###############################################
#                                             #
#                                             #
#             AddAnimal Model                 #
#                                             #
#                                             #
##############################################


class AddAnimal(models.Model):
	name  = models.CharField(max_length=50)
	tag_no = models.IntegerField()
	animal_type = models.CharField(max_length=50)
	dob = models.DateField(auto_now=False, auto_now_add=False)
	stage = models.CharField(max_length=50)