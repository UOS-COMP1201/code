import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Vector;
class dpll {
public static void main(String[] argv){
    HashSet<Integer> clause;
    HashSet<HashSet<Integer> > formula=new HashSet<>(); 
    int nbvars,nbclauses;
    try{
    BufferedReader reader=new BufferedReader(new FileReader("cnf.txt"));
        String line;
        while((line=reader.readLine()) !=null){
            if (line.startsWith("c"))
                continue;
            if (line.startsWith("p cnf")){
                String[] tokens=line.split(" ");
                nbvars=Integer.valueOf(tokens[2]);
                nbclauses=Integer.valueOf(tokens[3]);
                System.out.println("number of clauses="+nbclauses+"  number of variables="+nbvars);
                continue;
            }
            String[] literals=line.split(" ");
            clause=new HashSet<>();

            // System.out.println("clause contains literals");
            // discard the 0 at the end of the line
            for(int i=0;i<literals.length-1;++i)
                 clause.add(Integer.valueOf(literals[i]));
            formula.add(clause);
        }
    reader.close();
    printFormula(formula);
    HashSet<HashSet<Integer>> modified=reduceFormula(formula, 1);
    System.out.println("\n Reduced formula");
    printFormula(modified);
    }
    catch(IOException e){
        e.printStackTrace();
    }
   
}
    public static void printFormula(HashSet<HashSet<Integer>> formula){
        for(HashSet<Integer> clause: formula){
            System.out.print("(");
            for(Integer literal: clause){
                System.out.print(literal+" ");
            }
            System.out.print(") ");
        }
        System.out.println("");
    }
    public static HashSet<HashSet<Integer>> 
            reduceFormula(HashSet<HashSet<Integer>> formula,Integer unit){
                HashSet<HashSet<Integer>> modified=new HashSet<>();
                
                for (HashSet<Integer> c:formula){
                        if(c.contains(unit)) continue;
                        else if (c.contains(-unit)){
                            /// don't forget to check for empty clauses
                            HashSet<Integer> clause=new HashSet<>();
                            for(Integer literal: c)
                                if (literal!=-unit)
                                    clause.add(literal);
                            if (clause.isEmpty())
                                 return null;
                            modified.add(clause);
                        }
                        else 
                            modified.add(c);
                }
                
      
                
    return modified;
    }
    private static Integer getUnitElement(HashSet<Integer> clause){
        for(Integer e:clause)
                return e;
        return null;
    }
    public static void unitPropagation(HashSet<HashSet<Integer>> formula){
        Vector<Integer> unit_clauses=new Vector<>();
        for(HashSet<Integer> c:formula)
            if(c.size()==1)unit_clauses.add(getUnitElement(c));
        while(unit_clauses.size()>0){
            Integer unit=unit_clauses.remove(0);
            formula=reduceFormula(formula,unit);
            if (formula==null) return;
            unit_clauses=new Vector<>();
            for(HashSet<Integer> c:formula)
                if(c.size()==1)unit_clauses.add(getUnitElement(c));            
        }

    }
}