# 04. Topic, Timer, Publisher/Subscriber

## Timer 노드

Timer는 일정 시간마다 함수를 반복 실행하게 해주는 기능이다.

```python
self.timer = self.create_timer(1.0, self.timer_callback)
```

위 코드는 1초마다 `timer_callback` 함수를 실행하라는 뜻이다.

로봇 프로그램은 센서 읽기, 상태 확인, 명령 계산 등을 계속 반복하는 경우가 많기 때문에 Timer는 자주 사용된다.

## Publisher

Publisher는 Topic에 메시지를 보내는 노드다.

```python
self.publisher = self.create_publisher(String, 'chatter', 10)
```

의미는 다음과 같다.

| 부분 | 의미 |
|---|---|
| `String` | 보낼 메시지 타입 |
| `'chatter'` | 메시지를 보낼 Topic 이름 |
| `10` | 메시지 대기열 크기 |

메시지를 실제로 보낼 때는 다음처럼 작성한다.

```python
msg = String()
msg.data = f'Hello ROS 2 Publisher: {self.count}'
self.publisher.publish(msg)
```

## Subscriber

Subscriber는 특정 Topic을 구독해서 메시지를 받는 노드다.

```python
self.subscription = self.create_subscription(
    String,
    'chatter',
    self.listener_callback,
    10
)
```

의미는 다음과 같다.

| 부분 | 의미 |
|---|---|
| `String` | 받을 메시지 타입 |
| `'chatter'` | 구독할 Topic 이름 |
| `self.listener_callback` | 메시지가 들어오면 실행할 함수 |
| `10` | 메시지 대기열 크기 |

메시지를 받으면 callback 함수가 실행된다.

```python
def listener_callback(self, msg):
    self.get_logger().info(f'I heard: "{msg.data}"')
```

## 최종 구조

```text
publisher_node
  → /chatter
  → subscriber_node
```

Publisher가 `/chatter` Topic에 문자열 메시지를 발행하고, Subscriber가 같은 Topic을 구독해서 메시지를 받는다.

## 확인 명령어

| 명령어 | 의미 |
|---|---|
| `ros2 topic list` | 현재 존재하는 Topic 목록 확인 |
| `ros2 topic echo /chatter` | `/chatter`에 흐르는 메시지 출력 |
| `ros2 topic info /chatter` | Topic 타입, Publisher 수, Subscriber 수 확인 |
| `ros2 node list` | 현재 실행 중인 Node 목록 |
| `ros2 node info /노드이름` | 특정 Node의 발행/구독 정보 확인 |

## 성공 기준

Publisher 터미널에 다음처럼 출력되고,

```text
[publisher_node]: Publishing: "Hello ROS 2 Publisher: 1"
```

Subscriber 터미널에 다음처럼 출력되면 성공이다.

```text
[subscriber_node]: I heard: "Hello ROS 2 Publisher: 1"
```

## 쉽게 비유하면

`publisher_node`는 방송실에서 말을 하는 사람이고, `/chatter`는 방송 채널이며, `subscriber_node`는 그 방송을 듣는 교실이다. 방송실에서 말한 내용이 채널을 통해 교실로 전달되는 구조다.
