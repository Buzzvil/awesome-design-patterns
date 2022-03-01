# Chain of Responsibility pattern

## TL;DR
Chain of Responsibility 는 핸들러 체인을 따라 요청을 전달할 수 있는 행동 디자인 패턴이다. 요청을 받으면 각 핸들러는 요청을 처리할지 다음 핸들러에게 요청을 넘길지 결정한다.

## Problem
온라인 주문 시스템에서 일하는 중이라고 가정 해 보자. 오직 인증된 유저만 주문할 수 있도록 시스템 접근권한을 제한하려 한다. 또한, 관리 권한을 가진 유저는 모든 주문에 대한 접근 권한이 있어야 한다.

어플리케이션 설계 중, 이러한 검사는 순차적으로 수행해야 한다는 것을 알게 되었다. 어플리케이션은 유저의 자격증명이 포함된 요청을 수신할 때 마다 유저 인증을 시도할 수 있다. 그러나 자격 증명이 올바르지 않거나 인증에 실패한다면, 다른 검사를 진행할 필요가 없다.

[![](https://mermaid.ink/img/pako:eNpNzzsOwjAMANCrWJ5aQS_QAYnfhkCCCTUMpjEQQRJInaFQ7k7KR8KTbT3L9gNrrxlLPAa6nmCxVg5SjKs13yI3soOiGMEky8ZRTuzE1CTGOxhA3_DB3N91nn_mJj3vttx0MK1WQXMw7gibthG2u3-y9B3MsgOVByr25HIcouVgyeh0y6OXCtNCywrLlGoKZ4XKPZOLV03Cc23EB0zzl4aHSFH8pnU1lhIi_9DMUPrLftXzBUqHTdE)](https://mermaid.live/edit#pako:eNpNzzsOwjAMANCrWJ5aQS_QAYnfhkCCCTUMpjEQQRJInaFQ7k7KR8KTbT3L9gNrrxlLPAa6nmCxVg5SjKs13yI3soOiGMEky8ZRTuzE1CTGOxhA3_DB3N91nn_mJj3vttx0MK1WQXMw7gibthG2u3-y9B3MsgOVByr25HIcouVgyeh0y6OXCtNCywrLlGoKZ4XKPZOLV03Cc23EB0zzl4aHSFH8pnU1lhIi_9DMUPrLftXzBUqHTdE)

<details><summary>주문 시스템에서 요청을 처리하기 전에 검증/인증 과정을 반드시 통과해야 한다.</summary>
<p>

``` Mermaid
graph LR;
    A[Request] --> B((Authentication + Authorization))
    B -->|Yes| C[Ordering System]
    B -->|No| D(fa:fa-ban)
```

</p></details>

그 후 몇달간 여러 순차적 체크를 더 구현했다.
- 원형 데이터를 주문 시스템에 직접 전달하는 것은 안전하지 않다는 의견이 있다. 그로 인해 요청에 실린 데이터를 삭제하기 위한 검증 단계를 추구하였다.
- 나중에 누군가는 시스템이 무차별 암호 해독에 취약하다는 사실을 알아냈다. 이를 막기 위해 동일한 IP 주소에서 오는 반복적인 실패 요청을 필터링하는 검사를 즉시 추가했다.
- 같은 데이터를 가진 반복 요청은 임시저장된 결과를 반환함으로 인해 시스템의 속도를 향상시킬 수 있다고 제안했다. 그 결과 적절한 임시 저장 결과가 없는 경우에만 요청이 시스템으로 전달되도록 하는 또 다른 검사를 추가했다.

이미 뒤죽박죽 꼬인 검사 코드는 새로운 기능을 추가할 때 마다 점점 더 부풀려졌다. 하나의 검사를 변경하면 때때로 다른 검사에 영향을 준다. 최악의 경우 시스템의 다른 구성 요소를 보호하기 위해 검사를 재사용하려고 할 때, 해당 코드 일부가 필요하지만 전부는 아니기 때문에 코드를 일부만 복제해야 했다.  

시스템은 이해하기 매우 어렵고 유지관리 비용이 비싸게 되었다. 전체 코드를 리팩토링하기로 결정할 때까지 당신은 한동안 코드와 씨름하게 되었다.

## Solution


## Structure

### Pros

### Cons

## Examples