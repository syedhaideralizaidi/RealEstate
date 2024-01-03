from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from realtors.models import Realtor
from realtors.serializers import RealtorSerializer


class RealtorListView(ListAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = RealtorSerializer
    pagination_class = None
    queryset = Realtor.objects.all()


class RealtorDetailView(RetrieveAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer


class TopSellerListView(ListAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = RealtorSerializer
    queryset = Realtor.objects.filter(top_seller=True)
    pagination_class = None
