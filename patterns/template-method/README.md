# Template method pattern

## TL;DR

알고리즘의 구조를 변경하지 않고 알고리즘의 특정 단계들을 다시 정의할 수 있게 해주는 패턴 (출처: 위키피디아)

## Problem

버즈스크린을 연동하면 바로 사용할 수 있는 기본 잠금화면(SimpleLockerActivity)을 제공해야 합니다. 또한 퍼블리셔가 화면을 직접 재구성한 커스텀 잠금화면을 만들 수도 있어야 합니다.

액티비티(안드로이드에서 Activity는 하나의 화면이라고 보시면 됩니다)의 생성(onCreate)부터 소멸(onDestroy)까지 정해진 라이프사이클이 있습니다. 각 단계마다 기본 잠금화면과 커스텀 잠금화면은 뷰 구성 정도를 제외하면 대부분의 기능이 동일합니다.

호출되는 순서가 정해져 있으면서 중복되는 코드가 많은 경우에 템플릿 메서드 패턴을 사용할 수 있습니다.

## Solution

abstract class인 BaseLockerActivity를 만듭니다.
기본 잠금화면을 제공하기 위해 BaseLockerActivity를 상속받아 SimpleLockerActivity를 구현합니다.
퍼블리셔 또한 BaseLockerActivity를 상속받아 직접 잠금화면을 구현할 수 있습니다.

뷰를 제외한 잠금화면의 기본 로직은 BaseLockerActivity에서 순서대로 제어합니다.

기본 잠금화면(SimpleLockerActivity) 또는 커스텀 잠금화면에서는
- onCurrentCampaignUpdated, onTimeUpdated 등 추상 메서드는 필수적으로 구현해야합니다.
- onCreate, onDestroy 등 BaseLockerActivity에서 구현이 되어 있는 로직은 BaseLockerActivity의 기본 구현을 사용하면서 필요한 경우 오버라이드합니다.

## Structure

![Template method pattern structure](https://refactoring.guru/images/patterns/diagrams/template-method/structure-indexed-2x.png)

## Pseudocode

```kotlin
abstract class BaseLockerActivity : Activity() {
    override protected fun onCreate() {
        super.onCreate()

        // 버즈스크린 컴포넌트 가져오기
        // 잠금화면에 필요한 설정값 가져오기
        ...
    }

    override protected fun onDestroy() {
        ...
        super.onDestroy()
    }

    protected abstract fun onCurrentCampaignUpdated(Campaign campaign)

    protected abstract fun onTimeUpdated(Calendar cal)
}

class SimpleLockerActivity : BaseLockerActivity {
    override protected fun onCreate() {
        super.onCreate()
        initUI();
    }

    private fun initUI() {
        // 화면을 구성하는 뷰 초기화
    }

    override fun onCurrentCampaignUpdated(Campaign campaign) {
        // 캠페인이 업데이트 되었을 때 UI 업데이트
    }

    override fun onTimeUpdated(Calendar cal) {
        // 날짜 및 시간 관련 UI 업데이트
    }
}

class CustomLockerActivity : BaseLockerActivity {
    override protected fun onCreate() {
        super.onCreate()
        initUI();
    }

    private fun initUI() {
        // 화면을 구성하는 뷰 초기화
    }

    override fun onCurrentCampaignUpdated(Campaign campaign) {
        // 캠페인이 업데이트 되었을 때 UI 업데이트
        // 원하는 기능 추가(ex. 로그 기록)
    }

    override fun onTimeUpdated(Calendar cal) {
        // 날짜 및 시간 관련 UI 업데이트
        // 원하는 기능 추가(ex. 세계시간을 추가로 표시)
    }
}
```

## Pros & Cons

### Pros

- 알고리즘(순서)을 유지한 상태로 특정 부분만 클라이언트가 재정의할 수 있습니다.
- 중복 코드를 슈퍼클래스로 가져올 수 있습니다.

### Cons

- 정해진 골격에 제한됩니다.
- 하위클래스에서 기본 구현을 오버라이드 하면서 동작이 변경되면 리스코프 치환 원칙을 위배할 수 있습니다.
- 하위클래스는 비교적 자유롭게 추가/수정이 가능하지만 슈퍼클래스의 변경은 어렵습니다.

## Examples

[예제 코드](./example.kt)