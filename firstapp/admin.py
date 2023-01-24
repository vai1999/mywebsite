from django.contrib import admin
from firstapp.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	list_display=['fname','lname','email','password','mob']
admin.site.register(Student)
