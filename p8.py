#include<stdio.h>
int main()
{
int l,a,i,cd;
printf("Enter twop integers:");
scanf("%d%d",&l,&a);
for(i=1; i <= l && i <= a; ++i)
    {       
        if(l%i==0 && a%i==0)       
            gcd = i;           
    }
   printf("G.C.D of %d and %d is %d", l, a, cd);
    return 0;
