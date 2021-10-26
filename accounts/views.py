from rest_framework.generics import views, UpdateAPIView
from rest_framework import status, permissions
from rest_framework.response import Response
from .models import User
from .serializers import UserCreateSerializer, ChangePasswordSerializer

class Users(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        brands = User.objects.all()
        serializer = UserCreateSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# Password change View
class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Неправильный пароль."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()


            return Response({'message': 'Пароль успешно обновлен!'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)