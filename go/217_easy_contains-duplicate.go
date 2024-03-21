package main

/*
Level: Easy

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109

*/

func main() {
	nums := []int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}
	println(containsDuplicate(nums))
}

func containsDuplicate(nums []int) bool {
	m := make(map[int]bool)
	for _, v := range nums {
		if m[v] {
			return true
		}
		m[v] = true
	}
	return false
}
