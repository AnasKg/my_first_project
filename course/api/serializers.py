from rest_framework import serializers

from course.models import Branch


class BranchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=False)
    photo = serializers.ImageField(required=False)

    def create(self, validated_data):
        return Branch.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.photo = validated_data.get('photo', instance.photo)

        instance.save()
        return instance
