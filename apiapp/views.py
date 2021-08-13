from .serialaizer import MemberSerialaizer
from rest_framework import viewsets, generics
from .models import Member
from rest_framework.pagination import LimitOffsetPagination


# class MemberPagination(PageNumberPagination):
#     page_size = 3


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerialaizer
    pagination_class = LimitOffsetPagination


class MemberList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerialaizer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerialaizer
