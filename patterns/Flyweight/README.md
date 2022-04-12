# Observer

## TL;DR

- Flyweight는 각 개체의 모든 데이터를 유지하는 대신 여러 개체 간에 공통 상태 부분을 공유하여 메모리 사용량을 최소화합니다.

## Problem

![](https://refactoring.guru/images/patterns/diagrams/flyweight/problem-en-2x.png?id=0728488af118d8ee99c8c58878749f2a)

- 전투기를 조종하여 적을 물리치는 2D 비디오 게임을 개발하였습니다. 플레이어는 전투기를 조종하며, 수없이 쏟아지는 적 전투기와 싸우며 많은 양의 총알과 미사일을 피해야 합니다.
- 개발을 완료하여 직접 게임을 즐기려고 하는데, 오랫동안 게임을 실행하면 오류가 발생하였습니다. 로그를 분석해보니, 문제는 RAM이 충분하지 않았던 것으로 밝혀졌습니다.
- 알고보니 총알, 미사일, 적 전투기 등 많은 데이터가 포함되어 있으며 화면에 동시다발적으로 일어나는 객체들이 메모리를 많이 사용하고 있었습니다. 화면에 나타나는 총알, 미사일, 적 전투기 갯수만큼 새로운 객체를 할당해주고 있었기 때문입니다.

## Solution
- 내적 상태(Intrinsic State)와 외적 상태(Extrinsic State)를 구분합니다. 예를 들면, 미사일의 모습이나 색깔은 게임을 진행하는 동안 변하지 않고 컨텍스트에서 독립적인 내적 상태입니다. 하지만 미사일의 위치나 속도는 게임을 진행하는 동안 변하고 컨텍스트에 종속적인 외적 상태입니다.
- 객체 내부에 외적 상태를 저장하지 않도록 합니다. 대신, 이 상태에 의존하는 특정 메서드에 이 상태를 전달하도록 합니다.
- 내적 상태는 객체 내에서 변하지 않고 유지되는 값이므로 다른 컨텍스트에서 재사용할 수 있습니다.


## Structure
![image](https://refactoring.guru/images/patterns/diagrams/flyweight/solution3-en-2x.png?id=a8679f0aa03f6521dd206fcbc5ed9176)


## Pros & Cons
장점
- 프로그램에 유사한 요소가 많이 있다고 가정하면 많은 RAM을 절약할 수 있습니다.

단점
- 누군가 flyweight 메서드를 호출할 때마다 컨텍스트 데이터 중 일부를 다시 계산해야 하는 경우 CPU 리소스가 소모될 수 있습니다.
- 코드가 훨씬 더 복잡해집니다. 새로운 팀원들은 항상 엔티티의 상태가 왜 그런 식으로 분리되었는지 궁금해 할 것입니다.



## Examples

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)