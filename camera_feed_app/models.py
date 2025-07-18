from django.db import models

class Cluster(models.Model):
    name = models.CharField(max_length=255)  # Name of the cluster

    def __str__(self):
        return self.name

class Machine(models.Model):
    name = models.CharField(max_length=255)  # Name of the machine
    cluster = models.ForeignKey(Cluster, on_delete=models.SET_NULL, related_name='machines',null=True,blank=True)  # Association with Cluster

    def __str__(self):
        return f"{self.name} ({self.cluster.name})"

class Camera(models.Model):
    name = models.CharField(max_length=255)  # Name of the camera
    ip_address = models.CharField(max_length=15)  # IP address of the camera
    port = models.IntegerField(default=554)  # RTSP default port
    username = models.CharField(max_length=255)  # Login username for camera
    password = models.CharField(max_length=255)  # Login password for camera
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='cameras', default='')  # Association with Machine

    def __str__(self):
        return self.name

class CameraSwitchTime(models.Model):
    class Meta:
        db_table = "CameraSwitchTime"
    time = models.CharField(max_length=100,blank=True,null=True)
    