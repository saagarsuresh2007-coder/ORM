

from django.db import models
from django.contrib import admin
class swiggyDB(models.Model):
	Address=models.CharField(max_length=1000);
	Name=models.CharField(max_length=10);
	Coupon=models.CharField(max_length=100);
	Upi_id=models.CharField(max_length=100);
	Credit_card_no=models.IntegerField();
	Email=models.EmailField();
	Mobile_no=models.IntegerField(primary_key=True);
class swiggyDBAdmin(admin.ModelAdmin):
	list_display=['Address','Name','Coupon','Upi_id','Credit_card_no','Email','Mobile_no'];



