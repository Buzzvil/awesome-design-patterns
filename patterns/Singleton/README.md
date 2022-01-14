# Singleton

## TL;DR

생성자가 여러 번 호출이 되어도 실제 생성되는 객체는 하나이고 최초 생성 이후에는 호출이 된 생성자는 최초의 생성자가 만든 객체를 리턴하는 방법. 즉, 전체 시스템 통틀어서 싱글톤 객체는 유일하며, 전역변수처럼 취급이 될 수 있다.

## Problem

로그를 기록하는 클래스를 정의했다고 가정하자. 각 레이어에서 이 클래스를 이용하여 같은 역할을 하는 객체를 생성한다면, 같은 기능을 하는 중복된 객체가 생성이 되므로 효율이 좋지 않다. 또한 코드 재활용이라는 기준으로 볼 때 적합하지 않다.

## Solution

다음과 같은 방법으로 문제를 해결합니다.
- 클래스에 하나의 인스턴스만 있는지 확인
- 클래스의 유일한 인스턴스에 쉽게 액세스
- 인스턴스화 제어
- 인스턴스 수 제한
- 전역 변수에 액세스

## Structure

클래스의 생성자를 숨기고 유일한 인스턴스를 반환하는 public static operation를 정의한다. private으로 숨겨진 생성자는 클래스 외부에서 인스턴스화 할 수 없고, 이 작업은 클래스명과 operation 이름으로만 접근이 가능하다. 이런 면에서, singleton은 다른 패턴들과도 호환이 가능하다.
- Abstract factory, factory method, builder, and prototype 패턴도 singleton으로 만들 수 있다.
- Facade 객체는 단 하나의 facade 객체가 필요하다는 의미에서 singleton으로 명시되기도 한다.
- Singleton은 어떠한 namespace에도 포함되지 않고, lazy allocation과 initialization을 서용하기 때문에 전역 변수처럼 사용이 될 수 있다.

## Pseudocode

```
class Singleton {
	void * __instance = null
}

Singoeton::Singleton (args)  {
	if __instance {
		return __instance
	} else {
		__instance = new Singleton(args)
		return __instance
	}	
}
```

## Anti-pattern

- 크게 의미가 없는 상황에서 불필요한 제한을 두어서 전역 변수로 사용하는 경우에 위험하다.
- 어디서든 접근이 가능하다는 것은, 개발자가 내부 작동 원리를 정확하게 알아야만 한다.
- **단일 책임 원칙을 위반한다.**
- 테스트가 어렵다.

## Examples

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* [singleton](/examples/Singleton/python/singleton.py)

![Kotlin](https://img.shields.io/badge/Kotlin-0095D5?&style=for-the-badge&logo=kotlin&logoColor=white)
* [singleton](/examples/Singleton/kotlin/singleton.kt)
