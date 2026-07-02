# 08. 자주 만난 오류와 해결

## ros2: command not found

### 원인

새 터미널에서 ROS 2 환경을 source 하지 않았기 때문이다.

### 해결

```bash
source /opt/ros/jazzy/setup.bash
```

작업공간 패키지까지 사용하려면 다음도 실행한다.

```bash
cd ~/ros_study
source install/setup.bash
```

## /opt/ros/humble/setup.bash: No such file or directory

### 원인

현재 설치된 ROS 2 배포판은 Humble이 아니라 Jazzy이다.

### 해결

```bash
source /opt/ros/jazzy/setup.bash
```

## source install/setup.bash: No such file or directory

### 원인

현재 위치가 작업공간 루트인 `~/ros_study`가 아니기 때문이다.

### 해결

```bash
cd ~/ros_study
source install/setup.bash
```

## colcon: command not found

### 원인

ROS 2 패키지를 빌드하는 도구인 `colcon`이 설치되어 있지 않다.

### 해결

```bash
sudo apt update
sudo apt install python3-colcon-common-extensions
```

## setup.py에서 NameError: name 'os' is not defined

### 원인

`setup.py`에서 `os.path.join()`을 사용했지만 `import os`를 하지 않았다.

### 해결

`setup.py` 맨 위에 다음을 추가한다.

```python
import os
from glob import glob
```

## ros2 launch에서 launch 파일을 찾지 못함

### 원인

launch 파일을 만들었지만 `setup.py`의 `data_files`에 launch 설치 규칙을 추가하지 않았거나, 빌드를 다시 하지 않았다.

### 해결

`setup.py`에 다음을 추가한다.

```python
(os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
```

그 후 다시 빌드한다.

```bash
cd ~/ros_study
colcon build --packages-select my_first_ros
source install/setup.bash
```

## rqt_graph에 아무것도 안 보임

### 원인

보기 설정이 `Nodes only`로 되어 있거나, 필터 때문에 Topic이 숨겨져 있을 수 있다.

### 해결

- 상단 드롭다운을 `Nodes/Topics (all)`로 변경
- 새로고침 버튼 클릭
- Hide 필터 확인

## Node not found

### 원인

확인하려는 노드가 아직 실행 중이 아니거나, launch 실행이 끝났을 수 있다.

### 해결

먼저 노드가 실행 중인지 확인한다.

```bash
ros2 node list
```

노드가 없으면 해당 노드를 다시 실행한다.

## Ctrl + C 후 KeyboardInterrupt 출력

### 원인

실행 중인 Python 노드를 사용자가 강제로 종료했기 때문이다.

### 해결

실패가 아니다. ROS 2 노드를 끌 때 흔히 볼 수 있는 정상 종료 흔적이다.

## TurtleSim GUI가 안 보임

### 원인

창이 뒤에 숨었거나 WSL GUI 포커스가 꼬였을 수 있다.

### 해결

Alt+Tab으로 창을 찾아보고, 그래도 안 보이면 WSL을 재실행한다.

```bash
wsl --shutdown
```

## 로그가 너무 많이 출력됨

### 원인

`/turtle1/pose`는 계속 발행되는 토픽이고, 구독 콜백도 계속 실행된다.

### 해결

정상 동작이다. 필요하면 나중에 출력 주기를 조절하거나 일정 조건에서만 로그를 찍도록 수정하면 된다.
