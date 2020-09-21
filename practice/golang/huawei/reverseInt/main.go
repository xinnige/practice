package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func reverseInt(number1 int) string {
	num := strconv.Itoa(number1)
	reverse := make([]byte, len(num))
	for i := range num {
		reverse[i] = num[len(num)-1-i]
	}
	return fmt.Sprintf("%s", reverse)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	input := scanner.Text()
	number, _ := strconv.Atoi(input)
	fmt.Printf("%s\n", reverseInt(number))
}
