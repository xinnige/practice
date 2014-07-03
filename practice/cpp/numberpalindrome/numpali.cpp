#include "stdio.h"
#include "stdlib.h"

int get_digit(int number){
    int digit = 1;
    while (number/digit > 10){
        digit *= 10;
    }
    printf("%d is %d digits.\n", number, digit);
    return digit;
}

void print_numbers(int digits, int number, int first, int last){
    printf("number %d, digits %d, first %d, last %d,\n",number,digits,first,last);
}

bool is_palindrome(int number)
{
    if (number < 0){
        return false;
    }
    int digits = get_digit(number);
    int first_digit = number/digits;
    int last_digit = number%10;
    print_numbers(digits,number,first_digit,last_digit);
    while (first_digit == last_digit){
       number = number%digits;
       number = number/10;
       digits /= 100;
       if (digits)
       first_digit = number/digits;
       last_digit = number%10;
       print_numbers(digits,number,first_digit,last_digit);
       if (number < 100){
           return true;
       }
    }
    return false;
}

int main(int argc, char* argv[])
{
    if (argc != 2){
        printf("invalid parameter number: %d\n", argc);
        return 0;
    }

    int number=atoi(argv[1]);
    printf("check if %d is palindrome...\n",number);
    bool is_palind = is_palindrome(number);
    if (is_palind){
         printf("%d is palindrome.\n", number);
    } else { 
         printf("%d is not palindrome.\n", number);
    }
    return 0;
}
