package main

const StateOn = "ON"

type Light struct {
	state string
}

func (l *Light) TurnOn() {
	l.state = StateOn
}

type Heater struct {
	state string
}

func (h *Heater) Load() {
	h.state = StateOn
}

type Computer struct {
	state string
}

func (c *Computer) Boot() {
	c.state = StateOn
}

// It's Facade for light, heater, computer
type SmartHome struct {
	light    Light
	heater   Heater
	computer Computer
}

func (s *SmartHome) Start() {
	s.light.TurnOn()
	s.heater.Load()
	s.computer.Boot()
}
