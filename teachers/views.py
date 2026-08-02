from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Subject
from .serializers import SubjectSerializer


@api_view(['POST','GET'])
def subjects(request):

    if request.method == "GET":
        data = Subject.objects.all()
        serializer = SubjectSerializer(data, many=True)
        return Response(serializer.data)


    if request.method == "POST":
        serializer = SubjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)