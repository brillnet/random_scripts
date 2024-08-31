#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    
    //  Creating integer variable that will hold the size of the array
    //  read in from stdin.
    int n;
    
    //  Initialising total variable to 0.
    int total = 0;
    
    //  Getting the size of the array from stdin
    scanf("%d", &n); 
    
    // Creating dynamic integer array.
    int *arr = (int*)malloc(n * sizeof(int));
    
    //  For loop to read in integers from stdin and store them
    //  in array.
    for(int i=0; i<n; i++)  
    {  
        scanf("%d", &arr[i]);  // Read the input and store it in the array
    }
    
    //  For loop getting getting the total of every value
    //  in the array.
    for(int i=0; i<n; i++)  
    {  
        total = arr[i] + total;
    }
    
    //  Printing total
     printf("%d",total);
 
    return 0;
}
