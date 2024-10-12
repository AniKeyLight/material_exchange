from rest_framework import serializers
from .models import Material, Seller

class SellerSerializer(serializers.ModelSerializer):
    materials = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Seller
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    seller = serializers.SlugRelatedField(slug_field='name', queryset=Seller.objects.all())

    class Meta:
        model = Material
        fields = '__all__'
