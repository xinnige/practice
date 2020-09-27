package main

import (
	"fmt"
)

func fullPermute(letters [][]byte) [][]byte {
	ret := make([][]byte, 0)
	if len(letters) == 0 {
		return [][]byte{}
	}
	if len(letters) == 1 {
		for _, v := range letters[0] {
			ret = append(ret, []byte{v})
		}
		return ret
	}

	for _, v := range fullPermute(letters[1:]) {
		for _, l := range letters[0] {
			ret = append(ret, append([]byte{l}, v...))
		}
	}
	return ret
}

func letterCombinations(digits string) []string {
	buttons := map[byte][]byte{
		'2': []byte("abc"),
		'3': []byte("def"),
		'4': []byte("ghi"),
		'5': []byte("jkl"),
		'6': []byte("mno"),
		'7': []byte("pqrs"),
		'8': []byte("tuv"),
		'9': []byte("wxyz"),
	}
	letters := make([][]byte, 0)
	for i := range digits {
		letters = append(letters, buttons[digits[i]])
	}
	permutes := fullPermute(letters)

	ret := make([]string, len(permutes))
	for i := range permutes {
		ret[i] = string(permutes[i])
	}
	return ret
}

func main() {
	tests := []struct {
		input  string
		expect []string
	}{
		{"23", []string{"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}},
		{"", []string{}},
	}
	for _, tc := range tests {
		fmt.Printf("%s  -> %v (expects %v)\n", tc.input, letterCombinations(tc.input), tc.expect)
	}
}
