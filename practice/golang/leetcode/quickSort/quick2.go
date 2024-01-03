package main

func quickSort2(nums []int, left, right int) {
	if len(nums) <= 1 {
		return
	}
	if left >= right {
		return
	}

	i, j := left, right
	p := nums[i]

	for i < j {
		for i < j && nums[j] >= p {
			j--
		}

		nums[i] = nums[j]

		for i < j && nums[i] <= p {
			i++
		}

		nums[j] = nums[i]
	}

	nums[j] = p

	quickSort(nums, left, i-1)
	quickSort(nums, i+1, right)
}
