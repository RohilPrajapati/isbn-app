from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from books.services import handle_search_isbn


# Create your views here.
class BookSearchAPIView(APIView):
    def get(self, request):
        isbn = request.query_params.get("isbn")
        is_found, data = handle_search_isbn(isbn)
        if is_found:
            return Response(
                {"status": "Success", "data": data}, status=status.HTTP_200_OK
            )
        return Response(
            {"status": "Failed", "message": "No Data Found", "data": []},
            status=status.HTTP_404_NOT_FOUND,
        )
