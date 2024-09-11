import grpc
import orders_pb2_grpc  # 생성된 gRPC 코드를 임포트
import orders_pb2

def get_order(order_id):
    with grpc.insecure_channel('localhost:50051') as channel:  # gRPC 서버와 연결
        stub = orders_pb2_grpc.OrderServiceStub(channel)
        response = stub.GetOrder(orders_pb2.OrderRequest(order_id=order_id))
        print(f"Order: {response.order_id}, Status: {response.status}")