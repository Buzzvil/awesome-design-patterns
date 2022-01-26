# Iterator 
## TL;DR
**Iterator** 는 List, Stack 과 같은 Collection 의 내제된 특징을 노출하지 않은 채로 각각 요소를 순회할 수 있는 behavioral design pattern 이다.


## Problem
요소의 모음인 Collection 은 개발 시에 가장 많이 만나는 자료구조이다. 

Collection 에는 간단한 List 구조도 있고 Stack, Tree, Graph 와 같은 복잡한 구조도 존재하지만, 구조와 상관없이 Collection 안의 요소를 중복없이 모두 순회할 수 있는 방법을 제공해야 한다. 

Collection 이 List 구조라면 이는 매우 쉬운 요구사항이지만, Tree 같은 복잡한 자료구조에서는 어려운 요구사항이 된다.

Collection 에 더 많은 순회 알고리즘을 추가하면 효율적인 데이터 저장이라는 근본적 목적이 상실될 수 있다. 또한 일부 순회 알고리즘은 특수한 상황에만 적용될 수 있어서 일반 Collection class 에 포함하는 것이 어울리지 않을 수 있다.

Collection 들이 제각각 서로다른 순회방법을 제공하면, 다양한 Collection 을 이용할 경우 Collection 마다 순회를 위한 추가 코드작업이 필요하다.

## Solution
Iterator pattern 의 기본 아이디어는 Collection의 순회 동작을 별도의 객체로 추출하는 것이다.

Iterator 객체는 현재 위치 및 끝까지 남은 요소 수와 같은 모든 탐색 세부 정보를 캡슐화한다. 이런 특성으로 인해 여러 Iterator들은 서로 독립적으로 동시에 동일한 Collection을 순회할 수 있다.

일반적으로 Iterator 는 Collection의 요소를 가져오기 위한 하나의 기본 메소드를 제공한다. 클라이언트는 반환이 없을 때까지 해당 메소드를 계속 실행할 수 있다. 반환이 없다면 Iterator 가 모든 요소를 순회했다는 것을 의미한다.

모든 Iterator 는 동일한 인터페이스를 제공해야 한다. 만약 순회를 위한 특별한 방법이 필요하다면, Collection 이나 클라이언트 코드를 변경하지 말고, 새로운 Iterator class 를 생성하는 방법을 사용한다.


## Pros & Cons
### Pros
* *단일 책임 원칙*: 순회 알고리즘을 독립된 클래스로 분리하여 Collection 과 클라이언트 코드를 간결하게 유지할 수 있다. 
* *Open/Closed 원칙*: 기존 코드의 추가변경 없이 새로운 유형의 Collection 과 Iterator 를 구현하여 적용할 수 있다.
* 각각 Iterator 객체마다 고유의 iteration 상태를 갖기 때문에, 같은 Collection 을 동시에 병렬로 순회가 가능하다.
* iteration 동작을 미룰 수도 있고 언제든지 필요할 때 재개할 수 있다.
### Cons
* 간단한 Collection 들만 사용할 경우 굳이 Iterator pattern 을 적용하는 것이 과한 작업일 수 있다.
* 특정 Collection의 경우 Iterator 순회 방식이 비효율적일 수 있다.

## Examples

![Scala](https://img.shields.io/badge/scala-%23DC322F.svg?style=for-the-badge&logo=scala&logoColor=white)
* [Basic Iterator trait](./examples/scala/src/main/scala/CustomIterator.scala), [Basic Iterator Spec](./examples/scala/src/test/scala/CustomIteratorSpec.scala)


## Reference
[Refactoring.guru](https://refactoring.guru/design-patterns/iterator)