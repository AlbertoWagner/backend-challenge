from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination

from .models import Product
from .serializers import ProductSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HomeView(generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return Response(
            {"Fullstack Challenge 20201026"},
            status=status.HTTP_200_OK
        )


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'code'


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination
