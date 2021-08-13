from .models import Member
from rest_framework import serializers


class MemberSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'age', 'address', 'contact']