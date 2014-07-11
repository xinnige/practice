#include "stdlib.h"
#include "stdio.h"


int singleNumber(int A[], int n)
{
    int sum = 0;
    for (int i=0; i<n; i++){
        sum ^= A[i];
    }
    return sum;
}

int main()
{
    int a[]={-11,2,3,4,5,6,7,8,9,3,4,5,6,7,8,9,-11};
    int single = singleNumber(a,17);
    printf("%d\n",single);
    return 0;

}
