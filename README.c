#include <stdio.h>
int main()
{
    int i, s, r, k=0, count = 0, c = 0;
 printf("Enter number of rows: ");
    scanf("%d",&r);
 for(i=1; i<=r; ++i)
    {
        for(s=1; s <= r-i; ++s)
        {
            printf("  ");
            ++count;
        }

        while(k != 2*i-1)
        {
            if (count <= r-1)
            {
                printf("%d ", i+k);
                ++count;
            }
            else
            {
                ++c;
                printf("%d ", (i+k-2*c));
            }
            ++k;
        }
        c= count = k = 0;
        printf("\n");
    }
    return 0;
}
