# 02. ROS 2 핵심 개념

## ROS 2란?

ROS 2는 Robot Operating System 2의 약자다. 이름에 Operating System이 들어가지만 Windows나 Ubuntu 같은 일반 운영체제라기보다는, 로봇 프로그램을 여러 모듈로 나누고 서로 통신하게 해주는 로봇 소프트웨어 프레임워크에 가깝다.

즉, ROS 2는 로봇을 만들 때 필요한 통신 구조, 실행 구조, 도구들을 제공한다.

## 핵심 구조

```text
Node  →  Topic  →  Node
```

ROS 2에서는 하나의 큰 프로그램이 모든 일을 처리하기보다, 여러 개의 작은 프로그램인 Node들이 각자 역할을 맡는다. 그리고 Topic, Service 등을 통해 필요한 정보를 주고받는다.

## 주요 용어

| 용어 | 의미 | 예시 |
|---|---|---|
| Node | 실행되는 ROS 프로그램 하나 | `talker`, `listener`, `publisher_node` |
| Topic | 메시지가 오가는 통신 통로 | `/chatter`, `/turtle1/cmd_vel` |
| Message | Topic으로 오가는 데이터 형식과 실제 값 | `std_msgs/msg/String`, `geometry_msgs/msg/Twist` |
| Publisher | Topic에 메시지를 보내는 쪽 | `talker`, `publisher_node` |
| Subscriber | Topic에서 메시지를 받는 쪽 | `listener`, `subscriber_node` |
| Package | 코드와 설정을 묶은 단위 | `my_first_ros` |
| Workspace | 여러 패키지를 모아두는 작업공간 | `~/ros_study` |
| Service | 요청과 응답을 주고받는 통신 방식 | `/add_two_ints` |
| Parameter | 노드의 설정값 | `message`, `count_limit`, `forward_speed` |
| Launch | 여러 노드를 한 번에 실행하는 파일 | `pubsub.launch.py` |
| rqt_graph | 노드와 토픽 연결을 그림으로 보여주는 도구 | `/my_publisher → /chatter → /my_subscriber` |

## Topic과 Service 차이

| 구분 | Topic | Service |
|---|---|---|
| 느낌 | 방송 | 질문과 답변 |
| 방식 | Publisher가 계속 메시지를 발행 | Client가 요청하면 Server가 응답 |
| 응답 여부 | 기본적으로 응답 없음 | 요청에 대한 응답 있음 |
| 예시 | 센서값, 카메라 영상, 로봇 속도 명령 | 두 숫자 더하기, 로봇 상태 요청, 특정 동작 시작 |

## 이번 공부에서 가장 중요한 사고방식

ROS에서는 “프로그램 A가 프로그램 B에게 직접 보낸다”보다 “A가 Topic에 메시지를 올리고, B가 그 Topic을 구독해서 본다”라고 이해하는 것이 좋다.

예를 들어 talker/listener 예제는 다음 구조다.

```text
talker 노드
  → /chatter 토픽
  → listener 노드
```

talker가 listener에게 직접 보내는 것이 아니라, talker가 `/chatter`에 메시지를 발행하고 listener가 `/chatter`를 구독한다.

## ROS 그래프 관점

ROS 시스템을 볼 때는 “지금 어떤 노드가 살아 있는지”, “어떤 토픽이 있는지”, “그 토픽의 타입은 무엇인지”, “누가 발행하고 누가 구독하는지”를 확인하는 습관이 중요하다.

자주 쓰는 확인 명령어는 다음과 같다.

```bash
ros2 node list
ros2 topic list
ros2 topic info /chatter
ros2 topic echo /chatter
ros2 node info /listener
```
