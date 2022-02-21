package facade

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestWithFacadePattern(t *testing.T) {
	home := SmartHome{light: Light{StateOff}, computer: Computer{StateOff}, heater: Heater{StateOff}}
	home.Start()

	assert.Equal(t, StateOn, home.light.state)
	assert.Equal(t, StateOn, home.computer.state)
	assert.Equal(t, StateOn, home.heater.state)
}

func TestWithoutFacadePattern(t *testing.T) {
	light := Light{StateOff}
	computer := Computer{StateOff}
	heater := Heater{StateOff}

	light.TurnOn()
	computer.Boot()
	heater.Load()

	assert.Equal(t, StateOn, light.state)
	assert.Equal(t, StateOn, computer.state)
	assert.Equal(t, StateOn, heater.state)
}
