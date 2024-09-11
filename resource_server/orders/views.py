from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Order
from .serializers import OrderSerializer
from rest_framework import status

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # PUT 요청으로 주문 상태 업데이트
    def update(self, request, pk=None):
        order = self.get_object()
        new_status = request.data.get('status')

        # 상태값이 유효한지 확인 (Order 모델의 ORDER_STATUS_CHOICES 사용)
        if new_status in dict(Order.ORDER_STATUS_CHOICES):
            order.status = new_status
            order.save()
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)


