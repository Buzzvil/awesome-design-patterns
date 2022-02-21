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
- 

## 결론

## Solution

## Structure

### Pros

### Cons

## Examples