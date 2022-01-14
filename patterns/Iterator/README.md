# Iterator 
**Iterator** 는 List, Stack 과 같은 Collection 의 내제된 특징을 노출하지 않은 채로 각각 요소를 순회할 수 있는 Design Pattern 이다.


## Problem
element의 모음인 collection 은 개발 시에 가장 많이 만나는 자료구조이다. 

Collection 은 여러 형태가 있다. 간단한 list 구조도 있고 stacks, trees, graphs 와 같은 복잡한 구조도 존재한다.

그러나 collection 이 어떤 구조로 이루어지더라도 collection 안의 element를 중복없이 모두 순회할 수 있는 방법을 제공해야 한다. 

collection 이 list 구조라면 이는 매우 쉬운 요구사항이지만, tree 같은 복잡한 자료구조에서는 어려운 요구사항이 된다.

Collection 에 더 많은 순회 알고리즘을 추가하면 효율적인 데이터 저장이라는 근본적 목적이 상실될 수 있다. 또한 일부 순회 알고리즘은 특수한 상황에만 적용될 수 있어서 일반 collection class 에 포함하는 것이 어울리지 않을 수 있다.

collection 들이 각각의 방법으로 순회방법을 제공하면, 다양한 collection 을 이용할 경우 collection 마다 순회할 수 있는 추가 코드작업이 필요하다.

## Solution
Iterator pattern 의 기본 아이디어는 collection의 순회 동작을 별도의 객체로 추출하는 것이다.

Iterator 객체는 현재 위치 및 끝까지 남은 element 수와 같은 모든 탐색 세부 정보를 캡슐화한다. 이런 특성으로 인해 여러 iterator들은 서로 독립적으로 동시에 동일한 collection을 순회할 수 있다.

일반적으로 iterator 는 collection의 elemenㅇ를 가져오기 위한 하나의 기본 메소드를 제공한다. 클라이언트는 반환이 없을 때까지 해당 메소드를 계속 실행할 수 있다. 반환이 없다면 iterator 가 모든 element를 순회했다는 것을 의미한다.

모든 iterator 는 동일한 인터페이스를 제공해야 한다. 만약 순회를 위한 특별한 방법이 필요하다면, collection 이나 클라이언트 코드를 변경하지 말고, 새로운 iterator class 를 생성하는 방법을 사용한다.

## Structure

...

## Pseudocode

...

## Pros & Cons
### Pros
* *단일 책임 원칙*: 순회 알고리즘을 독립된 클래스로 분리하여 collection 과 client 코드를 간결하게 유지할 수 있다. 
* *Open/Closed 원칙*: 기존 코드의 추가변경 없이 새로운 유형의 collection 과 iterator 를 구현하여 적용할 수 있다.
* 각각 iterator 객체마다 고유의 iteration 상태를 갖기 때문에, 같은 collection 을 동시에 병렬로 순회가 가능하다.
* iteration 동작을 미룰 수도 있고 언제든지 필요할 때 재개할 수 있다.
### Cons
* 간단한 collection 들만 사용할 경우 굳이 iterator pattern 을 적용하는 것이 과할 수 있다.
* 특정 collection의 경우 iterator 순회 방식이 비효율적일 수 있다.

## Examples

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* [Basic Iterator example](./examples/python/sample-iterator.py)
* [Looping through an Iterator example](./examples/python/looping_through_an_iterator.py)

![Scala](https://img.shields.io/badge/scala-%23DC322F.svg?style=for-the-badge&logo=scala&logoColor=white)
* [Basic Iterator example](./examples/scala/simple.scala)


## Reference
[Refactoring.guru](https://refactoring.guru/design-patterns/iterator)