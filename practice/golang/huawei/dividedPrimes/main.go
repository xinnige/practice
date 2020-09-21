package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	if n == 2 || n == 3 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	sqroot := int(math.Sqrt(float64(n)))

	for i := 3; i <= sqroot; i = i + 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func getPrimes(n int) []int {
	primes := []int{2}
	for i := 3; i < n; i = i + 2 {
		if isPrime(i) {
			primes = append(primes, i)
		}
	}
	return primes
}

func dividePrimes(n int) []int {
	if isPrime(n) {
		return []int{n}
	}
	primes := getPrimes(n)
	//fmt.Printf("get primes: %v\n", primes)
	divides := make([]int, 0)
	for i := 0; i < len(primes); {
		if n%primes[i] == 0 {
			divides = append(divides, primes[i])
			n = n / primes[i]
		} else {
			i++
		}
		if n == 1 {
			break
		}
	}
	return divides
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	text := scanner.Text()
	number, _ := strconv.Atoi(text)
	divides := dividePrimes(number)
	for _, d := range divides {
		fmt.Printf("%d ", d)
	}
	fmt.Printf("\n")
}
