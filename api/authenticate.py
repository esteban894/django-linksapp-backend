from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()


class EmailPasswordAuthentication(BaseAuthentication):
    def authenticate(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise AuthenticationFailed('Invalid email or password')

            if user.check_password(password):
                return (user, password)

        raise AuthenticationFailed('Invalid email or password')
