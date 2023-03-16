import sys, random


def parse(filename):
    #DIMACS format
    # lines starting with c are comments
    # after the comments there is a line p cnf nbvars nbclauses
    # followed by the clauses
    # each clause is a sequence of distinct non-null numbers between -nbvars and nbvars. The clause must end with a 0
    # a negative literal is the negation of a literal. A clause cannot contain a literal and its negation
    formula = []
    for line in open(filename):
        if line.startswith('c'): continue
        if line.startswith('p'):
            nbvars, nbclauses = line.split()[2:4]
            continue
        clause = [int(x) for x in line[:-2].split()]
        formula.append(clause)
    return formula, int(nbvars)

def print_formula(formula):
    for c in formula:
        print("(",end="")
        print(c,end="")
        print(")",end="")
    print()
def reduce_formula(formula, unit):
    # if a clause contains the unit literal remove the clause
    # if it contains the negation of the unit literal remove the negation from the clause
    modified = []
    for clause in formula:
        if unit in clause: continue
        if -unit in clause:
            c = [x for x in clause if x != -unit]
            # an empty clause means formula is unsatisfiable 
            if len(c) == 0: return -1
            modified.append(c)
        else:
            modified.append(clause)
    print_formula(modified)
    return modified


def count_variables(formula):
    counter = {}
    for clause in formula:
        for literal in clause:
            if literal in counter:
                counter[literal] += 1
            else:
                counter[literal] = 1
    return counter



def unit_propagation(formula):
    # iteratively propagate unit literals
    # when a unit literal is removed from clauses
    # it is possible to "uncover" other unit literals
    assignment = []
    unit_clauses = [c for c in formula if len(c) == 1]
    while len(unit_clauses) > 0:
        unit = unit_clauses[0]
        formula = reduce_formula(formula, unit[0])
        assignment += [unit[0]]
        if formula == -1:
            return -1, []
        if not formula:
            return formula, assignment
        unit_clauses = [c for c in formula if len(c) == 1]
    return formula, assignment


def choose_literal(formula):
    counter = count_variables(formula)

    # Either select the next variable randomly 
    # or as illustrated in class select the "next" variable
    
    #return random.choice(list(counter.keys()))
    return sorted(list(counter.keys()))[0]

def backtracking(formula, assignment):
   
    formula, unit_assignment = unit_propagation(formula)
    assignment = assignment +  unit_assignment
    if formula == - 1:
        return []
    if not formula:
        return assignment

    literal = choose_literal(formula)
    # reduce formula by setting chosen literal to true
    assignment = backtracking(reduce_formula(formula, literal), assignment + [literal])
    # if unsat backtrack and reduce by setting chosen literal to false
    if not assignment:
        assignment = backtracking(reduce_formula(formula, -literal), assignment + [-literal])
    return assignment


def main():
    formula, nbvars = parse('cnf.txt')
    # clauses, nvars = parse(sys.argv[1])
    assignment = backtracking(formula, [])
    if assignment:
        # add the literals that did not appear in the formula
        assignment += [x for x in range(1, nbvars + 1) if x not in assignment and -x not in assignment]
        assignment.sort(key=lambda x: abs(x))
        print ('SAT')
        print ('Truth assignment:' + ' '.join([str(x) for x in assignment]))
    else:
        print ('UNSAT')


if __name__ == '__main__':
    main()
