# 금방주식회사 백엔드 입사과제<br/>
<br/>
## Quick Start<br/>
<br/>
### 환경 설정<br/>
<br/>
1. 프로젝트 클론<br/>
<br/>
2. 가상 환경 생성 및 활성화<br/>
<br/>
# 가상 환경 생성 (윈도우)<br/>
python -m venv venv<br/>
<br/>
# 가상 환경 활성화 (윈도우)<br/>
venv\Scripts\activate<br/>
<br/>
4. .env 파일 설정<br/>
<br/>
프로젝트 루트 디렉토리에 .env 파일을 생성합니다.<br/>
<br/>
5. 데이터베이스 설정<br/>
HeidiSQL로 MariaDB에 접속하여 auth_db 및 resource_db를 생성합니다.<br/>
<br/>
6. Django 데이터베이스 마이그레이션<br/>
<br/>
python manage.py makemigrations<br/>
python manage.py migrate<br/>
<br/>
7. 서버 실행<br/>
3.1 Django 서버 실행 (auth_server 및 resource_server)<br/>
<br/>
- 터미널에서 포트 지정<br/>
**auth_server**에서 8888번 포트로 실행:<br/>
python manage.py runserver 8888<br/>
**resource_server**에서 9999번 포트로 실행:<br/>
python manage.py runserver 9999<br/>
<br/>
auth_server에서<br/>
python manage.py runserver 8888<br/>
<br/>
resource_server에서<br/>
python manage.py runserver 9999<br/>
<br/>
<br/>
8. gRPC 서버 실행 (auth_server)(미구현)<br/>
<br/>
bash<br/>
auth_server 디렉토리에서 gRPC 서버 실행<br/>
python grpc_server.py<br/>
<br/>

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