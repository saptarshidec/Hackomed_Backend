from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.db import connection
from .models import *
from .prediction import *
from .serializers import *

# Create your views here.
class PredictionView(APIView):
    def post(self, request, *args, **kwargs):
        success=False
        error_message=""
        firstName=request.data.get('firstName')
        lastName=request.data.get('lastName')
        dob=request.data.get('dob')
        doctorName=request.data.get('doctorName')
        mcv=request.data.get('mcv')
        mch=request.data.get('mch')
        mchc=request.data.get('mchc')
        rdw=request.data.get('rdw')
        
        mcv_prediction,mch_prediction,mchc_prediction,rdw_prediction=calc(mcv,mch,mchc,rdw)

        find_patient=Patient.objects.filter(firstName=firstName,lastName=lastName,dob=dob)

        if not find_patient.exists():
            patient={
                'firstName':firstName,
                'lastName':lastName,
                'doctorName':doctorName,
                'dob':dob
            }
            patientserializer=PatientSerializer(data=patient)
            if patientserializer.is_valid():
                saved_patient=patientserializer.save()
                id=saved_patient.id
            else:
                success=False
                error_message="Unable to create patient record"
                response={
                    'success':success,
                    'errorMessage':error_message
                }
                return Response(response, status=status.HTTP_200_OK)
        else:
            id=find_patient.first().id

        data={
            'patient':id,
            'mcv':mcv,
            'mch':mch,
            'mchc':mchc,
            'rdw':rdw,
            'mcv_prediction':mcv_prediction,
            'mch_prediction':mch_prediction,
            'mchc_prediction':mchc_prediction,
            'rdw_prediction':rdw_prediction
        }

        serializer=PredictionSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            success=True
            response={
                'success':success,
                'errorMessage':error_message,
                'mcv_prediction':mcv_prediction,
                'mch_prediction':mch_prediction,
                'mchc_prediction':mchc_prediction,
                'rdw_prediction':rdw_prediction
            }
            return Response(response,status=status.HTTP_200_OK)
        else:
            success=False
            error_message="Incorrect values provided"
            response={
                'success':success,
                'errorMessage':error_message
            }
            return Response(response, status=status.HTTP_200_OK)