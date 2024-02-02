import java.lang.reflect.Array;
import java.util.*;

public class Top
{
    
    int time;
    Map<String,Vertex> graph;
    LinkedList<Vertex> order;
    public Top(Map<String,Vertex> nodes ){
        graph=nodes;
        time=0;
        order=new LinkedList<Vertex>();
    }
   
    /** DFS function **/
    public void search() 
    {
       
       ArrayList<Vertex> order=new ArrayList<Vertex>(graph.values());
       /* random shuffle just to show that the topological ordering does not depend
        * on the order of processing of the vertices.
        */
       Collections.shuffle(order);
        for(Vertex u:order) {
        	if(u.color==Color.WHITE)
        		visit(u);
        	
        }
    }
    public void visit(Vertex u) {
    	u.color=Color.GRAY;
        time++;
        u.start=time;

    	for(Vertex v:u.getAdj()) {
    		if(v.color==Color.WHITE) {
    			v.p=u;
    			visit(v);
    		}
    	}
    	u.color=Color.BLACK;
        time++;
        u.end=time;
        order.addFirst(u);
    	//System.out.println(u.label);
    }

public static void main(String[] args) {
   
    
    Map<String,Vertex> map=new HashMap<String,Vertex>();
    map.put("a",new Vertex("a"));
    map.put("b",new Vertex("b"));
    map.put("c",new Vertex("c"));
    map.put("d",new Vertex("d"));
    map.put("e",new Vertex("e"));
    map.put("f",new Vertex("f"));
//edges
    map.get("a").addAdj(map.get("b"));
    //map.get("b").addAdj(map.get("a"));
    map.get("b").addAdj(map.get("c"));
    //map.get("b").addAdj(map.get("d"));
    //map.get("c").addAdj(map.get("b"));
    map.get("c").addAdj(map.get("d"));
    //map.get("c").addAdj(map.get("e"));
    //map.get("d").addAdj(map.get("b"));
    //map.get("d").addAdj(map.get("c"));
    map.get("e").addAdj(map.get("c"));
   // map.get("e").addAdj(map.get("f"));
    map.get("f").addAdj(map.get("e"));

    Top t=new Top(map);
    t.search();
    
    for(Vertex u:t.order)
        System.out.print(u.label+"-");
    System.out.println();
}
}
