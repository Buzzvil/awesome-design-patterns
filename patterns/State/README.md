# State

## TL;DR

- State 디자인 패턴은 객체의 내부 상태가 변경될 때 객체가 동작을 변경할 수 있도록 하는 디자인 패턴입니다.
- 객체의 각 상태를 클래스로 분리합니다. 그리고 객체가 어떤 동작을 수행해야 할 때 상태가 행위를 수행하도록 위임합니다.

## Problem
- 테니스 코트를 예약하는 시스템이 있다고 해봅시다.
- 테니스 코트에는 예약 가능, 예약 진행중, 예약 완료 세 가지 상태가 있습니다.
- 각 상태별로 예약, 결제, 취소 기능이 구현되어야 기니다. 예를 들면,
    - '예약 가능' 코트에 예약 동작을 수행하면 코트는 '예약 진행중'으로 변합니다.
    - '예약 가능' 코트에 결제나 취소 동작을 수행하면 동작이 불가능하다는 안내를 띄워줍니다.
- 각 메서드에서 현재 상태를 고려해서 적절한 동작을 수행하게 하는 것은 어렵지 않습니다.
- 하지만 더 많은 상태와 동작이 추가될수록 코드를 관리하기 어려워집니다. 예를 들면 코트에 '수리중'이라는 상태가 추가된다면, 기존에 구현된 메서드를 수정해야하며 메서드는 점점 복잡해질 것입니다.

## Solution
- 테니스 코트의 가능한 모든 상태를 클래스로 분리하고, 상태별 동작을 분리한 클래스에 구현합니다.
- 테니스 코트는 상태 객체를 가지고 있고, 상태 객체가 실질적인 동작을 수행하도록 위임합니다.

## Structure
![image](http://www.plantuml.com/plantuml/png/SoWkIImgAStDuKhEIImkLWYkB2v9pQtcKb18oO_Foa-ATzJGH72Sa3dEO4voHc9UUceyq9YIL0qmgSbLo-MPLv9Qb9QOdAeG318YqZoGJgWxdFFpaejIIrB1sXqLY3S0JRz_Kd5gKLbgaHCfHd1neLclMwfh1_495uR1o9AGq5FGoz63YN0vfEQbW88N0000)


## Pros & Cons
장점
- 기존 코드를 변경하지 않고 새로운 상태를 추가할 수 있어서 개방 폐쇄 원칙(Open-Closed Principle)을 준수합니다.
- 특정 상태와 관련된 코드를 별도의 클래스로 구성하여 단일 책임 원칙(Single Responsibility Principle)을 준수합니다합
- 부피가 큰 상태 조건을 제거하여 코드를 단순화할 수 있습니다.

단점
- 상태 시스템에 몇 가지 상태만 있거나 거의 변경되지 않는 경우, 패턴을 적용하는 것이 과도할 수 있습니다.


## Relations with Other Patterns
- Strategy 패턴과 State 패턴 모두 일부 작업을 별도 객체에 위임한다는 점에서 비슷합니다. Strategy 패턴은 별도 객체를 완전히 독립적으로 만들고 서로를 인식하지 못하게 합니다. State 패턴은 행동울 위임받은 객체들이 서로를 인식하며, 다른 객체로의 전이를 직접 다룹니다.

## Examples

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* [sample](examples/State/python/example.py)
