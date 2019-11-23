from iert_news.models import new

from .serializers import newSerializer

from rest_framework import viewsets

class newViewset(viewsets.ModelViewSet):
    queryset = new.objects.all()
    serializer_class = newSerializer

    
