from rest_framework import serializers


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [

        ]
