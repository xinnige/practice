package cre2

import (
	"os"
	"testing"

	"github.com/stretchr/testify/require"
)

var (
	patternUnsupport = `(?=abc)123??????xxx------`
	patternSimple    = `/[0-9]+`

	textUnmatch = `abcdefgHIJKLMN!@#$%^&`
	textSimple  = `/v1/api/resource/pbsc/9827651627391/9`
	textSimple2 = `/v1/api/resource/pbsc/9827651627391/9?query=30288c`
)

func TestMain(m *testing.M) {
	os.Exit(m.Run())
}

func TestCompile(t *testing.T) {
	t.Run("TestCompile", func(t *testing.T) {
		var (
			re  *Regexp
			err error
		)

		re, err = Compile(patternSimple)
		require.Nil(t, err)
		require.NotNil(t, re)
		re.Close()

		re, err = Compile(patternUnsupport)
		require.NotNil(t, err)
		require.Nil(t, re)
	})
}

func TestReplaceAll(t *testing.T) {
	t.Run("TestReplaceAll", func(t *testing.T) {
		re := MustCompile(patternSimple)
		defer re.Close()
		replaced := re.ReplaceAll([]byte(textSimple), []byte("/:id"))
		require.Equal(t, "/v1/api/resource/pbsc/:id/:id", string(replaced), string(replaced))
	})
}

func TestReplaceAllString(t *testing.T) {
	t.Run("TestReplaceAllString", func(t *testing.T) {
		re := MustCompile(patternSimple)
		defer re.Close()
		replaced := re.ReplaceAllString(textSimple, "/:id")
		require.Equal(t, "/v1/api/resource/pbsc/:id/:id", replaced, replaced)
	})
}

func TestMatchString(t *testing.T) {
	t.Run("TestMatchString", func(t *testing.T) {
		re := MustCompile(patternSimple)
		defer re.Close()
		matched := re.MatchString(textSimple)
		require.Equal(t, true, matched)

		nomatch := re.MatchString(textUnmatch)
		require.Equal(t, false, nomatch)
	})
}

func TestFindAllString(t *testing.T) {
	t.Run("TestFindAllString", func(t *testing.T) {
		re := MustCompile(patternSimple)
		defer re.Close()
		matched := re.FindAllString(textSimple2, -1)
		require.Equal(t, []string{"/9827651627391", "/9"}, matched)
	})
}
