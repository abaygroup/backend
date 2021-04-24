from rest_framework.generics import views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class AccountsView(views.APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return Response({"Say": "Hello"})