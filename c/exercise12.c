#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// s(1) = 1
// s(2) = 2
// s(3) = 3
// s(4) = s(3) + s(2) + s(1) = 3 + 2 + 1
// s(5) = s(4) + s(3) + s(2) = 6 + 3 + 2

int find_nth_term(int n, int a, int b, int c, int total) {

  // Dealing with end sum when a = 3, b = 2 and
  // c = 1.
  if (n < 4) {
    total = total + a + b + c;
  }
  else
  {
    // Decreasing n by 1. Ex) s(5) will be
    // s(4) on next call.
    n = n - 1;

    //  Getting totals for a,b and c using recursive calls.
    //  if statements will need be added here.
    // a = n - a;
    a = find_nth_term(n-a,a,b,c,total);
    b = n - b;                          
    c = n - c;                          
    
    //  Getting total.
    total = total + a + b + c;
  }
  
  //  Returning total
  return total;

}

int main() {
    int n, a, b, c;

    //Complete the following function.
    int total = 0;
  
    // scanf("%d %d %d %d", &n, &a, &b, &c);

    n = 5;
    a = 1;
    b = 2;
    c = 3;

    int ans = find_nth_term(n, a, b, c, total);
 
    printf("%d", ans); 
    
    printf("%s","\n");

    return 0;
}