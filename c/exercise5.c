#include <stdio.h>
/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a, int b, int c, int d)
{
    /*  Putting arguments sent into a list of integers. */
    int num_arr[] = {a,b,c,d};

    /* Initializing counter as int */
    int i;

    /* Getting size of array */
    int size_of_arr = sizeof(num_arr) / sizeof(num_arr[0]);

    /* Getting max value in array */
    int max_value = num_arr[0];

    /* For loop to find the largest value in array. */
    for (i = 0; i < size_of_arr; i++) {
        
        if (num_arr[i] > max_value) {
            max_value = num_arr[i];
        } 

    }

    return max_value;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}