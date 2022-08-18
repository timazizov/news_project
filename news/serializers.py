from rest_framework import serializers

from news.models import News, Category


class NewsSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    category_id = serializers.IntegerField(write_only=True)

    def get_category(self, obj):
        return obj.category.name

    def validate_category_id(self, value):
        try:
            Category.objects.get(id=value)
        except Category.DoesNotExist:
            raise serializers.ValidationError('This category_id doesn\'t exist!')
        return value

    class Meta:
        model = News
        fields = ['id', 'title', 'body', 'category', 'category_id', 'image', 'created_at', 'updated_at']
        read_only_fields = ['category']


class CategorySerializer(serializers.ModelSerializer):
    news = NewsSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'news', ]
