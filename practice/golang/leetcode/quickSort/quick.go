package main

func quickSort(nums []int, left, right int) {
	if left >= right {
		return
	}
	i, j := left, right
	p := nums[i]

	for i < j {

		// until smaller than p
		for i < j && nums[j] >= p {
			j--
		}
		// replace, p = nums[i] no need swap
		nums[i] = nums[j]

		// until larger than p
		for i < j && nums[i] <= p {
			i++
		}
		// replace with last j item
		nums[j] = nums[i]

	}

	// replace with p = nums[i] origin
	nums[j] = p

	quickSort(nums, left, i-1)
	quickSort(nums, i+1, right)
}
