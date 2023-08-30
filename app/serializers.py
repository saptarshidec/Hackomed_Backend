from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=['id','firstName','lastName','doctorName','dob','age','sex']

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Predictions
        fields=['patient','haemoglobin','mcv','mch','mchc','rdw','ret_count','anaemia_prediction','mcv_prediction','mch_prediction','mchc_prediction','rdw_prediction','ret_prediction','iron_deficiency','cause']