import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Vector;
import java.util.HashMap;
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
    // HashMap<Integer,Integer> pure=countLiterals(formula);
    // System.out.println(pure);
    Vector<Integer> a=backtrack(formula,new Vector<Integer>());
    System.out.println(a);
    //HashSet<Clause> modified=reduceFormula(formula, 1);
    //HashSet<Clause> modified=unitPropagation(formula);
    //System.out.println("\n Reduced formula");
    }
    catch(IOException e){
        e.printStackTrace();
    }
   
}

    public static Vector<Integer> backtrack(HashSet<Clause> formula,Vector<Integer> assignment){
      
        formula=pure_literals(formula,assignment);
        formula=unitPropagation(formula,assignment);

        if(formula==null) return new Vector<Integer>();

        return assignment;
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
    public static HashSet<Clause> unitPropagation(HashSet<Clause> formula,Vector<Integer> assignment){
        Vector<Integer> unit_clauses=new Vector<>();
        for(Clause c:formula)
            if(c.size()==1)unit_clauses.add(getElement(c));
        while(unit_clauses.size()>0){
            Integer unit=unit_clauses.firstElement();
            assignment.add(unit);
            formula=reduceFormula(formula,unit);
            printFormula(formula);

            if (formula==null) return null;
            unit_clauses.clear();
            for(Clause c:formula)
                if(c.size()==1)unit_clauses.add(getElement(c));  
                      
        }
        return formula;

    }
    public static HashMap<Integer,Integer>
            countLiterals(HashSet<Clause> formula){
                HashMap<Integer,Integer> counter=new HashMap<>();
                for(Clause c:formula){
                    for(Integer literal: c){
                        if (counter.containsKey(literal))
                            counter.put(literal,counter.get(literal)+1);
                        else
                            counter.put(literal,1);
                    }
                }
                return counter;
            }

    public static HashSet<Clause> pure_literals(HashSet<Clause> formula,Vector<Integer> assignment){
        HashMap<Integer,Integer> counter=countLiterals(formula);
        Vector<Integer> pures=new Vector<>();
        counter.forEach((k,v)->{
            if (!counter.containsKey(-k)) pures.add(k);
        });
        for(Integer pure:pures){
            assignment.add(pure);
            formula=reduceFormula(formula,pure);
        }
        return formula;
    }
    
}