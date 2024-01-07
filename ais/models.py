from django.db import models
import datetime

# Create your models here.

from ais.valid import validate


class ais(models.Model):
    product_name = models.CharField(max_length=40)
    product_part_number = models.CharField(max_length=200,unique=True)
    ais = models.FileField(upload_to='static/ais', validators=[validate])
    revision_num=models.IntegerField('revision num',default="1")
    ################ PED APPROVE ###############################
    ApprovedByped=models.BooleanField('Approved by ped', default=False)
    ApprovedBypedUser=models.CharField(max_length=100,default="PED")
   
    ApprovedBypeddate=models.CharField(max_length=100,default="ped date")
     ################ PRODUCTION APPROVE ###############################
    
    ApprovedByProduction = models.BooleanField('Approved by production', default=False)
    ApprovedByProductionUser=models.CharField(max_length=100,default="PRODUCTIO")
    ApprovedByProductiondate=models.CharField(max_length=100,default="production date")

     ################QUALITY APPROVE ###############################
    
    ApprovedByQUA = models.BooleanField("Approved by Quality", default=False)
    ApprovedByQUAUser=models.CharField(max_length=100,default="QUALITY")
    ApprovedByQUAdate=models.CharField(max_length=100,default="quality date")
    ################HOD APPROVE ###############################
    ApprovedByHod = models.BooleanField("Approved by Hod", default=False)
    ApprovedByHodUser=models.CharField(max_length=100,default="HOD")
    ApprovedByHoddate=models.CharField(max_length=100,default="hod date")
    ############### REJECT #######################

    RejectByPed=models.BooleanField('Reject by Ped', default=False)
    RejectByPedcommand=models.CharField(max_length=100,default="REJRCT BY PED")

    RejectdByProduction = models.BooleanField('Reject byProduction', default=False)
    RejectdByProductioncommand=models.CharField(max_length=100,default="REJRCT PRODUCTION")

    RejectdByQUA = models.BooleanField("Reject by Quality", default=False)
    RejectdByQUAcommand=models.CharField(max_length=100,default="REJRCT QUALITY")

    RejectdByHod = models.BooleanField("Reject by Hod", default=False)
    RejectdByHodcommand=models.CharField(max_length=100,default="REJRCT BY HOD")

    def __str__(self):
        return self.product_part_number
class pdi(models.Model):
    product_part_number = models.CharField(max_length=200,unique=True)
    pdi = models.FileField(upload_to='static/pdi', validators=[validate])

########################### Appprove Table############################
class PED_Approve(models.Model):
    product_part_number = models.ForeignKey(ais, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.product_part_number)
class production_Approve(models.Model):
    product_part_number = models.ForeignKey(ais, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.product_part_number)
class QUALITY_Approve(models.Model):
    product_part_number = models.ForeignKey(ais, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_part_number)

class Hod_Approve(models.Model):
    product_part_number = models.ForeignKey(ais, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.product_part_number)

########################### Reject Table ############################
class PED_Reject(models.Model):
    product_part_number = models.ForeignKey(ais, on_delete=models.CASCADE)
    command=models.TextField(default="")
    def __str__(self):
        return str(self.product_part_number)
class production_Reject(models.Model):
    product_part_number = models.ForeignKey(ais, on_delete=models.CASCADE)
    command=models.TextField(default="")
    def __str__(self):
        return str(self.product_part_number)
class QUALITY_Reject(models.Model):
    product_part_number = models.ForeignKey(ais, on_delete=models.CASCADE)
    command=models.TextField(default="")
    def __str__(self):
        return str(self.product_part_number)

class Hod_Reject(models.Model):
    product_part_number = models.ForeignKey(ais, on_delete=models.CASCADE)
    command=models.TextField(default="")
    def __str__(self):
        return str(self.product_part_number)


########################### login tables############################
class admin_login(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)


class production_login(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)


class quality_login(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)


class oparator_login(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)


class hod_login(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
