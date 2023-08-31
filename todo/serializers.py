from rest_framework import serializers
from .models import todolist, Pessoa

class todolistSerializer(serializers.ModelSerializer):
    class Meta: 
        model = todolist 
        fields = '__all__'

class PessoaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome']
                          