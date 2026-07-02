# ROS 2 Jazzy Study Repository

WSL2 + Ubuntu 24.04 환경에서 ROS 2 Jazzy를 설치하고, ROS 2 기본 개념과 실습 내용을 단계적으로 정리한 학습 기록 저장소입니다.

처음 ROS를 공부하는 사람이 전체 흐름을 다시 따라갈 수 있도록 `Node`, `Topic`, `Service`, `Parameter`, `Launch`, `rqt_graph`, `Turtlesim` 제어까지 연결해서 정리했습니다.

## 학습 환경

| 항목 | 내용 |
|---|---|
| OS 환경 | Windows + WSL2 |
| Linux 배포판 | Ubuntu 24.04 LTS |
| ROS 배포판 | ROS 2 Jazzy Jalisco |
| 작업공간 | `~/ros_study` |
| 실습 패키지 | `my_first_ros` |
| 주 사용 언어 | Python (`rclpy`) |

## 전체 학습 흐름

```text
환경 구축
  ↓
ROS 2 Jazzy 설치 및 talker/listener 예제 실행
  ↓
작업공간과 패키지 생성
  ↓
첫 ROS 2 Python 노드 작성
  ↓
Timer, Topic, Publisher/Subscriber 실습
  ↓
Service Server/Client 요청-응답 통신
  ↓
Parameter와 Launch 실습
  ↓
rqt_graph로 노드/토픽 구조 시각화
  ↓
Turtlesim으로 실제 움직임 확인
  ↓
/turtle1/pose 구독 + /turtle1/cmd_vel 발행 기반 피드백 제어
```

## 핵심 개념 요약

| 개념 | 의미 | 이번 실습에서의 예 |
|---|---|---|
| Node | ROS에서 실행되는 하나의 프로그램 단위 | `publisher_node`, `subscriber_node`, `wall_avoid_turtle_node` |
| Topic | 노드끼리 메시지를 주고받는 통로 | `/chatter`, `/turtle1/cmd_vel`, `/turtle1/pose` |
| Message | Topic을 통해 오가는 데이터 형식 | `std_msgs/msg/String`, `geometry_msgs/msg/Twist`, `turtlesim/msg/Pose` |
| Publisher | Topic에 메시지를 보내는 쪽 | `publisher_node`, `square_turtle_node` |
| Subscriber | Topic에서 메시지를 받는 쪽 | `subscriber_node`, `pose_subscriber_node` |
| Service | 요청을 보내고 응답을 받는 통신 방식 | `/add_two_ints` |
| Parameter | 코드 수정 없이 바꿀 수 있는 노드 설정값 | `forward_speed`, `wall_limit`, `turn_gain` |
| Launch | 여러 노드를 한 번에 실행하는 파일 | `pubsub.launch.py`, `wall_avoid.launch.py` |
| rqt_graph | 노드와 토픽 연결 관계를 시각화하는 도구 | `/wall_avoid_turtle_node → /turtle1/cmd_vel → /turtlesim` |

## 문서 구조

| 파일 | 내용 |
|---|---|
| [`docs/01_environment_setup.md`](docs/01_environment_setup.md) | WSL, Ubuntu, ROS 2 Jazzy 설치 및 시작 루틴 |
| [`docs/02_ros2_core_concepts.md`](docs/02_ros2_core_concepts.md) | Node, Topic, Message, Package 등 핵심 개념 |
| [`docs/03_workspace_package_node.md`](docs/03_workspace_package_node.md) | 작업공간, 패키지, 첫 노드 생성 |
| [`docs/04_topic_pubsub.md`](docs/04_topic_pubsub.md) | Timer, Publisher, Subscriber, `/chatter` 통신 |
| [`docs/05_service_client_server.md`](docs/05_service_client_server.md) | Service Server/Client 요청-응답 통신 |
| [`docs/06_parameter_launch_rqt.md`](docs/06_parameter_launch_rqt.md) | Parameter, Launch, rqt_graph 정리 |
| [`docs/07_turtlesim_control.md`](docs/07_turtlesim_control.md) | Turtlesim 제어, Twist, Pose, 피드백 제어 |
| [`docs/08_troubleshooting.md`](docs/08_troubleshooting.md) | 자주 만난 오류와 해결 방법 |
| [`docs/09_learning_log.md`](docs/09_learning_log.md) | 일차별 학습 기록 |

## 예제 코드 구조

```text
src/my_first_ros_examples/
├── first_node.py
├── timer_node.py
├── publisher_node.py
├── subscriber_node.py
├── add_two_ints_server.py
├── add_two_ints_client.py
├── parameter_node.py
├── auto_turtle_node.py
├── square_turtle_node.py
├── pose_subscriber_node.py
└── wall_avoid_turtle_node.py

launch/
├── pubsub.launch.py
├── parameter.launch.py
└── wall_avoid.launch.py
```

> `src/my_first_ros_examples` 폴더는 학습 내용을 정리하기 위한 예제 코드 모음입니다. 실제 ROS 2 패키지에서 실행하려면 `~/ros_study/src/my_first_ros/my_first_ros/` 내부에 파일을 배치하고, `setup.py`의 `console_scripts`에 실행 항목을 등록해야 합니다.

## 기본 실행 루틴

새 터미널을 열 때마다 아래 명령어를 먼저 실행합니다.

```bash
cd ~/ros_study
source /opt/ros/jazzy/setup.bash
source install/setup.bash
```

패키지를 수정한 뒤에는 다시 빌드합니다.

```bash
cd ~/ros_study
colcon build --packages-select my_first_ros
source install/setup.bash
```

## 최종 실습 구조

```text
/turtlesim
  → /turtle1/pose
  → /wall_avoid_turtle_node
  → /turtle1/cmd_vel
  → /turtlesim
```

이 구조는 거북이의 현재 위치를 읽고, 벽 근처 여부를 판단한 뒤, 이동 명령을 다시 보내는 간단한 피드백 제어 흐름입니다.

## 다음 학습 후보

현재 저장소는 ROS 2 입문 핵심 구조를 정리한 단계입니다. 이후에는 다음 내용을 이어서 공부할 수 있습니다.

- TF2: 로봇 좌표계 관리
- URDF: 로봇 모델 작성
- RViz2: 센서와 로봇 상태 시각화
- Gazebo: 로봇 시뮬레이션
- SLAM: 지도 작성
- Navigation2: 자율주행 경로 계획 및 이동
- 실제 센서 또는 카메라 기반 ROS 2 프로젝트
