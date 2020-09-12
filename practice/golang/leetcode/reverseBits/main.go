package main

import (
	"fmt"
)

func reverseBits(x uint32) uint32 {
	var r uint32
	for i := 0; i < 32; i++ {
		r = (r << 1) | (x & 1);
		x = x >> 1
	}
	return r;
}

// func reverseBits(x uint32) uint32 {
// 	x = (x&0x55555555)<<1 | (x&0xAAAAAAAA)>>1
//     x = (x&0x33333333)<<2 | (x&0xCCCCCCCC)>>2
//     x = (x&0x0F0F0F0F)<<4 | (x&0xF0F0F0F0)>>4
//     x = (x&0x00FF00FF)<<8 | (x&0xFF00FF00)>>8
// 	x= (x&0x0000FFFF)<<16 | (x&0xFFFF0000)>>16
// 	return x
// }

func main() {
	tests := []struct{
		input uint32
		expect uint32
	} {
		{43261596, 964176192},
		// {1,2147483648},
	}
	for _, tc := range tests{
		fmt.Printf("input=(%d), output=(%d), expect=(%d)\n", tc.input, reverseBits(tc.input), tc.expect)
	}
}