#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ITEMS 5

    struct stk {
        char symbol[5];
        int quantity;
        float price;
        struct stk *next;
    };

    struct stk *make_structure(void);
    void fill_structure(struct stk *a,int c);
    void show_structure(struct stk *a);

int main()
{

    struct stk *first;
    struct stk *current;
    int x;

    for(x=0;x<ITEMS;x++)
    {
        if(x==0)
        {
            first=make_structure();
            current=first;
        }
        else
        {
            current->next=make_structure();
            current=current->next;
        }
        fill_structure(current,x+1);
    }

    current->next=NULL;

    // output
    puts("Investment Portfolio");
    printf("Symbol\tShares\tPrice\tValue\n");
    current=first;
    while(current)
    {
        show_structure(current);
        current=current->next;
    }

    return 0;

}

//  allocate new structure
struct stk *make_structure(void)
{
    struct stk *a;

    a=(struct stk *)malloc(sizeof(struct stk) * 1);
    if(a == NULL)
    {
        puts("Some kind of malloc error");
        exit(1);
    }

    return(a);
}

void fill_structure(struct stk *a, int c)
{
    printf("Item #%d/%d:\n",c,ITEMS);
    printf("Stock Symbol: ");
    scanf("%s",a->symbol);
    printf("Number of shares: ");
    scanf("%d",&a->quantity);
    printf("Share price: ");
    scanf("%f",&a->price);
}

//  output the structure
void show_structure(struct stk *a)
{
    printf("%-6s\t%5d\t%.2f\t%.2f\n",\
    a->symbol,
    a->quantity,
    a->price,
    a->quantity*a->price);
}