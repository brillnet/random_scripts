#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    /* Declaring two integers. */
	int a;
    int b;

    /* Declaring two floats. */
    float c;
    float d;

    /* Reading in two integer values. */
    scanf("%d %d", &a, &b);

    /* Reading in two floats. */
    scanf("%f %f", &c, &d);
    
    /* Getting sumOne */
    int sumOne = a + b;

    /* Getting diffOne */
    int diffOne = a - b;

    /* Printing the above two values */
    printf("%d %d", sumOne, diffOne);
    printf("\n");

    /* Getting sumTwo */
    float sumTwo = c + d;

    /* Getting diffTwo */
    float diffTwo = c - d;

    /* Printing the above two values */
    printf("%.1f %.1f", sumTwo, diffTwo);
    printf("\n");

    return 0;
}