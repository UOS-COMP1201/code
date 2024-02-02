import java.lang.reflect.Array;
import java.util.*;
 
public class DFS
{
    
    int time;
    Map<String,Vertex> graph;
    public DFS(Map<String,Vertex> nodes ){
        graph=nodes;
        time=0;
    }
   
    /** DFS function **/
    public void search() 
    {
       // List<Vertex> order = new List(graph.values());
       ArrayList<Vertex> order=new ArrayList<Vertex>(graph.values());
       Collections.shuffle(order);
        for(Vertex u:order) {
        	if(u.color==Color.WHITE)
        		DFS_visit(u);
        	
        }
    }
    public void DFS_visit(Vertex u) {
    	u.color=Color.GRAY;
        time++;
        u.start=time;

    	for(Vertex v:u.getAdj()) {
    		if(v.color==Color.WHITE) {
    			v.p=u;
    			DFS_visit(v);
    		}
    	}
    	u.color=Color.BLACK;
        time++;
        u.end=time;
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

    for(Vertex u:map.values()) {
    	System.out.print(u.label);
        System.out.print(":");
    	for(Vertex v:u.getAdj()) {
    		System.out.print(v.label);
            System.out.print("-");
    	}
        System.out.println();
    }
    DFS dfs=new DFS(map);
    dfs.search();
    for(Vertex u:map.values()) 
         System.out.println(u.label+"="+u.start+" , "+u.end);
    
}
}
