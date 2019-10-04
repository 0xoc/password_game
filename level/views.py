from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Level
from .serializers import LevelDetailedRetrieveSerializer
from rest_framework.response import Response
import hashlib 
import json
from rest_framework import status


def get_latest_hash():
    all_levels = Level.objects.all()

    data = LevelDetailedRetrieveSerializer(all_levels, many=True).data
    data_hash = hashlib.md5(json.dumps(data).encode('utf-8'))

    return str(data_hash.hexdigest())


class ListLevelsView(GenericAPIView):
    def get_queryset(self):
        pass
    
    def get(self, request):
        all_levels = Level.objects.all().order_by('id')

        data = LevelDetailedRetrieveSerializer(all_levels, many=True).data
        data_hash = hashlib.md5(json.dumps(data).encode('utf-8'))

        response = {'hash': str(data_hash.hexdigest()), 'levels': data}

        return Response(response)


class IsUpToDate(GenericAPIView):

    def get_queryset(self):
        pass
    
    def get(self, request):
        hash = request.GET.get('hash', None)

        if not hash:
            return Response({
                'Error': 'No Hash'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'is_up_to_date': hash == get_latest_hash()})
    




