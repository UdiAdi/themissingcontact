from rest_framework import serializers
from firstapp.models import BandMembers


class BandMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandMembers
        fields = ('id', 'full_name', 'nick_name')
