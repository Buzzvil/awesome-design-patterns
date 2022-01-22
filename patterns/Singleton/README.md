# Singleton

## TL;DR

Singleton은 앱이 실행되는 동안에 한 클래스가 유일한 인스턴스를 가진다는 것을 보장하고, 이 인스턴스에 전역 접근을 허용하는 디자인 패턴입니다.

## Problem

Singleton 패턴은 단일 책임 원칙(Single Responsibility Principle, a.k.a SRP)을 위반함으로써 두 개의 문제를 해결합니다.
1. 클래스는 유일한 인스턴스를 가집니다. 
2. 이 인스턴스에 대하여 전역 접근을 허용합니다.

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
class Log is
    private static instance: Log

    private constructor Log() is
    // initialize Log instance
    public static method getInstance() is
        if (Log.instance == null) then
            acquireThreadLock()
            if (Log.instance == null) then
                Log.instance = new Log()
        return Log.instance

    // Any singleton should define some business logic
    // which can be executed on its instance.
    public method info(str) is
        // record
}

class Application is 
    method main() is 
        Log foo = Log.getInstance()
        foo.info("Hello World!")
        ...
        Log bar = Log.getInstance()
        bar.info("Hello World!")
        // foo is the same object as bar 
```

## Pros and Cons

+ 단일 인스턴스를 사용한다는 것을 보장합니다.
+ 해당 인스턴스에 대해서 전역 접근 포인트가 생깁니다.
+ 처음 선언될 때 초기화되고, 이후에는 변하지 않습니다.
- **단일 책임 원칙을 위반합니다.**
- 프로그램의 각 컴포넌트가 너무 많이 알게 되면, Singleton 패턴은 잘못된 디자인을 숨길 수 있습니다.
- 멀티쓰레드 환경에서 별도 처리를 하지 않으면 각 쓰레드 별로 Singleton 객체를 만들 위험이 있습니다.
- 클라이언트 측면에서 볼 때 유닛 테스트가 어렵습니다. 대부분의 테스트 프레임워크는 mocking 객체를 만들 때 상속에 의존하게 됩니다. 
  Singleton 클래스의 생성자가 private이고 정적 메서드를 overriding하는 것이 대부분의 언어에서 허용하지 않기 때문에,
  이 패턴을 mocking하기가 어렵습니다. 보통 이러한 경우에 테스트 코드를 작성하지 않거나 이 패턴을 포기하게 됩니다.

## Examples

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* [singleton](/examples/Singleton/python/singleton.py)

![Kotlin](https://img.shields.io/badge/Kotlin-0095D5?&style=for-the-badge&logo=kotlin&logoColor=white)
* [singleton](/examples/Singleton/kotlin/singleton.kt)
