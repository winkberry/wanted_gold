

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
  "customer_name": "John Doe",<br/>
  "order_type": "BUY",<br/>
  "product": "99.9% 금",<br/>
  "quantity": 100.0,<br/>
  "amount": 5000.00,<br/>
  "shipping_address": "서울시 강남구"<br/>
}<br/>
응답 예시:<br/>
{<br/>
  "order_number": "ORD-20240912-000001",<br/>
  "customer_name": "John Doe",<br/>
  "status": "ORDER_COMPLETE",<br/>
  "order_type": "BUY",<br/>
  "product": "99.9% 금",<br/>
  "quantity": 100.0,<br/>
  "amount": 5000.00,<br/>
  "shipping_address": "서울시 강남구"<br/>
}<br/>
<br/>
### 주문 상세 조회<br/>
URL: GET /api/orders/{id}/<br/>
설명: 특정 ID를 가진 주문을 조회합니다.<br/>
응답 예시:<br/>
{<br/>
  "order_number": "ORD-20240912-000001",<br/>
  "customer_name": "John Doe",<br/>
  "status": "ORDER_COMPLETE",<br/>
  "order_type": "BUY",<br/>
  "product": "99.9% 금",<br/>
  "quantity": 100.0,<br/>
  "amount": 5000.00,<br/>
  "shipping_address": "서울시 강남구"<br/>
}<br/>
<br/>
### 주문 수정<br/>
URL: PUT /api/orders/{id}/<br/>
헤더: Content-Type: application/json<br/>
요청 JSON:<br/>
{<br/>
  "customer_name": "John Smith",<br/>
  "product": "99.99% 금",<br/>
  "quantity": 150.0,<br/>
  "amount": 7500.00,<br/>
  "shipping_address": "서울시 서초구"<br/>
}<br/>
응답 예시:<br/>
{<br/>
  "order_number": "ORD-20240912-000001",<br/>
  "customer_name": "John Smith",<br/>
  "status": "ORDER_COMPLETE",<br/>
  "order_type": "BUY",<br/>
  "product": "99.99% 금",<br/>
  "quantity": 150.0,<br/>
  "amount": 7500.00,<br/>
  "shipping_address": "서울시 서초구"<br/>
}<br/>
<br/>
### 주문 삭제<br/>
URL: DELETE /api/orders/{id}/<br/>
설명: 특정 주문을 삭제합니다.<br/>
응답: 상태 코드 204 No Content<br/>
<br/>
### 주문 상태 수정<br/>
URL: POST /api/orders/{id}/update_status/<br/>
헤더: Content-Type: application/json<br/>
요청 JSON:<br/>
{<br/>
  "status": "PAYMENT_COMPLETE"<br/>
}<br/>
응답 예시:<br/>
{<br/>
  "status": "status updated"<br/>
}<br/>
<br/>