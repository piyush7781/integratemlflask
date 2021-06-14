import javax.swing.*;
class sta
{
public sta()
{
int stack[]=new int[5];
int i,top=-1;
}
public void push()
{
if(top==4)
JOptionPane.showMessageDialog(null,"OVERFLOW");
else
{
top++;
int m=Integer.parseInt(JOptionPane.showInputDialog("ENTER A NUMBER"));
stack[top]=m;
}
}
public void show()
{
for(i=0;i<=top;i++)
{
System.out.print(stack[i]+" ");
}
System.out.println();
}
public void pop()
{
if(top==-1)
JOptionPane.showMessageDialog(null,"EMPTY");
else
{
top--;
}
public static void main(String arg[])
{
int ch;
sta s1=new sta();
switch(ch)
{
case 1:s1.push();
case 2:s1.show();
case 3:s1.pop();
default:JOptionPane.showMessageDialog(null,"WRONG CHOICE");
}
}
}