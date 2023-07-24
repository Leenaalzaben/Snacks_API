from django.shortcuts import render
from .models import Snack
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
from .serializers import SnackSerializer
# Create your views here.

class SnackListView(ListCreateAPIView):

    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

    

