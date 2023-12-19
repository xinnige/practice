package main

func calculate(s string) int {
	var max uint = 1<<31 - 1
	var overflow bool = false

	neg := 1
	cursor := 0
	for i := cursor; i < len(s); i++ {
		if s[i] == ' ' {
			continue
		} else {
			cursor = i
			break
		}
	}
	for i := cursor; i < len(s); i++ {
		if s[i] == '-' {
			neg = -1
			cursor = i + 1
			break
		}
		if s[i] == '+' {
			cursor = i + 1
			break
		} else {
			break
		}
	}
	// calculate the number
	var number uint = 0
	for i := cursor; i < len(s); i++ {
		if s[i] >= '0' && s[i] <= '9' {
			raw := number*10 + uint(s[i]-'0')
			if raw >= number {
				number = raw
			} else {
				overflow = true
			}
		} else {
			break
		}
	}
	if neg == -1 {
		if number > max+1 || overflow {
			return -1 * int(max+1)
		}
	} else {
		if number > max || overflow {
			return int(max)
		}
	}

	return int(number) * neg
}

func myAtoi(s string) int {
	return calculate(s)
}
