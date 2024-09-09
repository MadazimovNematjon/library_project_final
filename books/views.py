from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer


class BookListApiView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True).data
        data = {
            'status': f"Returned {len(queryset)} books",
            'data': serializer
        }
        return Response(data, status=status.HTTP_200_OK)


class BookCreateApiView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': True,
                'data': serializer.data,
                'message': 'Successfully created book'
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:

            data = {
                'status': False,
                'message': serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class BookDetailApiView(APIView):

    def get(self, request, pk, ):
        try:
            queryset = Book.objects.get(id=pk)
            serializer = BookSerializer(queryset).data

            data = {
                'status': True,
                'data': serializer,
                'message': 'Successfully retrieved book'
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data = {
                'status': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)


class BookUpdateApiView(APIView):

    def put(self, request, pk):
        queryset = Book.objects.get(id=pk)
        data = request.data
        serializer = BookSerializer(instance=queryset, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
            data = {
                'status': True,
                'message': f'Successfully updated book {book_saved.title}'
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                'status': False,
                'message': serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class BookDeleteApiView(APIView):
    def delete(self, request, pk, ):
        try:
            queryset = Book.objects.get(id=pk)
            queryset.delete()
            data = {
                'status': True,
                'message': 'Successfully deleted book'
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data = {
                'status': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#################################################################################################################


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get_object(self):
#         return self.queryset.get()


# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#      serializer_class = BookSerializer


# class BookListCreateApiView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# # function base view in drf
# @api_view(['GET'])
# def book_list_view(request, *args, **kwargs):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)
