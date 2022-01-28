# Factory Method

## TL;DR
- 객체를 생성하는 인터페이스는 미리 정의하고, 어떤 클래스의 인스턴스를 만들지는 서브 클래스에서 정한다. (GoF Design Pattern)
- 팩토리메서드는 생성패턴의 한 종류로, 서브클래스에서 오브젝트를 생성할 수 있는 인터페이스를 제공하고, 서브클래스가 생성하는 오브젝트의 타입을 바꿀 수 있게 해준다. (refactoring.guru)

## Problem
- 다양한 종류의 문서를 표현하기 위한 Application과 Document이라는 인터페이스를 가지는 응용 프로그램 프레임워크가 있다.
- Application은 Document를 생성하고 수정하고 관리할 것이다.
- 이 프레임워크를 이용해서 그리기 관련 응용프로그램을 생성한다면, DrawApplication과 DrawingDocument를 생성하게 될 것이다.
- 이렇게 Document의 서브 클래스는 다양하게 만들어질 것이고, Application은 Document의 어떤 서브 클래스의 인스턴스를 만들어야 하는지 미리 알 수가 없다.
- Application은 **언제** 문서의 인스턴스를 만들어야 하는지만 알고 있을 뿐, **어떤** 종류의 문서를 생성해야 하는지는 알지 못한다.

## Solution
- Document의 어떤 서브 클래스를 생성하게 되는지를 Application의 서브 클래스에서 정한다.

## Structure
![image](https://www.planttext.com/api/plantuml/png/VL7D2eCm3BxtANBS3le0miGXx3QsLoWrJi6ragQCCNptPKEdLjWj-PBl9wJmh8d3lLEjPQHQ6uGhkIeOLifqsdiedJM4Z3yu0Y09IJwJ5a8beMP7y5809ssaV9wH6rVjze8SxQL7qjmwA_qGs_qZ3tE8QUqROcosqxHBy-qXrZ42jRU6mTKJESiMmSIx7wyyR5AWhU0Z4UkilRDinHD56GQo7Ym-uanBLLL8APzv0m00)
- Product: 생성하고자 하는 객체의 인터페이스.
- ConcreteProduct: Product의 구현체, 생성하려는 객체.
- Creator
  - Product타입을 반환하는 팩토리 메서드를 선언.
  - 팩토리 메서드는 abstract로 선언해도 되고, Product를 리턴하게 선언해도 됨.
  - 프로덕트에에 관한 코어 비즈니스 로직이 있어야 함.
- ConcreteCreator: 팩토리 메서드를 재정의해서 ConcreteProduct의 인스턴스를 반환.

## Pros & Cons
###  Pros
- SRP - 객체 생성 코드를 한 공간에서 관리할 수 있다.
- OCP - 기존 코드를 수정하지 않고 새로운 타입의 프로덕트 코드를 추가할 수 있다.
- creator와 concrete products 사이의 커플링을 피할 수 있다.

### Cons
- 계속해서 새로운 하위 클래스를 정의하게되어, 불필요하게 많은 클래스를 정의하게 되어 복잡해질 수 있다.

## Examples
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* [example-1](/patterns/factory-methodry-method/examples/python/example-1.py)
* [example-2](/patterns/factory-methodry-method/examples/python/example-2.py)
