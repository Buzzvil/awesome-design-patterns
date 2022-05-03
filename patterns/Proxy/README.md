# Proxy pattern

## TL;DR

실제 서비스(객체, 서버, 데이터베이스 등)을 대리(proxy)하여 로직의 흐름을 제어하는 패턴
실제 서비스를 변경하지 않고도 접근 제어, 캐싱, 스텁 등의 역할을 수행함

## Problem & Solution

프록시 패턴은 어떤 기능을 대신할 것인지에 따라 다양한 기능을 수행할 수 있다.

- 가상(virtual) 프록시: 지연 초기화
    - 프록시 객체가 최소한의 정보만 들고 있다가 진짜로 필요해질 때 실제 서비스에서 로딩
- 보호(protection) 프록시: 엑세스 제어
    - 실제 서비스에 접근하기 위해 인증 절차 등을 추가로 수행
- 원격(remote) 프록시: 원격 서비스의 로컬 실행
    - 네트워크 요청이나 마샬링 등의 추가 작업을 프록시 객체가 수행
- 로깅(logging) 프록시
    - 로그 기록
- 캐싱(caching) 프록시
    - 요청 결과를 캐싱하고 캐시의 수명 주기 관리
- 스마트 포인터(smart reference)도 일종의 프록시 패턴
    - 메모리 관리, 경계 검사 같은 추가 기능을 제공하면서 포인터를 시뮬레이션 하는 추상 데이터 유형

## Structure

![proxy pattern](https://refactoring.guru/images/patterns/diagrams/proxy/structure-2x.png)
(이미지 출처: https://refactoring.guru/design-patterns/proxy)

## Pseudocode

```kotlin
interface PizzaHouse {
    fun getPizza(): Pizza
}

class RealPizzaHouse : PizzaHouse {
    override fun getPizza(): Pizza {
        return makePizza()
    }

    private fun makePizza(): Pizza {
        // 매우 복잡한 피자 만드는 과정
        //   도우를 직접 반죽해서 발효하기
        //   신선한 토핑과 치즈 구매하기
        //   ...
        //   피자 화덕에서 노릇하게 굽기
        return deliciousPizza
    }
}

class ProxyPizzaHouse : PizzaHouse {
    // 냉동 피자 == 캐싱
    private var frozenPizza: Pizza? = null

    override fun getPizza() {
        if (frozenPizza == null) {
            frozenPizza = RealPizzaHouse.getPizza()
        }

        return frozenPizza
    }
}
```

## Pros & Cons

### 장점

- 클라이언트 입장에서 실제 객체와 프록시 객체를 구분할 필요가 없음(동일한 인터페이스)
  - 클라이언트가 알지 못하는 상태에서 실제 객체를 제어 및 관리(수명 주기 등)
  - 실제 객체가 없어도 작동할 수 있음
  - 실제 객체를 변경하지 않고도 새로운 프록시를 도입하여 기능을 추가/변경할 수 있음

### 단점

- 코드가 복잡해짐
- 어떤건 프록시 객체를 통해 접근하고, 어떤건 실제 객체에 직접 접근하는 경우 동작이 달라질 여지가 있음
- 실제 응답이 늦어질 수 있음

## 다른 패턴과의 관계

- Adapter, Decorator <> Proxy
    - Adapter는 객체를 래핑하여 '다른' 인터페이스를 제공
    - Decorator는 '향상된' 인터페이스를 제공
    - Proxy는 '동일한' 인터페이스 제공
- Facade <> Proxy
    - 자체적으로 복잡한 기능을 대신 수행한다는 점에서 유사함
    - but 프록시 패턴은 실제 객체/서비스와 인터페이스가 동일하기 때문에 '대체해서' 사용 가능
- Decorator <> Proxy
    - 작업을 위임한다는 점에서 유사함
    - Proxy는 자체적으로 실제 객체/서비스의 수명 주기 등을 관리
    - Decorator는 클라이언트에 의해 제어됨
- Flyweight, Singleton <> Proxy
    - 프록시를 여러개 만드는 것이 부담되는 경우, 플라이웨이트/싱글톤 패턴과 결합하여 프록시 객체의 인스턴스를 공유

## Examples

- [가상(virtual) 프록시 예제](./VirtualProxyExample.kt)
- [보호(protection) 프록시 예제](./ProtectionProxyExample.kt)
- [원격(remote) 프록시 예제](./RemoteProxyExample.kt)
