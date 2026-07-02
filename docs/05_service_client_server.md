# 05. Service Server/Client

## Service란?

Service는 요청과 응답 구조를 가진 ROS 2 통신 방식이다.

Topic이 계속 흘러가는 방송이라면, Service는 필요할 때 질문을 보내고 답을 받는 방식이다.

## 이번 실습 구조

```text
add_two_ints_client
  → /add_two_ints Service
  → add_two_ints_server
```

Client가 두 정수 `a`, `b`를 요청으로 보내면, Server가 두 수를 더해서 `sum`을 응답으로 돌려준다.

## Topic과 Service 비교

| 구분 | Topic | Service |
|---|---|---|
| 느낌 | 계속 흐르는 방송 | 질문과 답변 |
| 통신 방식 | Publisher가 계속 발행 | Client가 요청하면 Server가 응답 |
| 응답 여부 | 기본적으로 응답 없음 | 요청에 대한 응답 있음 |
| 예시 | 센서값, 카메라 영상, 로봇 속도 명령 | 두 숫자 더하기, 특정 동작 시작 요청 |

## Service Server 핵심 코드

```python
from example_interfaces.srv import AddTwoInts

self.srv = self.create_service(
    AddTwoInts,
    'add_two_ints',
    self.add_two_ints_callback
)

def add_two_ints_callback(self, request, response):
    response.sum = request.a + request.b
    return response
```

| 코드 | 의미 |
|---|---|
| `AddTwoInts` | 두 정수를 요청으로 받고 합을 응답하는 Service 타입 |
| `create_service()` | 이 노드를 Service Server로 등록 |
| `'add_two_ints'` | 서비스 이름 |
| `request.a`, `request.b` | Client가 보낸 요청값 |
| `response.sum` | Server가 돌려줄 응답값 |

## 명령어로 Service 호출

Server가 실행 중일 때 다른 터미널에서 다음 명령어로 Service를 호출할 수 있다.

```bash
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 3, b: 4}"
```

응답은 다음처럼 나온다.

```text
sum=7
```

## Service Client 핵심 코드

```python
self.client = self.create_client(AddTwoInts, 'add_two_ints')

request = AddTwoInts.Request()
request.a = a
request.b = b

future = self.client.call_async(request)
rclpy.spin_until_future_complete(node, future)
response = future.result()
```

| 코드 | 의미 |
|---|---|
| `create_client()` | Service를 호출할 Client 생성 |
| `AddTwoInts.Request()` | 요청 객체 생성 |
| `call_async(request)` | 비동기 방식으로 요청 전송 |
| `spin_until_future_complete()` | 응답이 올 때까지 대기 |
| `future.result()` | 응답 꺼내기 |

## 실행 예시

Server 실행:

```bash
ros2 run my_first_ros add_two_ints_server
```

Client 실행:

```bash
ros2 run my_first_ros add_two_ints_client 10 20
```

정상 결과:

```text
Result: 10 + 20 = 30
```

## service list에서 보이는 추가 항목

`ros2 service list`를 실행하면 `/add_two_ints` 외에도 Parameter 관련 서비스들이 같이 보일 수 있다. 이것은 오류가 아니다. ROS 2 노드는 기본적으로 Parameter를 다루기 위한 서비스들을 함께 가지고 있다.

이번 실습에서 직접 만든 핵심 서비스는 `/add_two_ints`이다.
