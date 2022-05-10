from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import User, Project, IP
from .serializers import UserSerializer, ProjectSerializer, IPSerializer
from datetime import datetime


@api_view(['GET'])
def getUser(request):
    # ipData = {'ipAddress': '192.168.1.4'}
    print(request)
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request):
    # ipData = {'ipAddress': '192.168.1.4'}
    print(request)
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def updateIP(request):
    email, project = request.data['email'], request.data['project']
    userID, projectID= getUserIDFromEmail(email), getProjectIDFromName(project)
    if userID == -1 or projectID == -1:
        message = 'Invalid user or project'
        return Response(data={'error': message}, status=400)

    # create data for inserting/updating db
    data = {
        'project_id': projectID,
        'user_id': userID,
        'ipAddress': request.data['ipAddress']
    }
    ip = getIPFromEmailProject(request.data['email'], request.data['project'])
    if ip != -1:
        # if ip exists, modified on will be added
        data['modified_on'] = datetime.now()
    
    print(type(data))
    serializer = IPSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        message = 'update successful'
    else:
        message = f'update unsuccessful, ${serializer.errors}'
    return Response({'message':message})
    


@api_view(['POST'])
def getIP(request):
    ip = getIPFromEmailProject(request.data['email'], request.data['project'])
    if ip == -1:
        message = 'Could not find IP for given email and project'
        return Response(data={'error': message}, status=400)
    else:
        print(ip)
        message = ip
        return Response({'message': f'IP Address is ${message}'})


def getUserIDFromEmail(emailID):
    users = User.objects.filter(email=emailID)
    if users.exists():
        serializer = UserSerializer(users, many=True)
        return serializer.data[0]['id']
    else:
        return -1


def getProjectIDFromName(projectName):
    projects = Project.objects.filter(name=projectName)
    if projects.exists():
        serializer = ProjectSerializer(projects, many=True)
        return serializer.data[0]['id']
    else:
        return -1


def getIPFromEmailProject(email, project):
    userID, projectID = getUserIDFromEmail(email), getProjectIDFromName(project)
    if userID == -1 or projectID == -1:
        return -1
        
    ip = IP.objects.filter(user_id=userID, project_id=projectID)
    if ip.exists():
        serializer = IPSerializer(ip, many=True)
        return serializer.data[0]['ipAddress']
    else:
        return -1