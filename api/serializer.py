from rest_framework import serializers

from .models import Site

class SiteListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        fields = '__all__'


class SiteAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        exclude = ('status', )


class SiteDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        fields = '__all__'