import java.util.*;

public class Lists {

 public static void main(String[] args){

double startTime = System.nanoTime();

/* ArrayList */

  List<Integer> list=new ArrayList<>();
  for(int i=0;i<10000000;i++)
     list.add(i);

   for(int i=0;i<1000;i++)
       list.add(0,-1);
double endTime = System.nanoTime();

double duration = (endTime - startTime)/1000000;
System.out.println(duration);


/** LinkedList **/

List<Integer> l_list=new LinkedList<>();
startTime = System.nanoTime();
  for(int i=0;i<10000000;i++)
     l_list.add(i);

   for(int i=0;i<1000;i++)
       l_list.add(0,-1);

endTime = System.nanoTime();
duration = (endTime - startTime)/1000000;
System.out.println(duration);
}
}
