from rest_framework import serializers
from advice.models import Advice

# id bigint
# description var 10000
# image vars
# title vars 1000
class AdviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Advice
        fields = (
            'id',
            'description',
            'image',
            'title',
        )

