import java.lang.reflect.Array;
import java.util.*;
 /* Kosaraju strongly connected components */
public class SCC
{
    
    int time;
    Map<String,Vertex> graph;
    boolean print;
    public SCC(Map<String,Vertex> nodes,boolean print){
        graph=nodes;
        time=0;
        this.print=print;
    }
   
    /** DFS function **/
    public void search() 
    {
       
        ArrayList<Vertex> order=new ArrayList<Vertex>(graph.values());
        order.sort(new Order(true));
        for(Vertex u:order){
            
        	if(u.color==Color.WHITE){
                if (print) System.out.println("new component");
        		    visit(u);
            }
        	
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
        if(print)
        	System.out.println(u.label);
    }
    public Map<String,Vertex> transpose() {
        /* transpose the graph, i.e. "flip" the direction of edges
         * and keep the "end" times of the vertices.
         */
        Map<String,Vertex> trans=new HashMap<String,Vertex>();
        // create a copy of the vertices with same end times.
        for(String s: graph.keySet()){
            Vertex u=new Vertex(s);
            u.end=graph.get(u.label).end;
            trans.put(s,u);
        }
        for(Vertex u:graph.values()) {
            for(Vertex v:u.getAdj()) {
                trans.get(v.label).addAdj(trans.get(u.label));
            }
        }
        return trans;
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
    ///
    map.get("d").addAdj(map.get("b"));

   /* first DFS  */
    SCC dfs=new SCC(map,false);
    dfs.search();
    /* transpose the graph and keep the end times from DFS */
    var t=dfs.transpose();
    /* second DFS in descending order of finishing time */
    SCC dfs2=new SCC(t,true);
    dfs2.search();
    
   
}
}
class Order implements Comparator<Vertex>{
    boolean reverse;
    public Order(boolean reverse){
        this.reverse=reverse;
    }
    public int compare(Vertex a,Vertex b){
        if(reverse)
            return b.end-a.end;
        else 
            return a.end-b.end;
    }
}
