#include <iostream.h>
#include <conio.h>
#include <string.h>
void main()
{
  string str;
  cout<<"ENTER THE STRING";
  getline(cin,str);
  int i,j,l;
  l=strlen(str);
  for(i=0;j=l-1;i<j;i++,j--)
  {
    if(str.at(i)==str(j))
    f=1;
    break;
    
  }
  if(f==0)
  cout<<"NOT PALINDROME";
  else
  cout<<"PALINDROME";
}
