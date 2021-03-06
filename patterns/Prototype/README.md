# Prototype

## TL;DR

- 다른 클래스에 의존하지 않으면서 그 클래스 인스턴스의 복제본을 만들 수 있다.

## Problem

- 어떤 객체의 복제본을 만들고 싶을 때, 사용하는 쪽에서 직접 복제본을 만들기 어려울 수 있다.
    - 비공개 변수에 접근을 허용하지 않는 언어라면, 객체에 공개되지 않은 변수가 있는 경우 사용하는 쪽에서 동일하게 복제하기 어렵다.
    - 객체의 내부 구조가 복잡해서 다른 객체를 참조하거나 기타 연산이 필요하다면 사용하는 측에서 관련된 작업을 해야한다.
    사용하는 측이 복제라는 하나의 연산을 하기 위해서 불필요한 다른 연산을 해야한다.
    - 예시 1: 건축 설계도를 그리는 CAD 소프트웨어를 만드는 상황을 가정
        - 소프트웨어의 주 기능 중 하나를 사용자가 저장한 도형을 설계도에 생성하는 것이라고 하자.
        사용자가 저장한 도형은 소프트웨어에서 제공한 도형을 사용한 것인데, 도형 간에 포함관계를 생성할 수 있어서 구조가 복잡할 수 있다.
        이 도형을 그대로 복제해서 생성하는 전략을 택하고싶은데 외부에서 복제하려면 도형을 정의한 클래스를 참조하여 내부 값을 참조하고 새로 생성해야 한다.
- 객체를 생성하고 사용하는 클래스를 구현하고 싶을 때, 사용하는 클래스가 객체의 구조에 의존하게 될 수 있다.
  - 예시 2: 예시 1과 동일한 상황 가정
    - 항상 같은 도형이 사용되고, 주로 사용될 도형과 이를 생성하고 사용하는 부분을 나눠서 구현한다고 가정하자.
    도형은 추상 클래스(Shape)를 구체 클래스(ConcreteShape)가 상속하는 형태로 되어있다.
    - 생성 및 사용하는 부분(Client)에서는 항상 같은 도형이 사용되므로 기존에 생성해둔 도형을 복제해서 사용하려고 한다.
    지금은 Shape에서 복제에 관한 인터페이스를 제공하지 않으므로 Client를 상속한 ConcreteClient가 구체 클래스를 참조해서 새로 생성해야 한다.
    한 ConreteClient가 한 ConcreteShape를 담당하도록 참조를 분리하다보니 Client의 구조가 Shape에 의존하게 되었다.
    ```mermaid
    classDiagram
  
    class Shape
    <<abstract>> Shape
    class ConcreteShapeA
    class ConcreteShapeB
    ConcreteShapeA --|> Shape
    ConcreteShapeB --|> Shape
    
    class Client {
        +void someWork()
    }
    <<abstract>> Client
    class ConcreteClientA
    class ConcreteClientB
    ConcreteClientA ..> ConcreteShapeA
    ConcreteClientB ..> ConcreteShapeB
    ConcreteClientA --|> Client
    ConcreteClientB --|> Client
    ```

## Solution

- 복제 대상이 되는 클래스에서 복제 기능을 제공한다.
    - 객체는 내부 값을 알고있으므로 외부에서 복제를 시도하는 것 보다 내부에서 시도하는 것이 더 쉽다.
- 구체(concrete) 클래스의 인스턴스를 미리 생성해두고 이 인스턴스의 복제를 계속 가져다 사용하는 방식으로 구현한다.
    - 사용하는 클래스가 객체의 구조에 의존하게 되어 문제가 되었던 경우, 사용하는 클래스에 복제를 전달하는 방식으로 해결할 수 있다.
    ```mermaid
    classDiagram
  
    class Shape {
        +Shape clone()
    }
    <<abstract>> Shape
    class ConcreteShapeA
    class ConcreteShapeB
    ConcreteShapeA --|> Shape
    ConcreteShapeB --|> Shape
    
    class Client {
        +void someWork(Shape shape)
    }
    Client ..> Shape
    ```

### Implementation

- 복제할 대상이 하나가 아니라 여럿인 경우 여러 prototype들을 관리할 registry를 들고있는 클래스(PrototypeManager)를 정의해 사용할 수 있다.
여기서 PrototypeManager는 특정 key로 prototype을 가져오고, 설정하고, 지우는 operation을 제공하는 역할을 하는 것으로 볼 수 있다.
- Client에서 prototype의 복제만으로 만족하지 못하는 경우 일부 값을 변경해야할 수도 있다.
이 때 어떤 값을 전달해야할지 통일되지 않은 경우 prototype을 복제할 때 일부 값을 전달하도록 구현하기 어려울 수 있다.
이 경우 prototype이 특정 값을 변경하는 operation을 제공해서 Client가 이를 복제한 직후에 사용하거나, Initialize operation을 제공해서 주어진 값으로 prototype의 내부 상태를 새로 지정하는 방법이 있을 수 있다.

## Structure

```mermaid
classDiagram

class Prototype {
    +Prototype clone()
}
<<abstract>> Prototype

class ConcretePrototype

ConcretePrototype --|> Prototype
```


## Pros & Cons

### Pros

- 구체 클래스에 의존하지 않고도 복제를 생성할 수 있다.
- 복잡한 객체의 복제를 쉽게 생성할 수 있다.
- 사용하는 측이 알아야하는 내용을 줄일 수 있다.

### Cons

- 순환 참조가 있는 복잡한 객체는 내부에서 복제하기 어려울 수 있다.


## Examples

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* [sample](examples/Prototype/python/basic_example.py)
