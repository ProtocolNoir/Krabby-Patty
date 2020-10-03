#include <iostream>
using namespace std;
void check(int a[][3],int i,int j,int c)
{
	int m;
	for(m=1;m<a[0][2]+1;m++)
	{
		if(a[m][0]==i)
		{
			if(a[m][1]==j)
			{
			cout<<a[m][0]<<'\t'<<a[m][1]<<'\t'<<a[m][2]<<'\t'<<c<<"\n";
			break;
		    }
		}
	}
}
int main(){
int p,q,n;
cin>>p>>q>>n;
int i,j,c=1,k=1,l=0,t=0;
int a[n+1][3];
a[0][0]=p;
a[0][1]=q;
a[0][2]=n;
for(i=1;i<n+1;i++)
{
	cin>>a[i][0]>>a[i][1]>>a[i][2];
}
cin>>i>>j;
check(a,i,j,c);
t++;
while(t<(p*q))
{   
	for(l=0;l<k;l++)
	{
		i++;
		t++;
		c=1;
		check(a,i,j,c);	
	}
	for(l=0;l<k;l++)
	{
		j++;
		t++;
		c=2;
		check(a,i,j,c);
	}
	k=k+1;
	for(l=0;l<k;l++)
	{
		i--;
		t++;
		c=3;
		check(a,i,j,c);
	}
	for(l=0;l<k;l++)
	{
		j--;
		t++;
		c=4;
		check(a,i,j,c);
	}
	k=k+1;	
}
}
