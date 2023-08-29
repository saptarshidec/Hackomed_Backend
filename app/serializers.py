from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=['id','firstName','lastName','doctorName','dob']

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Predictions
        fields=['patient','mcv','mch','mchc','rdw','mcv_prediction','mch_prediction','mchc_prediction','rdw_prediction']