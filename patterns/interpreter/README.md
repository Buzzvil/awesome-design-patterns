# Interpreter

## TL;DR

Interpreter 패턴은 언어의 문장을 평가하는 방법론을 정하는 디자인 패턴입니다.
주로 각 기호에 대한 클래스를 갖는 방향으로 구성합니다. 이 방법으로 신택스 트리는 복합 패턴의 인스턴스이며 클라이언트에 대한 문장을 해석하는 데 사용이 됩니다.
이를 이해하기 위해서는 Composite 패턴을 이해해야 합니다.

## Problem

Interpreter 패턴은 다음 문제를 해결합니다.

1. 언어의 문장이 해석될 수 있도록 간단한 언어의 문법을 어떻게 정의할 것인가?
특정 종류의 문제가 자주 발생한다면 문제의 사례를 간단한 언어로 문장으로 표현을 하는 것이 좋은 방법일 수 있습니다.
예를 들어, 검색 표현식을 정하는 것은 자주 발생하는 문제입니다. 클래스 내에서 필요할 때마다 구현하는 것은 유연성이 떨어지기 때문에, 좋은 설게 방법이 아닙니다.
이런 경우에는 검색 표현식을 동적으로 지정하고 해석할 수 있는 쿼리 언어를 정의하는 것이 더 좋습니다.

## Solution

Interpreter 패턴은 다음 해결을 제시합니다.
1. Expression class를 사용하여 언어에 대한 문법을 정의합니다.
2. AST(Abstract Syntax Tree)로 문장을 언어로 표현합니다.
3. AST에서 Interpreter(Context)를 호출하여 문장을 해석합니다.

## Structure

![image](url)

클래스의 생성자를 숨기고 유일한 인스턴스를 반환하는 public static operation를 정의합니다.
private으로 숨겨진 생성자는 클래스 외부에서 인스턴스화 할 수 없고, 이 작업은 클래스명과 operation 이름으로만 접근이 가능합니다.
이런 면에서, singleton은 다른 패턴들과도 호환이 가능합니다.
- Abstract factory, factory method, builder, and prototype 패턴도 Singleton으로 만들 수 있습니다.
- Facade 객체는 단 하나의 facade 객체가 필요하다는 의미에서 Singleton으로 명시되기도 합니다.
- Singleton은 어떠한 namespace에도 포함되지 않고, lazy allocation과 initialization을 서용하기 때문에 전역 변수처럼 사용이 될 수 있습니다.

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
| Pros | Cons |
|------|------|
|문법을 쉽게 변경할 수 있습니다.|복잡한 문법을 표현하기 어렵게 만듭니다.|
|새로운 종류의 인터프리터를 쉽게 추가할 수 있습니다.|      |

## Examples

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Kotlin](https://img.shields.io/badge/Kotlin-0095D5?&style=for-the-badge&logo=kotlin&logoColor=white)
