# 09. 일차별 학습 기록

## Day 1

WSL2와 Ubuntu 24.04를 설치하고 Linux 기본 명령어를 실습했다. ROS 2 설치를 위한 저장소 등록도 진행했다.

핵심 내용:

- WSL2 설치
- Ubuntu 24.04 설치
- Linux 기본 명령어 학습
- ROS 저장소 등록

## Day 2

ROS 2 Jazzy를 설치하고 talker/listener 예제를 실행했다.

핵심 구조:

```text
talker → /chatter → listener
```

## Day 3

ROS 2의 Topic 구조를 다시 복습하고, `ros2 topic pub` 명령어로 직접 `/chatter` Topic에 메시지를 발행했다.

## Day 4

`my_first_ros` 패키지를 만들고, 직접 작성한 첫 Python 노드인 `first_node`를 실행했다.

핵심 구조:

```text
my_first_ros 패키지
  → first_node.py
  → ros2 run my_first_ros first_node
```

## Day 5

Timer 노드와 Topic 기반 Publisher/Subscriber 통신을 실습했다.

핵심 구조:

```text
publisher_node → /chatter → subscriber_node
```

## Day 6

Service Server/Client 구조를 실습했다.

핵심 구조:

```text
add_two_ints_client → /add_two_ints → add_two_ints_server
```

## Day 7

Parameter와 Launch를 실습했다.

- `ros2 param list/get/set`
- `pubsub.launch.py`
- `publisher_node`와 `subscriber_node` 동시 실행

## Day 8~9

Launch 파일에서 Parameter 값을 미리 넣어 실행했고, rqt_graph로 Pub/Sub 구조를 시각적으로 확인했다.

핵심 구조:

```text
/my_publisher → /chatter → /my_subscriber
```

## Day 10

Turtlesim을 실행하고 키보드 조종, Topic 직접 발행, Python 자동 제어 노드를 실습했다.

핵심 Topic:

- `/turtle1/cmd_vel`
- `/turtle1/pose`

## Day 11

`square_turtle_node.py`를 작성해 거북이를 전진/회전 반복 방식으로 움직였다.

핵심 구조:

```text
/square_turtle_node → /turtle1/cmd_vel → /turtlesim
```

## Day 12~14

`/turtle1/pose`를 구독하고, 벽 근처 여부를 판단해 `/turtle1/cmd_vel`로 이동 명령을 발행하는 피드백 제어 노드를 구현했다.

최종 구조:

```text
/turtlesim
  → /turtle1/pose
  → /wall_avoid_turtle_node
  → /turtle1/cmd_vel
  → /turtlesim
```

최종적으로 ROS 2 입문 핵심 흐름인 Node, Topic, Service, Parameter, Launch, rqt_graph, Turtlesim 제어를 한 번씩 실습했다.
