from rest_framework import serializers
from .models import Cluster, Machine, Camera,CameraSwitchTime


class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = '__all__'


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__' 

    
class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'

class CameraSwitchTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraSwitchTime
        fields = ['id', 'time'] 