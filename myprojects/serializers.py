from django.contrib.auth.models import User
from rest_framework import serializers
from myprojects.models import Program


class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Program
        fields = ('title', 'id', 'description', 'created', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    programs = serializers.HyperlinkedRelatedField(
        many=True, view_name='program-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'programs')
