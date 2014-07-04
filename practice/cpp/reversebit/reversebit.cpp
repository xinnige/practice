#include "stdio.h"
#include "stdlib.h"

void print_binary(unsigned int number)
{
    char binary[32];
    for (unsigned int i=1; i<=32;i++){
        if (number & 1){
            binary[32-i]='1';
        }
        else{
            binary[32-i]='0';
        }
        number >>= 1;
    }
    printf("%s\n",binary);
}

unsigned int swapBits(unsigned int x,unsigned int i, unsigned int j)
{
    unsigned int lowbit = ((x >> i) & 1);
    unsigned int highbit = ((x >> j) & 1);
    printf("i:%u,j:%u,lowbit:%u,highbit:%u.\n",i,j, lowbit, highbit);
    if (lowbit ^ highbit){
        x ^= ((1<<i)|(1<<j));
    }
    return x;
}

unsigned int reversebit(unsigned int number)
{
    unsigned int n = sizeof(number)*8;
    printf("Sizeof %u: %u,\n",number,n);
    for  (unsigned int i = 0; i < n/2; i++){
        number = swapBits(number,i,n-i-1);
    }
    return number;
}

unsigned int reversebit2(unsigned int number)
{
    //assert(sizeof(number)==4);
    number = ((number&0x55555555) << 1)| ((number&0xaaaaaaaa)>>1);
    number = ((number&0x33333333) << 2)| ((number&0xcccccccc)>>2);
    number = ((number&0x0f0f0f0f) << 4)| ((number&0xf0f0f0f0)>>4);
    number = ((number&0x00ff00ff) << 8)| ((number&0xff00ff00)>>8);
    number = ((number&0x0000ffff) << 16)| ((number&0xffff0000)>>16);
    return number;  
}

int main(int argc, char* argv[])
{
    if (argc != 2){
        printf("Invalid Parameter number:%d.\n",argc);
        return 0;
    }
    unsigned int number = atoi(argv[1]);
    printf("Reversing bits of ");
    print_binary(number);
    
    unsigned int reversed = reversebit2(number);
    printf("After reversing ");
    print_binary(reversed);

    return 0;
}
