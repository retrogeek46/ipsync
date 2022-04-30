from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getUser(request):
    ipData = {'ipAddress': '192.168.1.4'}
    return Response(ipData)