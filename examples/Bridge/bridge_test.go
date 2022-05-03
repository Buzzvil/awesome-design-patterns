package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestWithChefRobotPrepareLunch(t *testing.T) {
	chefRobot := ChefRobot{&chefRobotManual{}, []string{}}

	chefRobot.PrepareLunch()

	output := chefRobot.GetOutput()
	assert.Equal(t, output[0], "Got excellent bread")
	assert.Equal(t, output[1], "Got excellent steak")
	assert.Equal(t, output[2], "Chef Robot Performed Following Jobs.")

}
func TestWithChefRobotCleanHouse(t *testing.T) {
	chefRobot := ChefRobot{&chefRobotManual{}, []string{}}

	chefRobot.CleanHouse()

	output := chefRobot.GetOutput()
	assert.Equal(t, output[0], "Got better contidioned room, but not clean enough")
	assert.Equal(t, output[1], "Got better contidioned room, but not clean enough")
	assert.Equal(t, output[2], "Chef Robot Performed Following Jobs.")

}

func TestWithCleaningRobotPrepareLunch(t *testing.T) {
	chefRobot := CleaningRobot{&cleanRobotManual{}, []string{}}

	chefRobot.PrepareLunch()

	output := chefRobot.GetOutput()
	assert.Equal(t, output[0], "Got low quliaty Bread")
	assert.Equal(t, output[1], "Got low quality steak")
	assert.Equal(t, output[2], "Cleaning Robot Performed Following Jobs.")
}

func TestWithCleaningRobotCleanHouse(t *testing.T) {
	chefRobot := CleaningRobot{&cleanRobotManual{}, []string{}}

	chefRobot.CleanHouse()

	output := chefRobot.GetOutput()
	assert.Equal(t, output[0], "Got excellent room condition")
	assert.Equal(t, output[1], "Got perfectly arranged desk")
	assert.Equal(t, output[2], "Cleaning Robot Performed Following Jobs.")
}
