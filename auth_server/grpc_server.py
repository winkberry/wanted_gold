import grpc
from concurrent import futures
import orders_pb2_grpc  # 생성된 gRPC 코드를 임포트
import orders_pb2

class OrderServiceServicer(orders_pb2_grpc.OrderServiceServicer):
    def GetOrder(self, request, context):
        # 예시 응답
        return orders_pb2.OrderResponse(
            order_id=request.order_id,
            customer_name="John Doe",
            status="ORDER_COMPLETE",
            product="99.9% 금",
            quantity=100.0,
            amount=5000.00,
            shipping_address="서울시 강남구"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    orders_pb2_grpc.add_OrderServiceServicer_to_server(OrderServiceServicer(), server)
    server.add_insecure_port('[::]:50051')  # gRPC 포트
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()