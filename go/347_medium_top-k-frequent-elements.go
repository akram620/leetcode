package main

import "fmt"

/*
Level: Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

*/

func main() {
	nums := []int{1, 1, 1, 2, 2, 3}
	k := 2
	res := topKFrequent(nums, k)
	fmt.Println(res)
}

func topKFrequent(nums []int, k int) []int {
	counts := make(map[int]int, 0)

	for i := 0; i < len(nums); i++ {
		counts[nums[i]]++
	}

	freq := make([][]int, 0, len(nums))

	for i := 0; i < len(nums); i++ {
		el := make([]int, 0)
		freq = append(freq, el)
	}

	for el, count := range counts {
		freq[count-1] = append(freq[count-1], el)
	}

	res := make([]int, 0, k)
	for i := len(freq) - 1; i >= 0; i-- {
		if len(freq[i]) > 0 {
			res = append(res, freq[i]...)
		}
		if len(res) == k {
			break
		}
	}
	return res
}
