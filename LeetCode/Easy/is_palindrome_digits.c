#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>

int reverse(long x){
    x = labs(x);

    if ((int)x != x)
        return 0;

    bool lastIsZero = 0;
    
    long int temp = 0;
    int noOfDigits = 0;
    long int digitChecker = x;
    while (digitChecker > 0)
    {
        digitChecker /= 10;
        noOfDigits++;
    }
    noOfDigits--;
    while (x > 0){
        int digit = x%10;
        x = x/10;
        temp += (long int)pow(10, noOfDigits) * digit;
        if (temp != (int)temp)
            return 0;
        noOfDigits--;
    }
    return temp;
}

bool isPalindrome(int x){
    bool sign = x < 0? 1 : 0;
    if (sign)
        return false;
    else{
        int rev = reverse(x);
        return (rev == x);
    }
}

int main(){
    printf(isPalindrome(101)? "true" : "false");
}
