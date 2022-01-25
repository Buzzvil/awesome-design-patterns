# Observer

## TL;DR

- Observer pattern은 특정 객체(Subject)에 발생하는 모든 이벤트를 여러 객체(Observer)에 알리는 구독 메커니즘을 정의하는 디자인 패턴입니다.
- 객체 간 일대다 의존관계를 정의해 두어, 어떤 객체의 상태가 변할 때 그 객체에 의존성을 가진 다른 객체들이 그 변화를 통지받고 자동으로 갱신될 수 있게 만듭니다. 

## Problem

- Customer와 Store라는 두 유형의 객체가 있다고 합시다.
- Customer는 Store에 출시될 특정 브랜드의 제품(예를 들면, iPhone의 새 모델)에 관심이 있습니다.
- Customer는 매일 Store에 방문하여 제품이 출시되었는지 확인할 수 있습니다. 그러나 제품이 아직 출시되지 않았다면, Customer는 매번 헛걸음을 하게 됩니다.
- Store는 새 제품이 출시될 때마다 모든 고객에게 메일을 보낼 수 있습니다. 그러나, 그 제품에 관심이 없는 고객들은 필요없는 메일을 받게 될 것입니다.
- 결국 Customer는 제품 출시 여부를 확인하는 데 시간을 낭비하거나, Store는 적절하지 않은 고객에게 메일을 알리게 되어 리소스를 낭비합니다.

## Solution

- Store에서 제품이 출시될 때마다, 해당 제품 출시 정보를 구독한 Customer들에게 알림을 보냅니다.
- Customer들은 관심이 있는 제품 정보를 구독할 수 있도록 합니다.
- Customer들은 관심이 있는 제품이 출시되었다는 알림이 오면, 이에 따른 작업을 수행합니다.

## Structure
![image](https://www.planttext.com/api/plantuml/png/SoWkIImgAStDuShCAqajIajCJbK8BatAIaqkgUPIK4WiAKbCpj38JofEBIfBBT842gMaOWZbvPTafbLgQ7BLSYNd91ONApZdvoKNfPQaKc8IaeFyeIeKG0QL5gGabgHYiGocof4uPKxeohYuC4tIBTMrWrkF8U-4GnxgROWibCC54zJBqKFImkMGcfS237u0)


## Pros & Cons
장점
- Subject 코드를 변경하지 않고도 새로운 Observer 클래스를 만들거나, Observer 코드를 변경하지 않고도 새로운 Subject 클래스를 만들 수 있어서 개방 폐쇄 원칙(Open-Closed Principle)이 보장됩니다.
- Subject와 Observer의 관계를 런타임에서 다룰 수 있습니다.

단점
- Subject와 Observer 사이의 복잡성이 추가되어 코드가 복잡해질 수 있습니다.


## Examples

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* [sample](/Observer/examples/python)