package main

import (
	"fmt"
	"sort"
)

/*
Level: Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

*/

func main() {
	strs := []string{"eat", "tea", "tan", "ate", "nat", "bat"}
	res := groupAnagrams(strs)
	fmt.Println(res)
}

func groupAnagrams(strs []string) [][]string {
	groupsMap := make(map[string][]string)

	for _, str := range strs {
		arr := []byte(str)
		sort.Slice(arr, func(i, j int) bool { return arr[i] < arr[j] })

		sortedStr := string(arr)
		groupsMap[sortedStr] = append(groupsMap[sortedStr], str)
	}

	res := make([][]string, 0, len(groupsMap))
	for _, group := range groupsMap {
		res = append(res, group)
	}

	return res
}
