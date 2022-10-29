from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import responses, Response


# Create your views here.

class HelloOrdersView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={"message":"Hello Orders"}, status=status.HTTP_200_OK)