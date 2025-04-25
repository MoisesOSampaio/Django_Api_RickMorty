from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Personagens
from .serializers import PersonagemSerializer



@api_view(['GET', 'POST'])
def personagens_lista(request):
    if request.method == 'GET':
        personagens = Personagens.objects.all()
        serializer = PersonagemSerializer(personagens, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PersonagemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


