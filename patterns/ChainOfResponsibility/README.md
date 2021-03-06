# Chain of Responsibility pattern

## TL;DR
Chain of Responsibility 는 핸들러 체인을 따라 요청을 전달할 수 있는 행동 디자인 패턴이다. 요청을 받으면 각 핸들러는 요청을 처리할지 다음 핸들러에게 요청을 넘길지 결정한다.

## Problem
온라인 주문 시스템에서 일하는 중이라고 가정 해 보자. 오직 인증된 유저만 주문할 수 있도록 시스템 접근권한을 제한하려 한다. 또한, 관리 권한을 가진 유저는 모든 주문에 대한 접근 권한이 있어야 한다.

어플리케이션 설계 중, 이러한 검사는 순차적으로 수행해야 한다는 것을 알게 되었다. 어플리케이션은 유저의 자격증명이 포함된 요청을 수신할 때 마다 유저 인증을 시도할 수 있다. 그러나 자격 증명이 올바르지 않거나 인증에 실패한다면, 다른 검사를 진행할 필요가 없다.

``` mermaid
graph LR
    A(Request) --> B((Authentication + Authorization))
    B -->|Yes| C(Ordering System)
    B -->|No| D(X)
```

주문 시스템에서 요청을 처리하기 전에 검증/인증 과정을 반드시 통과해야 한다.


그 후 몇달간 여러 순차적 체크를 더 구현했다.
- 원형 데이터를 주문 시스템에 직접 전달하는 것은 안전하지 않다는 의견이 있다. 그로 인해 요청에 실린 데이터를 삭제하기 위한 검증 단계를 추구하였다.
- 나중에 누군가는 시스템이 무차별 암호 해독에 취약하다는 사실을 알아냈다. 이를 막기 위해 동일한 IP 주소에서 오는 반복적인 실패 요청을 필터링하는 검사를 즉시 추가했다.
- 같은 데이터를 가진 반복 요청은 임시저장된 결과를 반환함으로 인해 시스템의 속도를 향상시킬 수 있다고 제안했다. 그 결과 적절한 임시 저장 결과가 없는 경우에만 요청이 시스템으로 전달되도록 하는 또 다른 검사를 추가했다.

``` mermaid
graph LR;
    A(Request) --> B((Authentication + Authorization + Validation + Caching + ...))
    B -->|Yes| C(Ordering System)
    B -->|No| D(X)
```

이미 뒤죽박죽 꼬인 검사 코드는 새로운 기능을 추가할 때 마다 점점 더 부풀려졌다. 하나의 검사를 변경하면 때때로 다른 검사에 영향을 준다. 최악의 경우 시스템의 다른 구성 요소를 보호하기 위해 검사를 재사용하려고 할 때, 해당 코드 일부가 필요하지만 전부는 아니기 때문에 코드를 일부만 복제해야 했다.  

시스템은 이해하기 매우 어렵고 유지관리 비용이 비싸게 되었다. 전체 코드를 리팩토링하기로 결정할 때까지 당신은 한동안 코드와 씨름하게 되었다.

## Solution
다른 많은 행동 디자인 패턴과 마찬가지로, **Chain of Responsibility** 는 특정 행동을 *핸들러*라고 하는 독립 실행형 개체로 변환하고 이에 의존한다. 위 문제의 경우 각 검사는 검사를 수행하는 자체 클래스의 단일 메소드로 추출되어야 한다. 요청은 데이터와 함께 해당 메소드에 인수로 전달된다.

패턴은 이러한 핸들러들을 체인으로 연결하도록 제안한다. 연결된 각 핸들러에는 체인의 다음 핸들러에 대한 참조를 저장하기 위한 필드가 있다. 요청을 처리하는 것 외에도 핸들러는 체인을 따라 요청을 더 전달한다. 요청은 모든 핸들러가 처리할 기회를 가질 때까지 체인을 따라 이동한다.

**핸들러는 요청을 더 이상 체인 아래로 전달하지 않고 추가 처리를 효과적으로 중지할 수 있다.**

위 예제의 주문시스템에서 핸들러는 처리를 수행한 다음 요청을 체인 아래로 더 전달할지 여부를 결정한다. 요청에 올바른 데이터가 포함되어있다면 모든 핸들러는, 인증이든 검증이든, 본연의 동작을 실행할 수 있다.

그러나 요청을 수신하면 핸들러가 처리할 수 있는지 여부를 결정하는 약간 다른 접근방식이 있다. 가능한 경우에는 더 이상 요청을 전달하지 않는다. 따라서 요청을 처리하는 핸들러는 오직 하나 혹은 없게 된다. 이 접근 방식은 GUI 내에서 요소 스택의 이벤트를 처리할 때 매우 일반적이다.

예를 들어, 사용자가 버튼을 클릭하면 이벤트는 버튼에서 메인 애플리케이션 창까지 해당 컨테이너를 따라 이동하는 GUI 요소 체인을 통해 전파된다. 이벤트는 처리할 수 있는 체인의 첫 번째 요소에 의해 처리된다. 이 예는 또한 체인이 항상 개체 트리에서 추출될 수 있음을 보여주기 때문에 주목할 만 하다.

모든 핸들러 클래스가 동일한 인터페이스를 구현하는 것은 중요하다. 각 핸들러는 `execute` 메소드가 있는 다음 핸들러에 대해서만 신경을 써야 한다. 이렇게 하면 코드를 클래스에 연결하지 않고도 다양한 핸들러를 사용하여 런타임에 체인을 구성할 수 있다.

## Structure
1. **핸들러**는 모든 concrete 핸들러에 공통 인터페이스를 선언한다. 일반적으로 요청을 처리하기 위한 단일 메서드만 포함하지만, 때로는 체인에서 다음 핸들러를 설정하기 위한 또다른 메서드가 존재할 수 있다.
2. **기본 핸들러**는 모든 핸들러 클래스에 boilerplate 코드를 추가할 수 있는 선택적 클래스이다.
    
    일반적으로 기본 클래스는 다음 핸들러에 대한 참조를 저장하기 위한 필드를 정의한다. 클라이언트는 핸들러를 이전 핸들러의 생성자 혹은 setter 에게 전달하여 채인을 구축할 수 있다. 존재 여부를 확인한 후 다음 핸들러로 실행을 전달하는 것과 같은 기본 처리 동작을 기본 핸들러가 구현할 수도 있다.
3. Concrete 핸들러에는 요청을 처리하기 위한 실제 코드가 포함되어 있다. 요청을 수신하면 각 핸들러는 요청을 처리할지 여부와 함께 체인을 따라 요청을 전달할지 여부를 결정해야 한다.
   
   핸들러는 일반적으로 변화불가하고, 독립적이고, 생성자를 통해 필요한 모든 데이터를 한 번만 받아들인다.
4. 클라이언트는 응용 프로그램의 의사에 따라 체인을 한 번만 구성하거나 동적으로 구성할 수 있다. 요청은 체인의 모든 핸들러로 보낼 수 있지만, 첫번째 핸들러일 필요는 없다.

### Pros 
✅ 요청 처리 순서를 제어할 수 있다.

✅ *Single Responsibility Principle*. 작업을 수행하는 클래스에서 작업을 호출하는 클래스를 분리할 수 있다.

✅ *Open/Closed Principle*. 기존 클라이언트 코드 변화 없이 새 핸들러를 도입할 수 있다.


## Reference

[Refactoring.guru](https://refactoring.guru/design-patterns/chain-of-responsibility)