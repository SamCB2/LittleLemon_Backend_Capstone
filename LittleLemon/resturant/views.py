from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializer import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemViews (generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer

class SingleMenuItemView (generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer

class BookingViuewSet (viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

