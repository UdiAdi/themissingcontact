from firstapp.models import BandMembers
from firstapp.serializers import BandMemberSerializer
from rest_framework import generics


class MembersList(generics.ListCreateAPIView):
    queryset = BandMembers.objects.all()
    serializer_class = BandMemberSerializer

