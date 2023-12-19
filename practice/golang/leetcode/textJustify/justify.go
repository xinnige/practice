package main

import "strings"

func fullJustify(words []string, maxWidth int) []string {
	result := []string{}
	lines := make([][]string, 0)
	sizes := make([]int, 0)
	if len(words) == 0 {
		return result
	}
	var i int
	for i = 0; i < len(words)-1; i++ {
		// newline
		line := []string{words[i]}
		lineSize := len(words[i])
		for (i < len(words)-1) && (lineSize+len(words[i+1])+1 <= maxWidth) {
			lineSize += 1 + len(words[i+1])
			line = append(line, " ", words[i+1])
			i += 1
		}
		lines = append(lines, line)
		sizes = append(sizes, lineSize)
	}
	// last word
	if i < len(words) {
		// only one word
		if len(lines) > 0 && (sizes[len(lines)-1]+1+len(words[i]) <= maxWidth) {
			// append to the last line
			lines[len(lines)-1] = append(lines[len(lines)-1], words[i])
			sizes[len(lines)-1] += len(words[i]) + 1
		} else {
			// need new line
			lines = append(lines, []string{words[i]})
			sizes = append(sizes, len(words[i]))
		}
	}

	for i := 0; i < len(lines)-1; i++ {
		justify(lines[i], sizes[i], maxWidth)
		result = append(result, strings.Join(lines[i], ""))
	}

	// last line left justified
	lastLine := strings.Join(lines[len(lines)-1], "")
	for delta := maxWidth - sizes[len(lines)-1]; delta > 0; delta-- {
		lastLine += " "
	}
	result = append(result, lastLine)

	return result
}

func justify(line []string, lineSize, width int) {
	delta := width - lineSize
	if len(line) == 1 {
		for delta > 0 {
			line[0] += " "
			delta -= 1
		}
		return
	}
	// line >= 2
	var j int = 1
	for delta > 0 {
		line[j] += " "
		delta -= 1
		j = j + 2
		if j >= len(line) {
			j = 1
		}
	}
}
