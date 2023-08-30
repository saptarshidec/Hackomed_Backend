from django.db import models

# Create your models here.

class Patient(models.Model):
    id=models.AutoField(primary_key=True)
    firstName=models.TextField()
    lastName=models.TextField()
    doctorName=models.TextField()
    dob=models.DateField()
    phone=models.BigIntegerField()
    sex=models.TextField()
    class Meta:
        db_table='Patient'
        unique_together = ('firstName','lastName','dob','phone')

class Predictions(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    haemoglobin=models.FloatField()
    mcv=models.FloatField()
    mch=models.FloatField()
    mchc=models.FloatField()
    rdw=models.FloatField()
    ret_count=models.FloatField()

    anaemia_prediction=models.TextField()
    mcv_prediction=models.TextField()
    mch_prediction=models.TextField()
    mchc_prediction=models.TextField()
    rdw_prediction=models.TextField()
    ret_prediction=models.TextField()
    iron_deficiency=models.BooleanField()
    class Meta:
        db_table='Predictions'
