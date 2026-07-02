# 00. 전체 학습 요약

이번 ROS 2 공부의 목표는 ROS를 처음 접하는 상태에서, 최소한 ROS 2의 기본 구조를 설명하고 간단한 실습 코드를 직접 실행할 수 있는 수준까지 가는 것이었다.

최종적으로 WSL/Ubuntu 환경에서 ROS 2 Jazzy를 설치하고, 직접 Python 노드를 작성해 Topic, Service, Parameter, Launch, rqt_graph, Turtlesim 피드백 제어까지 실습했다.

## 한 문장으로 정리

ROS 2는 하나의 큰 프로그램이 아니라, 여러 개의 Node가 Topic, Service 등을 통해 데이터를 주고받으며 로봇 시스템을 구성하게 해주는 미들웨어다.

## 학습 단계

| 단계 | 내용 | 결과 |
|---|---|---|
| 1 | WSL2, Ubuntu 24.04 설치 | Linux 기반 ROS 실습 환경 준비 |
| 2 | ROS 2 Jazzy 설치 | `ros2` 명령어 사용 가능 |
| 3 | talker/listener 예제 실행 | 기본 Topic 통신 확인 |
| 4 | `my_first_ros` 패키지 생성 | 직접 만든 패키지 인식 성공 |
| 5 | 첫 Python 노드 작성 | `ros2 run`으로 직접 만든 노드 실행 |
| 6 | Timer, Publisher, Subscriber 작성 | `/chatter` 통신 성공 |
| 7 | Service Server/Client 작성 | `/add_two_ints` 요청-응답 성공 |
| 8 | Parameter 실습 | 실행 중 설정값 변경 성공 |
| 9 | Launch 실습 | 여러 노드 동시 실행 성공 |
| 10 | rqt_graph 실습 | 노드/토픽 연결 구조 시각화 |
| 11 | Turtlesim 실습 | 거북이 조종 및 자동 제어 |
| 12~14 | Pose 구독 + 벽 회피 제어 | 피드백 제어 구조 구현 |

## 현재 수준

현재는 ROS 2의 입문 핵심 개념을 한 번 실습해본 상태다. 즉, 실무 프로젝트를 바로 할 정도는 아니지만, ROS 2의 기본 문법과 구조를 설명하고 간단한 노드를 만들 수 있는 단계다.

정확히 표현하면 다음과 같다.

> ROS 2의 Node, Topic, Service, Parameter, Launch 구조를 이해하고, Turtlesim을 이용해 간단한 제어 노드를 직접 구현해본 상태.

## 교수님께 설명할 수 있는 문장

ROS 2 Jazzy를 WSL/Ubuntu 환경에 설치하고, Python 기반 패키지를 만들어 Node, Topic, Service, Parameter, Launch를 실습했습니다. 이후 Turtlesim을 이용해 `/turtle1/pose` 토픽을 구독하고, `/turtle1/cmd_vel` 토픽으로 이동 명령을 발행하는 간단한 피드백 제어 노드까지 구현했습니다.
