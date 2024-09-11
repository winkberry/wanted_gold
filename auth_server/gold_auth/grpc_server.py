import grpc
from concurrent import futures
import orders_pb2_grpc
import orders_pb2
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User

class AuthService(orders_pb2_grpc.AuthServiceServicer):
    def VerifyToken(self, request, context):
        try:
            token = AccessToken(request.token)
            user = User.objects.get(id=token['user_id'])
            return orders_pb2.TokenResponse(
                isValid=True,
                user_id=str(user.id),
                username=user.username,
                role="admin"
            )
        except Exception as e:
            return orders_pb2.TokenResponse(isValid=False)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    orders_pb2_grpc.add_AuthorizeServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()