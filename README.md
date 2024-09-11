

## API 요청 설명<br/>
### 주문 목록 조회<br/>
URL: GET /api/orders/<br/>
설명: 모든 주문을 조회합니다.<br/>
응답 예시:<br/>
[<br/>
  {<br/>
    "order_number": "ORD-20240912-000001",<br/>
    "customer_name": "John Doe",<br/>
    "status": "ORDER_COMPLETE",<br/>
    "order_type": "BUY",<br/>
    "product": "99.9% 금",<br/>
    "quantity": 100.0,<br/>
    "amount": 5000.00,<br/>
    "shipping_address": "서울시 강남구"<br/>
  },<br/>
  // 추가 주문들...<br/>
]<br/>

### 주문 생성<br/>
URL: POST /api/orders/<br/>
헤더: Content-Type: application/json<br/>
요청 JSON:<br/>
{<br/>
  "customer_name": "John Doe",
  "order_type": "BUY",
  "product": "99.9% 금",
  "quantity": 100.0,
  "amount": 5000.00,
  "shipping_address": "서울시 강남구"
}
응답 예시:
{
  "order_number": "ORD-20240912-000001",
  "customer_name": "John Doe",
  "status": "ORDER_COMPLETE",
  "order_type": "BUY",
  "product": "99.9% 금",
  "quantity": 100.0,
  "amount": 5000.00,
  "shipping_address": "서울시 강남구"
}

### 주문 상세 조회
URL: GET /api/orders/{id}/
설명: 특정 ID를 가진 주문을 조회합니다.
응답 예시:
{
  "order_number": "ORD-20240912-000001",
  "customer_name": "John Doe",
  "status": "ORDER_COMPLETE",
  "order_type": "BUY",
  "product": "99.9% 금",
  "quantity": 100.0,
  "amount": 5000.00,
  "shipping_address": "서울시 강남구"
}

### 주문 수정
URL: PUT /api/orders/{id}/
헤더: Content-Type: application/json
요청 JSON:
{
  "customer_name": "John Smith",
  "product": "99.99% 금",
  "quantity": 150.0,
  "amount": 7500.00,
  "shipping_address": "서울시 서초구"
}
응답 예시:
{
  "order_number": "ORD-20240912-000001",
  "customer_name": "John Smith",
  "status": "ORDER_COMPLETE",
  "order_type": "BUY",
  "product": "99.99% 금",
  "quantity": 150.0,
  "amount": 7500.00,
  "shipping_address": "서울시 서초구"
}

### 주문 삭제
URL: DELETE /api/orders/{id}/
설명: 특정 주문을 삭제합니다.
응답: 상태 코드 204 No Content

### 주문 상태 수정
URL: POST /api/orders/{id}/update_status/
헤더: Content-Type: application/json
요청 JSON:
{
  "status": "PAYMENT_COMPLETE"
}
응답 예시:
{
  "status": "status updated"
}
