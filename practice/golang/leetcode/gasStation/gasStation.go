package main

func getLowestIndex(gas, cost []int) int {
	tank := gas[0] - cost[0]
	minTank := tank
	minIndex := 0
	for i := 1; i < len(gas); i++ {
		tank += gas[i] - cost[i]
		if minTank >= tank {
			minTank = tank
			minIndex = i
		}
	}
	return (minIndex + 1) % len(gas)
}

func canCompleteCircuit(gas []int, cost []int) int {
	if len(gas) == 0 {
		return -1
	}
	if len(gas) != len(cost) {
		return -1
	}

	minIndex := getLowestIndex(gas, cost)
	tank := 0
	for i := 0; i < len(gas); i++ {
		index := (minIndex + i) % len(gas)
		tank += gas[index] - cost[index]
		if tank < 0 {
			return -1
		}
	}
	return minIndex
}
