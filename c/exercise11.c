#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

//  ToDo: Print maximum values.
int max_and_operation_result = 0;
int max_or_operation_result = 0;
int max_x_or_operation_result = 0;

// Setting the type operation char
char operation_and = 'a';
char operation_or = 'o';
char operation_x = 'x';


void set_max_operation_result(int n, char o, int k) {
    if (n < k)
    {
        if (o == operation_and) {
            if (n > max_and_operation_result)
            {
                max_and_operation_result = n;
            }
        }

        if (o == operation_or) {
            if (n > max_or_operation_result)
            {
                max_or_operation_result = n;
            }
        }

        if (o == operation_x) {
            if (n > max_x_or_operation_result)
            {
                max_x_or_operation_result = n;
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
            //  Running and operation against
            //  i and z.
            and_operation_result = i & z;
            
            //  Setting operation type
            operation = 'a';
            set_max_operation_result(and_operation_result, operation, k);

            //  Running or operation against
            //  i and z.
            or_operation_result = i | z;
            
            //  Setting operation type
            operation = 'o';
            set_max_operation_result(or_operation_result, operation, k);

            //  Running xor operation against
            //  i and z.
            x_or_operation_result = i ^ z;
            
            //  Setting operation type
            operation = 'x';
            set_max_operation_result(x_or_operation_result, operation, k);
        }
    }
}

int main() {
    int n, k;
    n = 5;
    k = 4;
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);

    printf("%d",max_and_operation_result);
    printf("%s","\n");
    printf("%d",max_or_operation_result);
    printf("%s","\n");
    printf("%d",max_x_or_operation_result);
    printf("%s","\n");

    return 0;
}