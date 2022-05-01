from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import User, Project, IP
from .serializers import UserSerializer, ProjectSerializer, IPSerializer

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

# @api_view(['POST'])
# def updateIP(request):
#     # ipData = {'ipAddress': '192.168.1.4'}
#     # print(request.data)
#     # print(request.data['email'])
#     # get user ID
#     user = getUserFromEmail(request.data['email'])
#     if user == -1:
#         return Response(data={'message': message}, status=400)
#     else:
#         print(user)
#     # userID = 
    
#     # serializer = IPSerializer(data=request.data)
#         message = user
#     # if serializer.is_valid():
#     #     serializer.save()
#     #     message = 'update successful'
#     # else:
#     #     message = 'update unsuccessful'
#         return Response({'message': message})

@api_view(['POST'])
def getIP(request):
    # print(request.data['email'])
    # get user ID
    # user = getUserFromEmail(request.data['email'])
    # if user == -1:
    #     return Response(data={'message': message}, status=400)
    # else:
    #     print(user)
    #     message = user
    #     return Response({'message': message})
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