from django.db import models

class Student(models.Model):
	lname=models.CharField(max_length=15)
	fname=models.CharField(max_length=15)
	email=models.EmailField(max_length=15)
	password=models.CharField(max_length=15)
	mob=models.IntegerField()




	def __str__(self):
		rec=str(self.id)+self.lname+self.fname+self.email+self.password+str(self.mob)
		return rec