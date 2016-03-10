#include "stdlib.h"
#include "stdio.h"
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int tail = 0;  //points to 1 past the last non-zero entry
        for (int i=0; i<nums.size(); i++) {
            if (nums[i] == 0)
                continue;

            // if ((tail++) != i) {
            tail++;
            if (0 != i) {
                nums[tail-1] = nums [i]; //Overwrite since there are 0s in the middle
                nums[i] = 0;
            }
        }
        print(nums);
    }
 
    void print(vector<int>& nums){
		for (int i = 0; i< nums.size();i++){
            cout << nums[i] << " ";
        }
		cout << endl;
	}
};


int main()
{
    Solution sol;
    int nums[] = {0,1,0,2,0,3,0,4,0,5};
    int nums1[] = {0,1,2,3,4,5,6,7};
    int nums2[] = {};
    int nums3[] = {0};
    int nums4[] = {1};
    int nums5[] = {1,2,3};
    int nums6[] = {1,2,3,0};
    int nums7[] = {1,2,0,0,3,4,0,0,0,0,0,5,0};
    int nums8[] = {1,2,3,4,5,0,0,0,0,0};
    int nums9[] = {0,4,2,3,1,1,0,9,0,0,0};
    vector<int> number(nums, nums + sizeof(nums)/sizeof(int));	
    vector<int> number1(nums1, nums1 + sizeof(nums1)/sizeof(int));	
    vector<int> number2(nums2, nums2 + sizeof(nums2)/sizeof(int));	
    vector<int> number3(nums3, nums3 + sizeof(nums3)/sizeof(int));	
    vector<int> number4(nums4, nums4 + sizeof(nums4)/sizeof(int));	
    vector<int> number5(nums5, nums5 + sizeof(nums5)/sizeof(int));	
    vector<int> number6(nums6, nums6 + sizeof(nums6)/sizeof(int));	
    vector<int> number7(nums7, nums7 + sizeof(nums7)/sizeof(int));	
    vector<int> number8(nums8, nums8 + sizeof(nums8)/sizeof(int));	
    vector<int> number9(nums9, nums9 + sizeof(nums9)/sizeof(int));	
    sol.moveZeroes(number);
    sol.moveZeroes(number1);
    sol.moveZeroes(number2);
    sol.moveZeroes(number3);
    sol.moveZeroes(number4);
    sol.moveZeroes(number5);
    sol.moveZeroes(number6);
    sol.moveZeroes(number7);
    sol.moveZeroes(number8);
    sol.moveZeroes(number9);
}
