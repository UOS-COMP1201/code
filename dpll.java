import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Vector;

final class Clause extends HashSet<Integer> {};

class dpll {
public static void main(String[] argv){
    Clause clause;
    HashSet<Clause> formula=new HashSet<>(); 
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
            clause=new Clause();

            // System.out.println("clause contains literals");
            // discard the 0 at the end of the line
            for(int i=0;i<literals.length-1;++i)
                 clause.add(Integer.valueOf(literals[i]));
            formula.add(clause);
        }
    reader.close();
   // printFormula(formula);
    //HashSet<Clause> modified=reduceFormula(formula, 1);
    HashSet<Clause> modified=unitPropagation(formula);
    System.out.println("\n Reduced formula");
    }
    catch(IOException e){
        e.printStackTrace();
    }
   
}
    public static void printFormula(HashSet<Clause> formula){
        for(Clause c: formula){
            System.out.print("(");
            for(Integer literal: c){
                System.out.print(literal+" ");
            }
            System.out.print(") ");
        }
        System.out.println("");
    }
    public static HashSet<Clause> 
            reduceFormula(HashSet<Clause> formula,Integer unit){
                HashSet<Clause> modified=new HashSet<>();
                
                for (Clause c:formula){
                        if(c.contains(unit)) continue;
                        else if (c.contains(-unit)){
                            /// don't forget to check for empty clauses
                            Clause clause=new Clause();
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
    private static Integer getElement(Clause c){
        for(Integer e:c)
                return e;
        return null;
    }
    public static HashSet<Clause> unitPropagation(HashSet<Clause> formula){
        Vector<Integer> unit_clauses=new Vector<>();
        for(Clause c:formula)
            if(c.size()==1)unit_clauses.add(getElement(c));
        while(unit_clauses.size()>0){
            Integer unit=unit_clauses.firstElement();
            formula=reduceFormula(formula,unit);
            printFormula(formula);

            if (formula==null) return null;
            unit_clauses.clear();
            for(Clause c:formula)
                if(c.size()==1)unit_clauses.add(getElement(c));  
                      
        }
        return formula;

    }
}
