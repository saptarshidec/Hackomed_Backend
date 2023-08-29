from django.db import models

# Create your models here.

class Patient(models.Model):
    id=models.AutoField(primary_key=True)
    firstName=models.TextField()
    lastName=models.TextField()
    doctorName=models.TextField()
    dob=models.DateField()
    class Meta:
        db_table='Patient'
        unique_together = ('firstName','lastName','doctorName', 'dob')

class Predictions(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    mcv=models.FloatField()
    mch=models.FloatField()
    mchc=models.FloatField()
    rdw=models.FloatField()
    mcv_prediction=models.TextField()
    mch_prediction=models.TextField()
    mchc_prediction=models.TextField()
    rdw_prediction=models.TextField()
    class Meta:
        db_table='Predictions'
