# Bridge pattern

## TL;DR

> 구현부에서 추상층을 분리하여 각자 독립적으로 변형할 수 있게 하는 패턴 어쩌구
> — *위키피디아*

상속대신 컴포지션을 사용하자 그런데 이제 추상화를 곁들인

## Problem

![](https://refactoring.guru/images/patterns/diagrams/bridge/problem-en-2x.png)

상속의 문제점: 경우의 수가 기하급수적으로 많아진다. 이로 인해 유지보수가 힘들어짐

예를 들면, 위 그림에서 색깔(노란색 등), 모양(삼각형 등)이 하나만 추가되어도 구현해야 하는 클래스가 너무 많아짐

## Solution

![](https://refactoring.guru/images/patterns/diagrams/bridge/solution-en-2x.png)

컴포지션으로 해결!

위 그림에서 빨간색 contains 부분 때문에 Bridge 패턴이라고 부른다.

![](https://refactoring.guru/images/patterns/content/bridge/bridge-2-en-2x.png?id=bbd64c96e6711636356944b3564ad67e)

UI와 로직을 분리하는 것도 일종의 브릿지 패턴이다. ~~우린 이걸 아키텍처라고 부르기로 했어요~~

## Structure

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Bridge_UML_class_diagram.svg/1920px-Bridge_UML_class_diagram.svg.png" style="background-color:white;" />

- Abstraction: 높은 수준의 추상화 클래스. 클라이언트는 이것만 참조하면 된다. 주입받은 구현체(Implementor)를 사용해서 원하는 동작을 제공한다. UseCase와 비슷한 느낌
- Implementor: 구현체. 인터페이스(Implementor)와 실제 구현체(ConcreteImplementor)로 나뉨
  - ConcreteImplementor는 여러개일 수 있다
  - Abstraction에 어떤 Implementor를 넣을지는 클라이언트의 역할
- RefinedAbstraction: 세련된 추상화라는 이름이 잘 와닿진 않는데, 그냥 Abstraction를 확장하는 자식 클래스임. 리팩토링 구루에서는 optional이라고 표기해놓음

(참고용) 리팩토링 구루에서 가져온 다이어그램

![](https://refactoring.guru/images/patterns/diagrams/bridge/structure-en-indexed-2x.png?id=99713473c8ba3c08ce6a3540f1453ebc)

![](https://refactoring.guru/images/patterns/diagrams/bridge/example-en-2x.png?id=9b24f3116b5b55a462841da41b11d32f)

## Pseudocode

refactoring guru의 예제를 Kotlin으로 작성

```kotlin
interface Device {
    fun isEnabled(): Boolean
    fun enable()
    fun disable()
    fun getVolume(): Int
    fun setVolume(percent: Int)
    fun getChannel(): Int
    fun setChannel(channel: Int)
}

class Tv : Device {
    // ...
}

class Radio : Device {
    // ...
}
```

```kotlin
open class RemoteControl(
    private val device: Device
) {
    fun togglePower() {
        if (device.isEnabled()) {
            device.disable()
        } else {
            device.enable()
        }
    }

    fun volumeDown() {
        device.setVolume(device.getVolume() - 10)
    }

    fun volumeUp() {
        device.setVolume(device.getVolume() + 10)
    }

    fun channelDown() {
        device.setChannel(device.getChannel() - 1)
    }

    fun channelUp() {
        device.setChannel(device.getChannel() + 1)
    }
}

class AdvancedRemoteControl(
    private val device: Device
) : RemoteControl(device) {
    fun mute() {
        device.setVolume(0)
    }
}
```

```kotlin
// client code
val tv = Tv()
val remote = RemoteControl(tv)
remote.togglePower()

val radio = Radio()
val advancedRemote = AdvancedRemoteControl(radio)
advancedRemote.mute()
```

## Pros & Cons

### 장점

- 컴포지션 + 추상화의 장점과 같음
- 개방 폐쇄 원칙: 추상화와 구현이 독립적
- 단일 책임 원칙: 특정 기능이 별도의 클래스로 분리됨

### 단점

- 결합도가 높은 클래스에 적용하려면 빡세다 정도?
- 패턴 자체가 가지고 있는 단점이라기 보단 컴포지션이 가지고 있는 단점들

## 다른 패턴과 비교

### 전략(Stragegy) 패턴

- 전략 패턴과 브릿지 패턴은 매우 유사한 코드 구조를 가짐 but 목적이 다름
- 전략 패턴은 런타임에 원하는 클래스를 선택할 수 있도록 하는 것
- 브릿지 패턴은 추상화와 컴포지션으로 결합도를 낮추는 구조를 갖는 것 -> 결과적으로 전략 패턴에서 하고 싶은 일(런타임에 클래스 교체 등)도 가능해짐

## 개인적인 생각

브릿지 패턴은 그냥 자연스럽게 컴포지션을 사용하다 보면 나오게 되는 패턴인 것 같다.

상속보다는 컴포지션을 사용하는 추세가 오래되었고, 이젠 브릿지 패턴이 너무 당연해져서 패턴이라고 하지도 않는 듯... 실제로 이런 구조를 논의하면 '브릿지 패턴을 사용하죠' 보다는 '이건 따로 클래스를 빼서 주입하죠' 라는 식으로 말할 것 같다.

## Examples

패턴 자체가 단순해서 수도 코드로 대체...

## 출처

- 대부분의 이미지 출처: https://refactoring.guru/design-patterns/bridge
- 다이어그램 출처: https://ko.wikipedia.org/wiki/%EB%B8%8C%EB%A6%AC%EC%A7%80_%ED%8C%A8%ED%84%B4
