from rest_framework import serializers
from .models import Visitor


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['id', 'name', 'phone', 'purpose', 'check_in_time', 'check_out_time']
        read_only_fields = ['check_in_time', 'check_out_time']

    def validate_phone(self, value):
        if Visitor.objects.filter(phone = value, check_out_time__isnull=True).exists():
            raise serializers.ValidationError ("This visitor already has an active visit")
        return value