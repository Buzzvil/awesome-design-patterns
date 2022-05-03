package main

type Manual interface {
	CookBread() string
	CookSteak() string
	CleanRoom() string
	ArrangeDesk() string
}

type chefRobotManual struct {
}

func (m *chefRobotManual) CookBread() string {
	return "Got excellent bread"

}
func (m *chefRobotManual) CookSteak() string {
	return "Got excellent steak"
}

func (m *chefRobotManual) CleanRoom() string {
	return "Got better contidioned room, but not clean enough"

}

func (m *chefRobotManual) ArrangeDesk() string {
	return "Got better contidioned room, but not clean enough"
}

type cleanRobotManual struct {
}

func (m *cleanRobotManual) CookBread() string {
	return "Got low quliaty Bread"
}
func (m *cleanRobotManual) CookSteak() string {
	return "Got low quality steak"
}

func (m *cleanRobotManual) CleanRoom() string {
	return "Got excellent room condition"
}

func (m *cleanRobotManual) ArrangeDesk() string {
	return "Got perfectly arranged desk"
}
