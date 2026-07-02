# setup.py 등록 예시

Python 기반 ROS 2 패키지에서는 새 실행 파일을 만들 때마다 `setup.py`의 `console_scripts`에 등록해야 한다.

```python
entry_points={
    'console_scripts': [
        'first_node = my_first_ros.first_node:main',
        'timer_node = my_first_ros.timer_node:main',
        'publisher_node = my_first_ros.publisher_node:main',
        'subscriber_node = my_first_ros.subscriber_node:main',
        'add_two_ints_server = my_first_ros.add_two_ints_server:main',
        'add_two_ints_client = my_first_ros.add_two_ints_client:main',
        'parameter_node = my_first_ros.parameter_node:main',
        'auto_turtle_node = my_first_ros.auto_turtle_node:main',
        'square_turtle_node = my_first_ros.square_turtle_node:main',
        'pose_subscriber_node = my_first_ros.pose_subscriber_node:main',
        'wall_avoid_turtle_node = my_first_ros.wall_avoid_turtle_node:main',
    ],
},
```

Launch 파일을 설치 대상으로 포함하려면 `setup.py` 상단에 다음 import가 필요하다.

```python
import os
from glob import glob
```

그리고 `data_files`에 다음 항목을 추가한다.

```python
(os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
```

이 설정이 없으면 `src` 폴더에 launch 파일을 만들어도 `ros2 launch my_first_ros 파일명.launch.py` 명령이 해당 파일을 찾지 못할 수 있다.
