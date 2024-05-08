#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

//  ToDo: Print maximum values.

void calculate_the_maximum(int n, int k) {

    //  Declaring counter.
    int i;

    //  Declaring second counter.
    int z;

    //  And operation
    int and_operation_result;

    //  Or operation
    int or_operation_result;

    //  Xor operation
    int x_or_operation_result;

    //  For loop to get all of the combinations
    //  of numbers.
    for (i = 1; i < n; i++)
    {
        for (z = i + 1; z <= n; z++)
        {
            // printf("%d %d",i,z);
            // printf("%s","\n");

            //  Running and operation against
            //  i and z.
            and_operation_result = i & z;

            //  Running or operation against
            //  i and z.
            or_operation_result = i | z;

            //  Running xor operation against
            //  i and z.
            x_or_operation_result = i ^ z;

            printf("%s","\n");
            printf("%d %d %d",
            and_operation_result,
            or_operation_result,
            x_or_operation_result);
        }
    }
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}