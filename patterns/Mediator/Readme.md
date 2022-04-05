# Observer

## TL;DR

- Mediator Pattern은 클래스 간의 복잡한 상호작용을 캡슐화하여 하나의 클래스에 위임합니다. 그래서 객체 간의 직접적인 상호작용을 제한하고, Mediator 객체를 통해서만 상호작용하도록 합니다.

## Problem

![image](https://refactoring.guru/images/patterns/diagrams/mediator/problem1-en-2x.png)

- 고객 프로필을 만들고 편집하기 위한 대화 상자가 있다고 가정해보겠습니다. 텍스트 필드, 확인란, 버튼 등과 같은 다양한 양식으로 구성됩니다.

- 일부 양식은 다른 요소와 상호작용할 수 있습니다. 예를 들면, "개를 키우고 있습니다"라는 확인란을 선택하면 개의 이름을 입력하는 숨겨진 텍스트 필드가 나타날 수 있습니다.

- 이런 상호작용을 각 객체에 직접 구현하면 다른 객체에서 재사용하기가 어려워집니다. 그리고 객체 간 의존성이 늘어나며 결합도가 증가하고 유지보수가 어려워집니다.


## Solution
![image](https://refactoring.guru/images/patterns/diagrams/mediator/solution1-en-2x.png)

- 위의 예제에서, Dialog 객체가 모든 상호작용을 담당하도록 해봅시다. Dialog 객체는 모든 하위 요소를 알고 있으므로 새로운 종속성을 도입할 필요가 없습니다.

- 제출 버튼을 살펴봅시다. 이전에는 사용자가 버튼을 클릭할 떄마다 모든 개별 요소의 값을 검증해야 했습니다. 하지만 이제는 클릭이 발생했다고 Dialog 객체에 알리기만 하면 됩니다. Dialog 객체는 유효성 검사를 수행하거나 개별 요소에 작업을 전달합니다. 따라서 제출 버튼은 다른 요소들에 묶이지 않고 Dialog에만 종속됩니다.

- 이런 식으로, Mediator 패턴을 사용하면 단일 중재자 객체 내부의 다양한 객체 간의 관계를 캡슐화할 수 있습니다. 클래스의 종속성이 적을수록 해당 클래스를 수정, 확장 또는 재사용하기가 더 쉬워집니다.



## Structure
![image](https://refactoring.guru/images/patterns/diagrams/mediator/structure-2x.png)


## Pros & Cons
장점
- 다양한 구성 요소 간의 상호작용을 한 곳으로 추출하여 이해하기 쉬워지고 유지보수하기 쉬워집니다. (Single Responsibility Principle)
- 실제 구성 요소를 변경하지 않고도 새로운 중재자를 도입할 수 있습니다. (Open/Close Principle)
- 프로그램의 다양한 구성 요소 간의 결합을 줄일 수 있습니다.
- 개별 구성 요소를 더 쉽게 재사용할 수 있습니다.


단점
- 시간이 지남에 따라 Mediator는 God Object로 진화할 수 있습니다. 즉, 너무 많은 맥락을 알고 너무 많은 기능을 하는 객체가 될 수 있습니다.


## 다른 패턴과의 관계
- Facade와 Mediator는 비슷한 역할을 합니다. 밀접하게 연결된 많은 클래스 간의 협업을 구성하려고 합니다.
  - Facade에서, 하위 구성 요소들은 Facade 객체를 인식하지 못합니다. 그리고 하위 구성 요소들은 직접 통신할 수 있습니다.
  - Mediator에서, 하위 구성 요소들은 Mediator 객체만 인지하고 있습니다. 그리고 서로 직접 통신하지 않습니다.

- Observer와 Mediator는 경쟁 패턴입니다. 때로는 두 가지를 동시에 적용할 수도 있습니다.
  - observer는 "observer"와 "subject" 객체를 도입하여 통신을 다루지만, Mediator 객체는 다른 객체 간의 통신을 캡슐화합니다.
  - observer 패턴은 observer 간 조정이 필요하지 않을 때 잘 작동합니다.

## Examples

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* [sample](examples/python/test_sample.py)