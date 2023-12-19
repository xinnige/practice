package main

import (
	"fmt"
	"strconv"
	"log"
)

func encodeUtf8(s string) string {
	return strconv.QuoteToASCII(s)
}

func decodeUtf8(s string) string {
	str, err := strconv.Unquote(s)
	if err != nil {
		log.Printf("cannot decode %s, err: %v", s, err)
		return s
	}
	return str
}

func main() {
	raws := []string{"カタカナ", "👀👻😔🤪😀","中文字","abcdefg","room🤪😀1235","👀👻😔🤪😀｜⬆️《》"}

	for _, raw := range raws {
		encoded := encodeUtf8(raw)
		// dupencoded := encodeUtf8(encoded)
		decoded := decodeUtf8(encoded)
		// dupdecode := decodeUtf8(decoded)
		// fmt.Printf("%s -> %s (%s) -> %s -> %s\n",raw, encoded, dupencoded, decoded,dupdecode)
		fmt.Printf("%s -> %s -> %s\n",raw, encoded, decoded)
		fmt.Printf("%d -> %d -> %d\n", len(raw), len(encoded), len(decoded))
	}
}
