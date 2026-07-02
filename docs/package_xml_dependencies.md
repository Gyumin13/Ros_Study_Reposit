# package.xml 의존성 예시

이번 실습에서 사용한 주요 의존성은 다음과 같다.

```xml
<depend>rclpy</depend>
<depend>std_msgs</depend>
<depend>example_interfaces</depend>
<depend>geometry_msgs</depend>
<depend>turtlesim</depend>

<exec_depend>launch</exec_depend>
<exec_depend>launch_ros</exec_depend>
```

각 의존성의 의미는 다음과 같다.

| 의존성 | 의미 |
|---|---|
| `rclpy` | Python으로 ROS 2 노드를 만들 때 사용 |
| `std_msgs` | 문자열 등 기본 메시지 타입 |
| `example_interfaces` | `AddTwoInts` 같은 예제 Service 타입 |
| `geometry_msgs` | `Twist` 같은 로봇 이동 관련 메시지 타입 |
| `turtlesim` | Turtlesim의 `Pose` 메시지 사용 |
| `launch`, `launch_ros` | Launch 파일 실행에 필요 |

새로운 메시지 타입이나 Service 타입을 사용할 때는 코드 import만 추가하는 것이 아니라 `package.xml` 의존성도 함께 확인해야 한다.
