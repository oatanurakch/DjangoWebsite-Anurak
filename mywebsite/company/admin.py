from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Product)    #ทำให้ Admin มองเห็นข้อมูลใน Database
admin.site.register(ContactList)
admin.site.register(Profile)
admin.site.register(ResetPasswordToken)