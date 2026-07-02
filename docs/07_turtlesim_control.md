# 07. Turtlesim 제어

## Turtlesim이란?

Turtlesim은 ROS 2 입문자가 Topic, Message, Service, Parameter 등을 눈으로 확인할 수 있게 해주는 간단한 2D 시뮬레이터다.

거북이가 화면 위에서 움직이고, 우리는 ROS 2 Topic에 메시지를 보내 거북이를 제어할 수 있다.

## 기본 실행

```bash
ros2 run turtlesim turtlesim_node
```

키보드 조종 노드 실행:

```bash
ros2 run turtlesim turtle_teleop_key
```

기본 구조는 다음과 같다.

```text
/turtle_teleop_key
  → /turtle1/cmd_vel
  → /turtlesim
```

## 주요 Topic

| Topic | 의미 |
|---|---|
| `/turtle1/cmd_vel` | 거북이에게 이동 명령을 보내는 Topic |
| `/turtle1/pose` | 거북이의 현재 위치와 방향이 나오는 Topic |

## Twist 메시지

`/turtle1/cmd_vel`은 `geometry_msgs/msg/Twist` 타입을 사용한다.

| 필드 | 의미 |
|---|---|
| `linear.x` | 앞으로 가는 속도 |
| `angular.z` | 회전 속도 |

직접 Topic 발행:

```bash
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
```

## Pose 메시지

`/turtle1/pose`는 거북이의 현재 상태를 알려준다.

| 필드 | 의미 |
|---|---|
| `x` | 가로 위치 |
| `y` | 세로 위치 |
| `theta` | 바라보는 방향 |
| `linear_velocity` | 현재 직선 속도 |
| `angular_velocity` | 현재 회전 속도 |

확인 명령어:

```bash
ros2 topic echo /turtle1/pose
```

## 자동 제어 노드

`auto_turtle_node.py`와 `square_turtle_node.py`에서는 Python 노드가 `/turtle1/cmd_vel` Topic으로 Twist 메시지를 발행해 거북이를 자동으로 움직였다.

구조는 다음과 같다.

```text
/square_turtle_node
  → /turtle1/cmd_vel
  → /turtlesim
```

## 피드백 제어

마지막 실습에서는 거북이의 현재 위치를 구독하고, 그 위치를 바탕으로 다시 이동 명령을 보내는 구조를 만들었다.

```text
/turtlesim
  → /turtle1/pose
  → /wall_avoid_turtle_node
  → /turtle1/cmd_vel
  → /turtlesim
```

이 구조는 다음 세 단계로 이해하면 된다.

```text
상태 읽기 → 판단하기 → 명령 보내기
```

## wall_avoid_turtle_node 핵심 아이디어

1. `/turtle1/pose`를 구독해서 현재 `x`, `y`, `theta`를 읽는다.
2. 거북이가 벽 근처인지 판단한다.
3. 벽 근처라면 중앙 방향으로 회전한다.
4. 안전 구역이면 앞으로 이동한다.
5. `/turtle1/cmd_vel`로 Twist 명령을 발행한다.

## Parameter 적용

최종적으로 속도와 벽 판단 기준을 Parameter로 관리했다.

| Parameter | 의미 |
|---|---|
| `forward_speed` | 평소 전진 속도 |
| `near_wall_speed` | 벽 근처에서의 속도 |
| `turn_gain` | 중앙 방향으로 회전하는 강도 |
| `wall_limit` | 벽 근처라고 판단하는 기준값 |
| `center_x`, `center_y` | 중앙 좌표 |

Launch 파일에서 시작값을 넣어 실행했다.

```python
parameters=[
    {
        'forward_speed': 0.8,
        'near_wall_speed': 0.5,
        'turn_gain': 4.0,
        'wall_limit': 3.0,
        'center_x': 5.5,
        'center_y': 5.5,
    }
]
```

## 최종 설명 문장

ROS 2에서 Turtlesim의 `/turtle1/pose` 토픽을 구독해 현재 위치를 읽고, 벽 근처 여부를 판단한 뒤 `/turtle1/cmd_vel` 토픽으로 이동 명령을 발행하는 간단한 피드백 제어 노드를 구현했다.
