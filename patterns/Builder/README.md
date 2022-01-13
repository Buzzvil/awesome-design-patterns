# Builder pattern

## TL;DR

개체를 생성하는 코드를 따로 분리하여 생성자를 복잡하게 만들지 않고 다양한 옵션으로 개체를 생성할 수 있도록 도와주는 패턴

## Problem

1. 생성할 때 가능한 옵션이 너무 많으면 생성자의 경우의 수가 너무 많아지는 경우가 있다.
예를 들어, 샌드위치를 만드는데 `샌드위치(빵, 고기, 소스)`, `샌드위치(빵, 치즈, 채소)`, `샌드위치(빵, 고기, 치즈, 채소, 소스)` 등 옵션이 많으면 모든 경우의 생성자를 만들기란 사실상 불가능에 가깝다.

물론 필요 없는 파라미터는 null을 넘겨주는 방식으로 생성자를 하나만 유지할 수도 있다. 하지만 필요없는 파라미터를 함께 신경써야 하기 때문에 타입, 순서에 대한 관리가 어려워진다. 이는 아래 문제와도 연관이 있다.

2. 생성자의 파라미터의 순서를 헷갈려서 잘못 넣는 경우 의도하지 않은 개체가 만들어 질 수 있다.
예를 들면 `사람(이름, 나이, 키)`를 받아야 하는데 `사람("Gildong", 175, 25)` 이런 식으로 175살에 25cm인 사람이 만들어질 수 있다.

## Solution

빌더 패턴에서는 개체 생성과 관련된 클래스를 별도로 분리하여, 개체를 생성하는 방법이 복잡한 경우(Optional한 속성이 많을 때)에도 동일한 방식으로 생성할 수 있도록 한다.

## Structure

![](https://imgur.com/g8AsAjc.jpg)

## Pseudocode

```java
// 출처: https://ko.wikipedia.org/wiki/%EB%B9%8C%EB%8D%94_%ED%8C%A8%ED%84%B4

/** "Product" */
class Pizza {
	private String dough = "";
	private String sauce = "";
	private String topping = "";

	public void setDough(String dough) {
		this.dough = dough;
	}

	public void setSauce(String sauce) {
		this.sauce = sauce;
	}

	public void setTopping(String topping) {
		this.topping = topping;
	}
}

/** "Abstract Builder" */
abstract class PizzaBuilder {
	protected Pizza pizza;

	public Pizza getPizza() {
		return pizza;
	}

	public void createNewPizzaProduct() {
		pizza = new Pizza();
	}

	public abstract void buildDough();

	public abstract void buildSauce();

	public abstract void buildTopping();
}

/** "ConcreteBuilder" */
class HawaiianPizzaBuilder extends PizzaBuilder {
	public void buildDough() {
		pizza.setDough("cross");
	}

	public void buildSauce() {
		pizza.setSauce("mild");
	}

	public void buildTopping() {
		pizza.setTopping("ham+pineapple");
	}
}

/** "ConcreteBuilder" */
class SpicyPizzaBuilder extends PizzaBuilder {
	public void buildDough() {
		pizza.setDough("pan baked");
	}

	public void buildSauce() {
		pizza.setSauce("hot");
	}

	public void buildTopping() {
		pizza.setTopping("pepperoni+salami");
	}
}

/** "Director" */
class Cook {
	private PizzaBuilder pizzaBuilder;

	public void setPizzaBuilder(PizzaBuilder pizzaBuilder) {
		this.pizzaBuilder = pizzaBuilder;
	}

	public Pizza getPizza() {
		return pizzaBuilder.getPizza();
	}

	public void constructPizza() {
		pizzaBuilder.createNewPizzaProduct();
		pizzaBuilder.buildDough();
		pizzaBuilder.buildSauce();
		pizzaBuilder.buildTopping();
	}
}

/** A given type of pizza being constructed. */
public class BuilderExample {
	public static void main(String[] args) {
		Cook cook = new Cook();
		PizzaBuilder hawaiianPizzaBuilder = new HawaiianPizzaBuilder();
		PizzaBuilder spicyPizzaBuilder = new SpicyPizzaBuilder();

		cook.setPizzaBuilder(hawaiianPizzaBuilder);
		cook.constructPizza();

		Pizza pizza = cook.getPizza();
	}
}
```

## Pros & Cons

### Pros

1. 필요한 데이터만 설정할 수 있음
2. 유연성을 확보할 수 있음
3. 가독성을 높일 수 있음
4. 불변성을 확보할 수 있음

출처: https://mangkyu.tistory.com/163 (각 항목에 대한 구체적인 예시가 있어서 참고하면 좋음)

### Cons

- 정적 분석 불가능
  - 의도치 않게 선택적 매개변수가 누락되는 경우 IDE의 도움을 받을 수 없음
  - (자바인 경우) 초기화가 누락된 멤버 변수의 기본값이 null이면 NPE 발생하기 좋음
- 더 많은 코드의 작성이 필요
  - 생성자의 파라미터가 2-3개 정도로 작은 규모인 경우 굳이 빌더 패턴을 사용하지 말고 그냥 생성자를 2~3개 만들자
- DTO를 매핑해야 하는 경우 빌더 패턴이랑 그닥 잘 매칭되지 않음

## Examples

[빌더 패턴으로 서브웨이 샌드위치 만들기(Kotlin)](https://github.com/Buzzvil/awesome-design-patterns/pull/27/commits/6cb276c91457e6bd49c3a25d05cf6fc1601dd815)
