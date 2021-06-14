import javax.swing.*;
class tra
{
public static void main(String xyz[])
{
int[][] ar=new int[10][10];
int i,j,temp;
for(i=0;i<3;i++)
{
for(j=0;j<3;j++)
{
ar[i][j]=Integer.parseInt(JOptionPane.showInputDialog("ENTER A NUMBER"));
}
}
for(i=0;i<3;i++)
{
  for(j=0;j<3;j++)
  {
  System.out.print(ar[i][j]+" ");
  }
  System.out.println();
}
System.out.println();

for(i=0;i<3;i++)
{
  for(j=0;j<3;j++)
  {
  System.out.print(ar[j][i]+" ");
  }
  System.out.println();
}
}
}
