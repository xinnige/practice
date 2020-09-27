package main

import (
	"fmt"
)

func longestCommonPrefix(strs []string) string {
	prefix := make([]byte, 0)
	stop := false
	for i := 0; i < len(strs[0]); i++ {
		for j := 0; j < len(strs)-1; j++ {
			if i >= len(strs[j]) || i >= len(strs[j+1]) || strs[j][i] != strs[j+1][i] {
				stop = true
				break
			}
		}
		if stop {
			break
		}
		prefix = append(prefix, strs[0][i])
	}

	return string(prefix)
}

func main() {
	tests := []struct {
		strs   []string
		expect string
	}{
		{[]string{"flower", "flow", "flight"}, "fl"},
		{[]string{"dog", "racecar", "car"}, ""},
	}
	for _, tc := range tests {
		fmt.Printf("common prefix of %v is %s (expects %s)\n", tc.strs, longestCommonPrefix(tc.strs), tc.expect)
	}

}
