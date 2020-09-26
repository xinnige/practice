package main

import (
	"fmt"
	"sort"
)

func frequencySort(s string) string {
	byteMap := make(map[byte]int)
	for i := range s {
		byteMap[s[i]] += 1
	}
	freqMap := make(map[int][]byte)
	for k, v := range byteMap {
		freqMap[v] = append(freqMap[v], k)
	}

	freqs := make([]int, 0)
	for k := range freqMap {
		freqs = append(freqs, k)
	}
	sort.Ints(freqs)
	freqStr := make([]byte, 0)
	for i := len(freqs) - 1; i >= 0; i-- {
		for _, fbyte := range freqMap[freqs[i]] {
			for c := 0; c < freqs[i]; c++ {
				freqStr = append(freqStr, fbyte)
			}
		}
	}
	return string(freqStr)
}

func main() {
	tests := []struct {
		input  string
		expect string
	}{
		{"a", "a"},
		{"tree", "eert"},
		{"cccaaa", "cccaaa"},
		{"Aabb", "bbAa"},
	}
	for _, tc := range tests {
		fmt.Printf("%s -> %s (%s)\n", tc.input, frequencySort(tc.input), tc.expect)
	}
}
