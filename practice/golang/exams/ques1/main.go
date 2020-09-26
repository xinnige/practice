package main

import (
	// "fmt"
	"sort"
)

func getNeighbor(citymap [][]int, city int) []int {
	neighbors := make([]int, 0)
	for i, v := range citymap[city] {
		if v == 1 {
			neighbors = append(neighbors, i)
		}
	}
	return neighbors
}

func getConnectedCity(citymap [][]int, city, except int) []int {
	neighbors := make([]int, 0)
	for i, v := range citymap[city] {
		if v == 1 && i != except {
			neighbors = append(neighbors, i)
		}
	}
	for _, n := range neighbors {
		nexts := getConnectedCity(citymap, n, city)
		neighbors = append(neighbors, nexts...)
	}
	return neighbors
}

func getDp(citymap [][]int, city, except int) int {
	connected := getConnectedCity(citymap, city, except)
	return len(connected) + 1
}

func getDps(citymap [][]int, city int) int {
	count := 0
	neighbors := getNeighbor(citymap, city)
	for _, neighbor := range neighbors {
		idp := getDp(citymap, neighbor, city)
		if idp > count {
			count = idp
		}
	}
	return count
}

func getMinDp(matrix [][]int) []int {
	citymap := make([][]int, len(matrix)+1)
	for i := 0; i <= len(matrix); i++ {
		citymap[i] = make([]int, len(matrix)+1)
	}
	for _, v := range matrix {
		citymap[v[0]-1][v[1]-1] = 1
		citymap[v[1]-1][v[0]-1] = 1
	}
	mapdp := make(map[int][]int)
	for i := range citymap {
		dps := getDps(citymap, i)
		mapdp[dps] = append(mapdp[dps], i)
	}
	mlen := make([]int, len(mapdp))
	i := 0
	for k := range mapdp {
		mlen[i] = k
		i++
	}
	sort.Ints(mlen)

	ret := make([]int, len(mapdp[mlen[0]]))
	for i, v := range mapdp[mlen[0]] {
		ret[i] = v + 1
	}
	return ret

}
