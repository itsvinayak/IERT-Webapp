from rest_framework import serializers

from iert_news.models import new


class newSerializer(serializers.ModelSerializer):

    class Meta:
        model = new
        feild= '__all__'
