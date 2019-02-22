z=input().split()
z=list(map(int,z))
num=z[0]/2
p=z[1]
q=z[2]
d=int(z[0]/p)
e=int(z[0]/q)
c=0
if(z[0]%2==0):
  for i in range(1,d):
    for j in range(1,e):
      if((p*i)+(q*j)==num):
        c=1
if(c==1):
  print('YES')
else:
  print('NO')
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
