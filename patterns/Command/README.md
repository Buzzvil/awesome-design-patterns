# Command
## TL;DR
- 요청을 객체의 형태로 캡슐화하여 서로 요청이 다른 사용자의 매개변수화, 요청 저장 또는 로깅, 그리고 연산의 취소를 지원하게 만드는 패턴입니다.

## Problem


## Solution


## Structure
```mermaid
classDiagram
    class Client{
    }
    class Receiver{
      operation((a, b, c)
    }
    class Command{
      execute()
    }
    class ConcreteCommand1{
      receiver
      params
      Command1(receiver, params)
      execute()
    }
    class ConcreteCommand2{
      execute()
    }
    class Invoker{
      command
      setCommand(command)
      executeCommand()
    }
    Invoker <-- Client
    Receiver <-- Client
    ConcreteCommand1 <.. Client
    Command <|-- ConcreteCommand1
    Receiver <-- ConcreteCommand1
    Command <|-- ConcreteCommand2
    Command <-- Invoker
```

## Pros & Cons
- 👍
- 👍
- 👎


## Examples
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* [example-1](/examples/Command/python/example-1.py)
