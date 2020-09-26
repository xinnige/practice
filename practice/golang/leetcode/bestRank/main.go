package main

import (
	"fmt"
	"sort"
)

func findRankFloat(rank []float64, score float64) int {
	for i := len(rank) - 1; i >= 0; i-- {
		if rank[i] == score {
			return len(rank) - i
		}
	}
	return len(rank)
}

func findRank(rank []int, score int) int {
	for i := len(rank) - 1; i >= 0; i-- {
		if rank[i] == score {
			return len(rank) - i
		}
	}
	return len(rank)
}

func compareRank(ranks []int) (int, int) {
	highest := 999
	highestIdx := -1
	for i := range ranks {
		if ranks[i] < highest {
			highest = ranks[i]
			highestIdx = i
		}
	}
	return highest, highestIdx + 1
}

func getCountryRank(mscore, golden, prize []int, avggolden, avgprize []float64) (int, int) {
	goldenRank := findRank(golden, mscore[0])
	prizeRank := findRank(prize, mscore[1])
	avggoldenRank := findRankFloat(avggolden, float64(mscore[0])/float64(mscore[2]))
	avgprizeRank := findRankFloat(avgprize, float64(mscore[1])/float64(mscore[2]))
	return compareRank([]int{goldenRank, prizeRank, avggoldenRank, avgprizeRank})
}

func rank(scores [][]int, m []int) [][]int {
	golden := make([]int, len(scores))
	prize := make([]int, len(scores))
	avggolden := make([]float64, len(scores))
	avgprize := make([]float64, len(scores))

	for i, v := range scores {
		golden[i] = v[0]
		prize[i] = v[1]
		avggolden[i] = float64(v[0]) / float64(v[2])
		avgprize[i] = float64(v[1]) / float64(v[2])
	}
	sort.Ints(golden)
	sort.Ints(prize)
	sort.Float64s(avggolden)
	sort.Float64s(avgprize)

	mranks := make([][]int, len(m))
	for i, v := range m {
		rank, code := getCountryRank(scores[v], golden, prize, avggolden, avgprize)
		mranks[i] = []int{rank, code}
	}
	return mranks
}

func main() {
	tests := []struct {
		scores    [][]int
		countries []int
		expect    [][]int
	}{
		{
			[][]int{[]int{51, 100, 1000}, []int{36, 110, 300}, []int{6, 14, 32}, []int{5, 18, 40}},
			[]int{0, 1, 2, 3},
			[][]int{[]int{1, 1}, []int{1, 2}, []int{1, 3}, []int{1, 4}},
		},
	}

	for _, tc := range tests {
		fmt.Printf("%v (expects %v)\n", rank(tc.scores, tc.countries), tc.expect)
	}
}
