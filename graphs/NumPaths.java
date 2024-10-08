import java.util.*;



public class NumPaths{

static int bfsVisit(BfsVertex source,BfsVertex dest,int m) {
	/* BFS visits all nodes at distance d before visiting
	* any node at d+1. So we exit the loop once d>m
    */
	int count=0;
	Queue<BfsVertex> q=new LinkedList<BfsVertex>();
	q.add(source);
	while(!q.isEmpty()) {
		BfsVertex u=q.remove();
		Iterator<BfsVertex> itr=u.getAdj().iterator();
		/* once the frontier is at a distance
		 * greater than m exit the loop
		 */  
			/* we might have multiple copies
			 * of the destination so we
			* compare the labels NOT the objects 
			*/
		if(u.d==m){
			if(u.label.equals(dest.label))
				count++;
			continue;
		}
			
		while(itr.hasNext()) {
			BfsVertex v=itr.next();
			//make a copy of v
			BfsVertex copy=new BfsVertex(v);
			copy.d=u.d+1;
			q.add(copy);
					
		}
	}
		return count;	
}



public static void main(String[] args){
			// total number of nodes in the graph
	int n = 5;
	//a=0,b=1,c=2,d=3,e=4		
	//BfsGraph g=new BfsGraph();
	BfsVertex[] nodes=new BfsVertex[n];
	for(int i=0;i<n;++i)
		nodes[i]=new BfsVertex(Integer.toString(i));
	//a	
	nodes[0].addAdj(nodes[1]);nodes[0].addAdj(nodes[2]);
	//b
	nodes[1].addAdj(nodes[3]);nodes[1].addAdj(nodes[4]);
	//c
	nodes[2].addAdj(nodes[1]);nodes[2].addAdj(nodes[3]);
	//d
	nodes[3].addAdj(nodes[4]);
	
			

	int m = 3;

			// Do modified BFS traversal from the source vertex 
	System.out.println(bfsVisit(nodes[0],nodes[4],m));
	}
}

class BfsVertex{
	//boolean visited; not needed
	//predecessor
	//BfsVertex p;not needed
	int d=0;
	String label;
	LinkedList<BfsVertex> adj;
	
	public BfsVertex(String label) {
		this.label=label;
		adj=new LinkedList<BfsVertex>();
	}
	/* copy constructor to clone a vertex
	 * so that we can maintain multiple
	 * copies of the same node corresponding
	 * to different paths used to reach it
	 */
	public BfsVertex(BfsVertex rhs) {
		this.label=rhs.label;
		adj=rhs.adj;
	}
	void addAdj(BfsVertex v) {
		adj.add(v);
	}
	LinkedList<BfsVertex> getAdj(){
		return adj;
	}
}
class BfsGraph{
	int n;
	LinkedList<BfsVertex> vertices;

	public BfsGraph() {
		n=0;
		vertices=new LinkedList<BfsVertex>();
	}
	void addVertex(BfsVertex v) {
		n++;
		vertices.add(v);
	}
	LinkedList<BfsVertex> getVertices(){
	    
		return vertices;
	}

}

