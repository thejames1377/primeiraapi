from django.shortcuts import render
from rest_framework import viewsets
from .serializers import todolistSerializer,PessoaSerializers
from .models import todolist,Pessoa


class todolistViewset(viewsets.ModelViewSet):
    queryset = todolist.objects.all()
    serializer_class = todolistSerializer

class PessoaViewset(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializers
