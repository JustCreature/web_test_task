from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
from .models import Site
from .serializer import (SiteListSerializer,
                         SiteAddSerializer,
                         SiteDetailSerializer)

from .services.services import SiteFilter, get_status



"""
Here is the two realizations with generics and with APIView, 
you can uncomment the code below to see if it works,
I left it to show that I can do it the other way, 
just in case! :)
"""



class SiteListView(generics.ListAPIView):
    """
    Represents all sites
    """

    serializer_class = SiteListSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = SiteFilter

    # # Uncomment or comment the following code to use permissions
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        sites = Site.objects.all()
        return sites


class SiteDetailView(generics.RetrieveAPIView):
    """
    Represents details about the specific site
    """

    queryset = Site.objects.all()
    serializer_class = SiteDetailSerializer



class SiteAddView(generics.CreateAPIView):
    """
    Adds new site (and checks its status)
    """

    serializer_class = SiteAddSerializer

    def perform_create(self, serializer):
        serializer.save(status=get_status(serializer.initial_data['url']))





# class SiteListView(APIView):
#     def get(self, request):
#         sites = Site.objects.all()
#         serializer = SiteListSerializer(sites, many=True)
#         return Response(serializer.data)
#
#
#
# class SiteAddView(APIView):
#     def post(self, request):
#         site = SiteAddSerializer(data=request.data)
#         if site.is_valid():
#             site.save()
#         return Response(status=201)
#
#
# class SiteDetailView(APIView):
#     def get(self, request, pk):
#         site = Site.objects.get(name=pk)
#         serializer = SiteDetailSerializer(site)
#         return Response(serializer.data)