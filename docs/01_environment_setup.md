# 01. 환경 구축과 시작 루틴

## 사용 환경

| 항목 | 내용 |
|---|---|
| Windows 환경 | WSL2 사용 |
| Linux 배포판 | Ubuntu 24.04 LTS |
| ROS 2 배포판 | Jazzy Jalisco |
| 작업공간 | `~/ros_study` |
| 실습 패키지 | `my_first_ros` |

## WSL과 Ubuntu

ROS 2는 Linux 환경에서 많이 사용된다. Windows에서도 WSL2를 이용하면 Ubuntu를 실행할 수 있고, 그 안에서 ROS 2를 설치해 실습할 수 있다.

이번 실습에서는 Windows 안에서 Ubuntu 24.04를 실행하고, 그 위에 ROS 2 Jazzy를 설치했다.

## ROS 2 Jazzy 환경 적용

새 터미널을 열면 ROS 2 명령어가 바로 인식되지 않을 수 있다. 그래서 아래 명령어로 ROS 2 환경을 현재 터미널에 적용해야 한다.

```bash
source /opt/ros/jazzy/setup.bash
```

정상 적용 여부는 다음 명령어로 확인한다.

```bash
echo $ROS_DISTRO
```

출력이 `jazzy`이면 정상이다.

## 작업공간 환경 적용

직접 만든 패키지를 사용하려면 작업공간으로 이동한 뒤 `install/setup.bash`도 source 해야 한다.

```bash
cd ~/ros_study
source /opt/ros/jazzy/setup.bash
source install/setup.bash
```

둘의 차이는 다음과 같다.

| 명령어 | 의미 |
|---|---|
| `source /opt/ros/jazzy/setup.bash` | ROS 2 Jazzy 자체를 현재 터미널에서 사용할 수 있게 함 |
| `source install/setup.bash` | 내가 빌드한 작업공간의 패키지를 현재 터미널에서 사용할 수 있게 함 |

## 기본 시작 루틴

ROS 공부를 시작할 때는 아래 세 줄을 먼저 입력한다.

```bash
cd ~/ros_study
source /opt/ros/jazzy/setup.bash
source install/setup.bash
```

## 패키지 수정 후 빌드 루틴

Python 파일, `setup.py`, `package.xml`, launch 파일 등을 수정했다면 다시 빌드해야 한다.

```bash
cd ~/ros_study
colcon build --packages-select my_first_ros
source install/setup.bash
```

## 자주 사용한 Linux 명령어

| 명령어 | 의미 |
|---|---|
| `pwd` | 현재 위치 확인 |
| `ls` | 파일/폴더 목록 확인 |
| `cd` | 폴더 이동 |
| `mkdir` | 폴더 생성 |
| `touch` | 빈 파일 생성 |
| `nano` | 터미널 텍스트 편집기 실행 |
| `sudo apt update` | 패키지 목록 최신화 |
| `sudo apt install 패키지명` | 패키지 설치 |

## 처음에 만난 핵심 오류

`ros2: command not found`는 대부분 ROS 2가 설치되지 않았거나, 현재 터미널에 `source /opt/ros/jazzy/setup.bash`를 하지 않았다는 뜻이다.

`/opt/ros/humble/setup.bash: No such file or directory`는 현재 설치된 배포판이 Humble이 아니라 Jazzy였기 때문에 발생했다. 이번 실습 환경에서는 항상 `jazzy` 경로를 사용한다.
