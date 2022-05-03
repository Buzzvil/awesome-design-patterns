package main

type Robot interface {
	PrepareLunch()
	CleanHouse()
	GetOutput() []string
}

type ChefRobot struct {
	manual Manual
	output []string
}

func (r *ChefRobot) PrepareLunch() {
	r.output = append(r.output, r.manual.CookBread())
	r.output = append(r.output, r.manual.CookSteak())
}

func (r *ChefRobot) CleanHouse() {
	r.output = append(r.output, r.manual.CleanRoom())
	r.output = append(r.output, r.manual.ArrangeDesk())
}

func (r *ChefRobot) GetOutput() []string {
	output := append(r.output, "Chef Robot Performed Following Jobs.")
	return output
}

type CleaningRobot struct {
	manual Manual
	output []string
}

func (r *CleaningRobot) PrepareLunch() {
	r.output = append(r.output, r.manual.CookBread())
	r.output = append(r.output, r.manual.CookSteak())
}

func (r *CleaningRobot) CleanHouse() {
	r.output = append(r.output, r.manual.CleanRoom())
	r.output = append(r.output, r.manual.ArrangeDesk())
}

func (r *CleaningRobot) GetOutput() []string {
	output := append(r.output, "Cleaning Robot Performed Following Jobs.")
	return output
}
