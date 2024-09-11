from django.db import models

class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ('BUY', '구매'),
        ('SELL', '판매'),
    ]
    
    ORDER_STATUS_CHOICES = [
        ('ORDER_COMPLETE', '주문 완료'),
        ('PAYMENT_COMPLETE', '입금 완료'),
        ('SHIPPED', '발송 완료'),
        ('RECEIVED', '수령 완료'),
    ]
    
    order_number = models.CharField(max_length=20, unique=True, blank=True)  # 주문 번호 (자동 생성)
    order_date = models.DateTimeField(auto_now_add=True)  # 주문 일자
    customer_name = models.CharField(max_length=100)  # 주문자
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='ORDER_COMPLETE')  # 주문 상태
    order_type = models.CharField(max_length=4, choices=ORDER_TYPE_CHOICES)  # 구매 or 판매
    product = models.CharField(max_length=50)  # 품목 (예: 99.9% 금)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # 수량 (그램)
    amount = models.DecimalField(max_digits=12, decimal_places=2)  # 금액
    shipping_address = models.TextField(null=True, blank=True)  # 배송지 (구매 시 필요)
    
    def __str__(self):
        return f'{self.order_number} ({self.customer_name})'

    def save(self, *args, **kwargs):
        # 주문 번호 자동 생성 로직 (주문 번호가 없을 경우에만 생성)
        if not self.order_number:
            # 객체가 처음 저장될 때 id가 없으므로 super().save()로 먼저 저장한 후 id를 사용
            super().save(*args, **kwargs)
            self.order_number = f"ORD-{self.order_date.strftime('%Y%m%d')}-{self.id:06d}"
            self.save(update_fields=['order_number'])
        else:
            super().save(*args, **kwargs)