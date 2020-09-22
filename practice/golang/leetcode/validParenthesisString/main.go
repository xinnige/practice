package main


import (
    "fmt"
)

func checker(leftcnt int, s string) bool {
    for i, c := range s {
        if c == '(' {
           leftcnt++
        } else if c == ')' {
           leftcnt--
        } else if c == '*' {
           if i == len(s)-1 {
                return leftcnt <= 1
           }
           return checker(leftcnt, s[i+1: len(s)]) || checker(leftcnt+1, s[i+1:len(s)]) || checker(leftcnt-1, s[i+1:len(s)])
        } else {
            return false
        }
        if leftcnt < 0 {
            return false
        }
    }
    return leftcnt == 0
}

func checkValidString(s string) bool {
    return checker(0, s)
}

func main(){
    tests := []struct{
        s string
        expect bool
    }{
        {"", true},
        {"*", true},
        {"{", false},
        {"}", false},
        {"{}", true},
        {"{{*}", true},
        {"{*}}", true},
        {"{*}", true},
        {"{}}", false},
        {"{}}}", false},
        {"}*", false},
        {"}{", false},
        {"{*", true},
        {"**", true},
        {"***", true},
        {"{}{}", true},
        {"{{{}}}", true},
        {"{{{*}}}", true},
    }
    for _, tc := range tests {
        fmt.Printf("%s should be %t:  %t\n", tc.s, tc.expect ,checkValidString(tc.s))
    }
}
