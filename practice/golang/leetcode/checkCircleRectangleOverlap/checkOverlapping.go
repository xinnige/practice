package main

func checkOverlap(radius int, x_center int, y_center int, x1 int, y1 int, x2 int, y2 int) bool {

	return true
}

func main() {
	inputs := []struct {
		r, x, y, x1, y1, x2, y2 int
		expect                  bool
	}{
		{1, 1, 1, 1, 1, 1, 1, true},
	}
	for _, input := range inputs {
		result := checkOverlap(input.r, input.x, input.y, input.x1, input.y1, input.x2, input.y2)
		if result != input.expect {
			panic("failed")
		}
	}
}
