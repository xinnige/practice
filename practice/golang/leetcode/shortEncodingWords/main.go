package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

func minimumLengthEncoding(words []string) int {
	lenmap := make(map[int][]string)
	for _, s := range words {
		slen := len(s)
		lenmap[slen] = append(lenmap[slen], s)
	}
	lengths := make([]int, 0)
	for k := range lenmap {
		lengths = append(lengths, k)
	}
	sort.Ints(lengths)
	codeStr := ""
	for i := len(lengths) - 1; i >= 0; i-- {
		strs := lenmap[lengths[i]]
		for _, s := range strs {
			if !strings.Contains(codeStr, s+"#") {
				codeStr += fmt.Sprintf("%s#", s)
			}
		}
	}
	return len(codeStr)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		t := scanner.Text()
		fmt.Printf("%d\n", minimumLengthEncoding(strings.Split(t, " ")))
	}
}
