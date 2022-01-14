# Abstract factory

## TL;DR

Abstract factory는 하나의 카테고리 내에서 연관되어 있는 서로 다른 Object들을 생성하기 위한 방법을 제공한다.

## Problem

버즈빌에서는 복지 차원에서 전 직원에게 새 스마트폰과 노트북을 지급하기로 결정하였다. 버즈빌 직원들은 기기 간의 연동을 중요하게 생각하기 때문에 각각의 기기는 항상 같은 회사의 제품이어야 한다. 직원마다 선호도의 차이가 있기 때문에 애플과 삼성의 제품 중에 선택이 가능하도록 한다.

|       |스마트폰       |노트북       |
|-------|-------------|-----------|
|Apple  |iPhone       |MacBook    |
|Samsung|Galaxy Z Flip|Galaxy Book|

스마트폰, 노트북을 각각 Product
이를 시스템으로 구현하기 위해서는 다음과 같은 요구사항이 도출된다.

* 같은 Product family(회사)에 속하는 서로 다른 Product를 생성할 수 있는 방법이 필요하다.
* Product familiy는 변경되거나 추가될 수 있고, 이 때마다 client의 코드가 변경되는 것을 방지해야 한다.

## Solution

각 Product마다 interface를 만들고, 실제 Product는 해당 interface를 구현한다. (e.g. iPhone, Galaxy -> Phone)

각 Product의 interface를 생성하는 factory method를 포함하고 있는 abstract factory를 정의하고 client는 이에 의존한다.

Product family마다 abstract factory의 구현체를 구현한다.


## Structure

![image](https://www.plantuml.com/plantuml/png/bP8nReKm38Ptdy9Zkt00XefuwDgX9qXJKv0WaHmpL5NltfHGQg4dyK1Y-27VdtoAkwnUT9ad6AEoz3umkhUiueC-bpV99tu1biTX4FRAxk5npRHbAlaR84m-PtnDCr_1xFfcQPwEUqDCoYZZnw2OUblVjbil80hh8h7kxe3ZE_vYvomTMFfd_uHUT62vObI1-vNi-XjEzR-LEgNfI1ijSyjaheoiBG6it-hfgHhjoSw9QN2smTK6j_dNXZr1LuvJ9ku7)


## Pros & Cons

✅ SRP. Product object를 생성하기 위한 로직은 Factory에서 집약적으로 관리한다.

✅ OCP. 새로운 Product family가 추가되는 경우 factory 구현체를 추가하여 확장 가능하며, 이는 client code에 변경을 요구하지 않는다.

❌ Product와 Factory를 표현하기 위한 interface와 class를 많이 관리해야 하므로 코드가 복잡해진다.

## Examples

![Go](https://img.shields.io/badge/Go-lightgrey?style=flat&logo=go)
* [sample](/examples/go/abstract_factory/sample.go)
