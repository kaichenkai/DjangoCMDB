from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# from .models import Book, Hero


# class BookInfoSerializer(serializers.ModelSerializer):
#     """图书数据序列化器"""
#     class Meta:
#         model = Book  # 指明该序列化器处理的数据字段从模型类 Book 参考生成
#         fields = "__all__"  # 表示包含所有字段
#
#     def create(self, validated_data):
#         book = Book.objects.create(**validated_data)
#         return book
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.pub_date = validated_data.get("pub_date", instance.pub_date)
#         instance.read_count = validated_data.get("read_count", instance.read_count)
#         instance.comment_count = validated_data.get("comment_count", instance.comment_count)
#         instance.save()
#         return instance
#
#
# class HeroInfoSerializer(serializers.ModelSerializer):
#     """英雄数据序列化器"""
#     class Meta:
#         model = Hero
#         fields = "a"
#         # required	表明该字段在反序列化时必须输入，默认True
#         id = serializers.IntegerField(label='ID', read_only=True)
#         create_time = serializers.DateTimeField(read_only=True)
#         update_time = serializers.DateTimeField(read_only=True)
#         name = serializers.CharField(label='名称', max_length=20, validators=[UniqueValidator(queryset=Hero.objects.all())])
#         gender = serializers.ChoiceField(choices=((0, 'male'), (1, 'female')), label='性别', required=False)
#         describe = serializers.CharField(label='描述内容', max_length=200, required=False)
#         is_delete = serializers.BooleanField(label='是否逻辑删除', required=False)
#         book_id = serializers.PrimaryKeyRelatedField(label='图书', queryset=Book.objects.all())
#
#     def create(self, validated_data):
#         hero = Hero.objects.create(**validated_data)
#         return hero
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.gender = validated_data.get("gender", instance.gender)
#         instance.describe = validated_data.get("describe", instance.describe)
#         instance.save()
#         return instance
