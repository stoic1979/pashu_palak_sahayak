from django.contrib import admin
from api.models import UserProfile,AddAnimal


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('mobile_no', 'state', 'district', 'village','tehsil', 'otp_number')
admin.site.register(UserProfile, UserProfileAdmin)


class AddAnimalAdmin(admin.ModelAdmin):
    display = ('animal_type', 'tag_no', 'name', 'dob','stage',)
admin.site.register(AddAnimal, AddAnimalAdmin)



