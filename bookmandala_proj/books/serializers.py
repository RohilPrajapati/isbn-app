from rest_framework import serializers
from books.models import Book


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
