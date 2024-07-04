package main

/*
Given two arrays of integers, return the sum of the two arrays as an array.

For example, if the input arrays are:
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

Then the output array would be:
[5, 7, 9]
*/

func sumTwoArray(arr1, arr2 []int) []int {
	if len(arr1) > len(arr2) {
		return solve(arr1, arr2)
	}
	return solve(arr2, arr1)
}

func solve(arr1, arr2 []int) []int {
	res := make([]int, 0)

	p1 := len(arr1) - 1
	p2 := len(arr2) - 1

	var o int
	for p1 >= 0 {
		n1 := arr1[p1]
		var n2 = 0
		if p2 >= 0 {
			n2 = arr2[p2]
		}

		sum := n1 + n2 + o
		o = sum / 10

		k := sum - (10 * o)
		res = append(res, k)

		p1--
		p2--
	}

	if o > 0 {
		res = append(res, o)
	}

	for i := 0; i < len(res)/2; i++ {
		j := len(res) - 1 - i
		res[i], res[j] = res[j], res[i]
	}

	return res
}
