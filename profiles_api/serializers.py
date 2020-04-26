from rest_framework import serializers

# serializer is work like a django form
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIViews"""
    name = serializers.CharField(max_length=10)
