package main

// in: ababcbacadefegdehijhklij
// out: [9, 7, 8]
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
