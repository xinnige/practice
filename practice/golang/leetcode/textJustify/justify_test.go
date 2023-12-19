package main

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestFullJustify(t *testing.T) {
	tests := []struct {
		input  []string
		width  int
		expect []string
	}{
		// {[]string{"This", "is", "an", "example", "of", "text", "justification."}, 16, []string{"This    is    an", "example  of text", "justification.  "}},
		// {[]string{"test"}, 5, []string{"test"}},
		{[]string{"a"}, 2, []string{"a "}},
		// {[]string{"What", "must", "be", "acknowledgment", "shall", "be"}, 16, []string{"What   must   be", "acknowledgment  ", "shall be        "}},
		// {[]string{"Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"}, 20, []string{"Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  "}},
	}

	for _, tc := range tests {
		require.Equal(t, tc.expect, fullJustify(tc.input, tc.width))
	}
}
