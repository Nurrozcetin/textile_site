from rest_framework import serializers

from textile_site_app.models import Category, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Item
        fields = ['id', 'title', 'fabric', 'description', 'category', 'date', 'image']

    def create(self, validated_data):
        categories_data = validated_data.pop('category')

        item = Item.objects.create(**validated_data)

        for category_data in categories_data:
            cat, created = Category.objects.get_or_create(**category_data)
            item.category.add(cat)

        return item

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)

        if 'title' in validated_data:
            instance.title = validated_data['title']
        if 'fabric' in validated_data:
            instance.desc = validated_data['fabric']
        if 'description' in validated_data:
            instance.desc = validated_data['description']
        if 'date' in validated_data:
            instance.desc = validated_data['date']
        if 'image' in validated_data:
            instance.desc = validated_data['image']

        if category_data:
            instance.category.clear()
            for cat_data in category_data:
                cat, created = Category.objects.get_or_create(**cat_data)
                instance.category.add(cat)

        instance.save()
        return instance