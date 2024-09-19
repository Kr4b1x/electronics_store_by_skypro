from rest_framework import serializers

from product.models import Products


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор объектов продукта."""

    class Meta:
        model = Products
        fields = "__all__"
        read_only_fields = ["arrears"]


class ProductListSerializer(serializers.ModelSerializer):
    """Сериализатор объектов списка продуктов."""

    class Meta:
        model = Products
        fields = ("id", "name", "product_models", "create_date", "company")


class ProductDetailSerializer(serializers.ModelSerializer):
    """Сериализатор сведений объектов продуктов."""

    class Meta:
        model = Products
        fields = "__all__"


class ProductUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор объектов обновления продукта."""

    class Meta:
        model = Products
        fields = "__all__"
