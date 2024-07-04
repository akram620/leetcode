package main

/*
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
*/

func partitionLabels(s string) []int {

	g := make(map[uint8]int)
	l := make(map[uint8]int)

	m := 0

	for i := 0; i < len(s); i++ {
		r := s[i]

		_, ok := l[r]
		if !ok {
			l[r] = 0
		}
		l[r]++

		gNum, ok := g[r]
		if !ok {
			m++
			g[r] = m
			continue
		}

		if gNum == m {
			continue
		}

		// seen
		for k, _ := range g {
			if g[k] > gNum {
				g[k] = gNum
			}
		}

		m = gNum
	}

	// g = {a: 1, b: 1}
	// l = {a: 2, b: 2}

	res := make([]int, m)
	for k, v := range g {
		res[v-1] += l[k]
	}

	return res
}
