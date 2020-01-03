from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from push.models import Device
from push.serializers import DeviceSerializer

@api_view(['GET','POST'])
def device_list(request):

    #device 조회
    if request.method == 'GET':
        queryset = Device.objects.all()
        serializer = DeviceSerializer(queryset, many=True)
        return Response(serializer.data)

    #device 추가
    if request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            try:
                device = Device.objects.get(model=request.data.get('model'))
            except Device.DoesNotExist:
                device = None

            if device is not None:
                device.fcm_token = request.data.get('fcm_token')
                device.save()
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


