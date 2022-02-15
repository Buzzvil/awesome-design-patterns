package sample

type Phone interface {
	Call()
}

type IPhone struct{}

func (p IPhone) Call() {}

type GalaxyZFlip struct{}

func (p GalaxyZFlip) Call() {}

type Notebook interface {
	Boot()
}

type MacBook struct{}

func (m MacBook) Boot() {}

type GalaxyBook struct{}

func (g GalaxyBook) Boot() {}

type AbstractDeviceFactory interface {
	NewPhone() Phone
	NewNotebook() Notebook
}

type AppleDeviceFactory struct{}

func (f AppleDeviceFactory) NewPhone() Phone {
	return IPhone{}
}

func (f AppleDeviceFactory) NewNotebook() Notebook {
	return MacBook{}
}

type SamsungDeviceFactory struct{}

func (f SamsungDeviceFactory) NewPhone() Phone {
	return GalaxyZFlip{}
}

func (f SamsungDeviceFactory) NewNotebook() Notebook {
	return GalaxyBook{}
}
