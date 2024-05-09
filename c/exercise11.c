#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

//  ToDo: Print maximum values.

int max_and_operator = 0;
int max_or_operation_result = 0;
int max_x_or_operation_result = 0;

// Setting the type operation char
char operation_and = 'a';
char operation_or = 'o';
char operation_x = 'x';

void set_max_operation_result(int n, char o) {



    if (n < 4)
    {
        if (n > max_and_operator)
        {
             if (strcmp(o, operation_and)) {
                max_and_operator = n;
             }
        }
    }
}

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

    //  Creating char value that will the type
    //  of operation either a,o,x
    char operation;

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
            
            set_max_operation_result(and_operation_result, operation);

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