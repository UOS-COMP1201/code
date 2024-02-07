import java.io.*;
import java.util.*;
import java.util.concurrent.ConcurrentSkipListSet;
import java.lang.*;
/** performance comparison of various linear lists in java */
public class Lists {

 public static void main(String[] args){
double startTime, endTime, duration;

/**** insertion in front of the list ******/
/******************************************/
System.out.println("Insertion in front of the list");
/* ArrayList */
startTime = System.nanoTime();
  List<Integer> list=new ArrayList<>();
  for(int i=0;i<10000000;i++)
     list.add(i);

   for(int i=0;i<1000;i++)
       list.add(0,-1);
endTime = System.nanoTime();
duration = (endTime - startTime)/1000000;
System.out.println("Duration for ArrayList is "+duration+" ms");


/** LinkedList **/

List<Integer> l_list=new LinkedList<>();
startTime = System.nanoTime();
  for(int i=0;i<10000000;i++)
     l_list.add(i);

   for(int i=0;i<1000;i++)
       l_list.add(0,-1);

endTime = System.nanoTime();
duration = (endTime - startTime)/1000000;
System.out.println("Duration for LinkedList is "+duration+" ms");


/******** Element at ***************/
/*********************************/
System.out.println("---------------------------------");
System.out.println("Element at ");
startTime = System.nanoTime();
for(int i=0;i<1000;i++)
    list.get(i);
endTime = System.nanoTime();
duration = (endTime - startTime)/1000000;
System.out.println("Duration for ArrayList is "+duration+" ms");

for(int i=0;i<1000;i++)
    l_list.get(i);



System.out.println("---------------------------------");
System.out.println("Searching ");
/**** searching *************/
/****************************/
/* ArrayList */
List<String> slist=new ArrayList<>();
List<String> sl_list=new LinkedList<>();
ConcurrentSkipListSet<String> skip_list=new ConcurrentSkipListSet<>();
try {
		File file=new File("words.txt");
		Scanner input=new Scanner(file);

		int count=20;
		while(input.hasNextLine()) {
			String line=input.nextLine();
			for(int i=0;i<count;i++) {
			   slist.add(line+Integer.toString(i));
          sl_list.add(line+Integer.toString(i));
          skip_list.add(line+Integer.toString(i));
      }
    }
		input.close();
		
		}
		catch(Exception e) {
			System.out.println("Exception"+e.getMessage());
		}
  /* ArrayList */
    startTime = System.nanoTime();
    for(int i=0;i<200;i++)
       slist.contains("parvenue"+Integer.toString(i));
    endTime = System.nanoTime();
    duration = (endTime - startTime)/1000000;
    System.out.println("Duration for ArrayList is "+duration+" ms");
    /*  LinkedList */
    startTime = System.nanoTime();
    for(int i=0;i<200;i++)
       sl_list.contains("parvenue"+Integer.toString(i));
    endTime = System.nanoTime();
    duration = (endTime - startTime)/1000000;
    System.out.println("Duration for LinkedList is "+duration+" ms");
     /*  SkipList */
     startTime = System.nanoTime();
     for(int i=0;i<200;i++)
        skip_list.contains("parvenue"+Integer.toString(i));
     endTime = System.nanoTime();
     duration = (endTime - startTime)/1000000;
     System.out.println("Duration for SkipList is "+duration+" ms");
  }
  
}

