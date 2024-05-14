#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

//Complete the following function.
int total = 0;

// s(1) = 1
// s(2) = 2
// s(3) = 3
// s(4) = s(3) + s(2) + s(1) = 3 + 2 + 1
// s(5) = s(4) + s(3) + s(2) = 6 + 3 + 2

int find_nth_term(int n, int a, int b, int c) {

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

    //  Decreasing a b c by the appropriate amounts
    //  for next recursive call.
    a = n - 1;
    b = n - 2;
    c = n - 3;
    
    //  Getting total.
    total = a + b + c;

    //  Next recursive call.
    total = total + find_nth_term(n,a,b,c);
  }
  return total;
}

int main() {
    int n, a, b, c;
  
    // scanf("%d %d %d %d", &n, &a, &b, &c);

    n = 5;
    a = 1;
    b = 2;
    c = 3;

    int ans = find_nth_term(n, a, b, c);
 
    printf("%d", ans); 
    
    printf("%s","\n");

    return 0;
}