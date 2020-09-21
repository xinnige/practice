package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCommonStr(t *testing.T) {
	tests := []struct {
		s1     string
		s2     string
		expect string
	}{
		{"asdfas", "werasdfaswer", "asdfas"},
		{"", "", ""},
		{"1", "2", ""},
		{"abc", "c", "c"},
		{"b", "abc", "b"},
		{"abc", "abc", "abc"},
		{
			"ujlzfqqscymxyooumhfwuokwvjnkboqwbsjktburxsazwrjltmmnuxsigpvsusgpztxodwfhagyzxpocvmladimtzfwwgkbarhmjthuubccwzvkgadrnpcr",
			"qmuwdtbmltlciaxogzjjktzyegefnkezoouvhbxxtnnctihybsnchumrxysynyhciezgbwjzljuhpgiiuwouyevymbhwsopcyhyhswhmdpdqajvpgitqxczkfegrqhgxlvykbhymnjjpgufdxccjacnfzxmejzrkywwazfiyuwmfbifhllebzojlqlqgpamzwawpgjaatgnrfpmlmgvsnlhufmvzrjwhmdwhxxiksqbwqgkakivvahjntcswdyllwjtwdyspae",
			"oou",
		},
		{
			"yrtqyfxyrmbasfmkbuudetaahxxgvcpkfhlkfxtjvguizsmwbnwamftshffyzumqfzqvirxgjjuocobvhvgstvrynduavkvntvxgnravjyfjkycguqyrnbnwnoqvhh",
			"xxzjrwyqtgzfgxyitvszmltcsdjweeycqgzsazahpqrvlgvwexcfwkusmuyltvtbjftkvwebmjctwbfcxfimoevbquznojlzkxygruhebhostshenguhymzjxhkjstiwzgyudtfeddgqlegxesngnlbubkhzfmspalfajiqsvohghxhswjiimnyazfmgqazdewfptldiilrwkhuntvseohykutjecuhg",
			"tsh",
		},
	}
	for _, tc := range tests {
		assert.Equal(t, tc.expect, longestCommonStr(tc.s1, tc.s2))
	}
}
