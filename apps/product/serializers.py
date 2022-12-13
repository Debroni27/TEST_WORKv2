from rest_framework import serializers

from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('path', )

    def to_representation(self, instance):
        result = super().to_representation(instance)
        f_string = result['path'].split('/')
        final_string = f_string[3] + "/" + f_string[4]
        final_string = final_string.split('.')
        result['path'] = final_string[0]
        result['formats'] = ['jpg', 'png', 'webp']
        return result


class ProductSerializer(serializers.ModelSerializer):
    image = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
