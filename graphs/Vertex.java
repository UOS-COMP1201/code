import java.util.*;
enum Color{
	WHITE,
	GRAY,
	BLACK
}
public class Vertex{
	Color color=Color.WHITE;
    int start,end;
	//predecessor
	Vertex p=null;
	String label;
	LinkedList<Vertex> adj;
	
	public Vertex(String label) {
		this.label=label;
		adj=new LinkedList<Vertex>();
	}
	void addAdj(Vertex v) {
		adj.add(v);
	}
	LinkedList<Vertex> getAdj(){
		return adj;
    }
}