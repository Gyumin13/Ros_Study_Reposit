# 03. 작업공간, 패키지, 첫 노드

## 작업공간 구조

이번 실습의 작업공간은 `~/ros_study`이다.

```text
~/ros_study/
├── src/
│   └── my_first_ros/
├── build/
├── install/
└── log/
```

| 폴더 | 의미 |
|---|---|
| `src/` | 직접 작성한 패키지 원본이 들어가는 곳 |
| `build/` | 빌드 과정에서 생기는 파일 |
| `install/` | 빌드 후 실행 가능한 결과물이 설치되는 곳 |
| `log/` | 빌드와 실행 로그 |

## 패키지 생성

Python 기반 ROS 2 패키지를 만들 때 사용한 명령어는 다음과 같다.

```bash
cd ~/ros_study
mkdir -p src
cd src
ros2 pkg create my_first_ros --build-type ament_python --dependencies rclpy std_msgs
```

명령어 의미는 다음과 같다.

| 부분 | 의미 |
|---|---|
| `ros2 pkg create` | 새 ROS 2 패키지 생성 |
| `my_first_ros` | 패키지 이름 |
| `--build-type ament_python` | Python 기반 패키지 |
| `--dependencies rclpy std_msgs` | 필요한 의존성 지정 |

## colcon 빌드

ROS 2 패키지는 만든 뒤 바로 실행하는 것이 아니라 `colcon build`로 빌드해야 한다.

```bash
cd ~/ros_study
colcon build --packages-select my_first_ros
source install/setup.bash
```

처음에는 `colcon`이 설치되어 있지 않아 실패했기 때문에 다음 패키지를 설치했다.

```bash
sudo apt update
sudo apt install python3-colcon-common-extensions
```

## 첫 노드 작성

`first_node.py`는 가장 처음 만든 ROS 2 Python 노드다.

```python
import rclpy
from rclpy.node import Node


class FirstNode(Node):
    def __init__(self):
        super().__init__('first_node')
        self.get_logger().info('Hello, this is my first ROS 2 node!')


def main(args=None):
    rclpy.init(args=args)
    node = FirstNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

핵심은 `Node`를 상속한 클래스를 만들고, `rclpy.spin(node)`로 노드가 계속 살아 있게 한다는 점이다.

## setup.py 등록

Python 파일을 만들었다고 바로 `ros2 run`으로 실행할 수 있는 것은 아니다. `setup.py`의 `console_scripts`에 실행 이름을 등록해야 한다.

```python
entry_points={
    'console_scripts': [
        'first_node = my_first_ros.first_node:main',
    ],
},
```

등록 후에는 다시 빌드한다.

```bash
cd ~/ros_study
colcon build --packages-select my_first_ros
source install/setup.bash
```

## 실행

```bash
ros2 run my_first_ros first_node
```

정상 실행되면 로그가 출력된다.

```text
[first_node]: Hello, this is my first ROS 2 node!
```

## 노드 확인

다른 터미널에서 다음 명령어를 실행하면 현재 살아 있는 노드 목록을 볼 수 있다.

```bash
ros2 node list
```

`/first_node`가 보이면 직접 만든 노드가 ROS 2 시스템 안에서 정상 실행 중이라는 뜻이다.
