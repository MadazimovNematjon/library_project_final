from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        title = data['title']
        author = data['author']

        # son mavjudmi yoki harif ligini tekshiradi isalpha() funksyasi hariflarni tekshiradi
        if not title.isalpha():
            data = {
                'title': "The title must consist of letters!"
            }
            raise serializers.ValidationError(data)

        # db da mavjud bo'sa qo'shmaydi
        if Book.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError({'author': "The author already exists!"})

        return data

    def validated_price(self, price):
        if price < 0 or price > 999999999999999999:
            raise serializers.ValidationError({'price': "The price must be between 0 and 999999999999999999"})
