import json
import datetime
from django.http import HttpResponse, JsonResponse
from django.views.generic import View

# rest framework
from rest_framework.viewsets import ModelViewSet
# from .serializers import BookInfoSerializer, HeroInfoSerializer


# class BooksAPI(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookInfoSerializer

    # def get(self, request):
        # books = Book.objects.all()
        # book_dict_li = list()
        # for book in books:
        #     books_dict = book.to_dict()
        #     book_dict_li.append(books_dict)
        # return JsonResponse({"content": book_dict_li, "status": 200})
        # pass

    # def post(self, request):
    #     json_str = request.body
    #     args_dict = json.loads(json_str)
    #
    #     title = args_dict.get("title")
    #     pub_date = args_dict.get("pub_date")
    #
    #     if not all([title, pub_date]):
    #         return JsonResponse({"content": "参数缺失", "status": 400})
    #     try:
    #         pub_date = datetime.date(*map(int, pub_date.split("-")))
    #     except:
    #         return JsonResponse({"content": "日期格式错误", "status": 400})
    #
    #     Book.objects.create(title=title, pub_date=pub_date)
    #     return JsonResponse({"content": "creating a successful"})


# class BookAPI(View):
    # def get(self, request, book_id):
    #     book = Book.objects.filter(id=book_id).first()
    #     if not book:
    #         return JsonResponse({"content": "书籍不存在", "status": 400})
    #     else:
    #         book_dict = book.to_dict()
    #         return JsonResponse(book_dict)
    #
    # def put(self, request, book_id):
    #     json_str = request.body
    #     args_dict = json.loads(json_str)
    #
    #     # 使用序列化器校验参数
    #     serializer = BookInfoSerializer(data=args_dict)
    #     result = serializer.is_valid()
    #     if not result:
    #         content = serializer.errors
    #         return JsonResponse({"content": content, "status": 400})
    #
    #     # 反序列化作用到模型的对象
    #     validated_data = serializer.validated_data
    #     book = Book.objects.filter(id=book_id).first()
    #     serializer.update(book, validated_data)
    #     return JsonResponse({"content": "修改成功", "status": 200})
    #
    # def delete(self, request, book_id):
    #     book = Book.objects.filter(id=book_id).first()
    #     if not book:
    #         return JsonResponse({"content": "书籍不存在", "status": 400})
    #     else:
    #         book.is_delete = 1
    #         book.save()
    #         return JsonResponse({"content": "删除成功", "status": 200})


# class HerosAPI(ModelViewSet):
    # queryset = Hero.objects.all()
    # serializer_class = HeroInfoSerializer
