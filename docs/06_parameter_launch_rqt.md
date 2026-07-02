# 06. Parameter, Launch, rqt_graph

## Parameter

Parameter는 노드가 사용하는 설정값이다. 코드 안에 값을 고정하면 수정할 때마다 코드를 바꿔야 하지만, Parameter로 만들면 외부에서 값을 확인하거나 변경할 수 있다.

예를 들어 다음처럼 선언한다.

```python
self.declare_parameter('message', 'Hello ROS 2 Parameter')
self.declare_parameter('count_limit', 5)
```

값을 읽을 때는 다음처럼 사용한다.

```python
message = self.get_parameter('message').value
count_limit = self.get_parameter('count_limit').value
```

## Parameter 확인 및 변경 명령어

```bash
ros2 param list /parameter_node
ros2 param get /parameter_node message
ros2 param set /parameter_node message "Changed from terminal"
ros2 param set /parameter_node count_limit 3
```

핵심은 코드를 다시 수정하지 않아도 실행 중인 노드의 설정값을 바꿀 수 있다는 점이다.

## Launch

Launch는 여러 노드를 한 번에 실행하기 위한 파일이다.

실제 로봇 시스템에서는 카메라, 라이다, 모터 제어, 위치 추정, 경로 계획 등 여러 노드가 동시에 실행되어야 한다. 이런 노드를 매번 터미널에서 하나씩 실행하는 것은 불편하므로 Launch 파일로 묶는다.

## Publisher/Subscriber Launch 예시

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    publisher = Node(
        package='my_first_ros',
        executable='publisher_node',
        name='my_publisher'
    )

    subscriber = Node(
        package='my_first_ros',
        executable='subscriber_node',
        name='my_subscriber'
    )

    return LaunchDescription([
        publisher,
        subscriber
    ])
```

실행:

```bash
ros2 launch my_first_ros pubsub.launch.py
```

## Launch에서 Parameter 넣기

Launch 파일에서 노드를 실행할 때 Parameter 값을 미리 넣을 수 있다.

```python
Node(
    package='my_first_ros',
    executable='parameter_node',
    name='parameter_node',
    parameters=[
        {'message': 'Hello from launch file'},
        {'count_limit': 10}
    ]
)
```

이렇게 하면 노드가 시작할 때부터 해당 Parameter 값이 적용된다.

## setup.py에서 launch 파일 설치 규칙 추가

`ament_python` 패키지에서는 launch 파일을 만들기만 하면 `ros2 launch`가 바로 찾지 못한다. `setup.py`의 `data_files`에 launch 파일 설치 규칙을 추가해야 한다.

```python
import os
from glob import glob
```

```python
(os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
```

이 설정을 추가한 뒤 다시 빌드해야 한다.

```bash
cd ~/ros_study
colcon build --packages-select my_first_ros
source install/setup.bash
```

## rqt_graph

`rqt_graph`는 현재 실행 중인 Node와 Topic의 연결 관계를 그림으로 보여주는 도구다.

```bash
rqt_graph
```

처음 그래프가 비어 보이면 다음을 확인한다.

- 상단 드롭다운을 `Nodes/Topics (all)`로 변경
- 새로고침 버튼 클릭
- Hide 필터 확인

## 확인한 구조

```text
/my_publisher
  → /chatter
  → /my_subscriber
```

rqt_graph를 통해 실제로 Publisher가 Topic으로 메시지를 보내고, Subscriber가 그 Topic을 구독하는 구조를 눈으로 확인했다.
