from classify import *
import math
from subprocess import call
import os
import csp


##
## CSP portion of lab 4.
##
from csp import BinaryConstraint, CSP, CSPState, Variable,\
    basic_constraint_checker, solve_csp_problem

# Implement basic forward checking on the CSPState see csp.py
def forward_checking(state, verbose=False):
    # Before running Forward checking we must ensure
    # that constraints are okay for this state.
    basic = basic_constraint_checker(state, verbose)
    if not basic:
        return False
    
    # Add your forward checking logic here.
    var = state.get_current_variable()
    value = None
    if not var: return True
    value = var.get_assigned_value()
    for constraint in state.get_constraints_by_name(var.get_name()):
        #print(state)
        my_constraint1=constraint.get_variable_i_name()
        my_constraint2=constraint.get_variable_j_name()
        my_constraint1_var=state.get_variable_by_name(my_constraint1)
        my_constraint2_var=state.get_variable_by_name(my_constraint2)
        my_constraint1_val=my_constraint1_var.get_assigned_value()
        my_constraint2_val=my_constraint2_var.get_assigned_value()
        if my_constraint1_var!=var:
            my_constraint_var=my_constraint1_var
        else:
            my_constraint_var=my_constraint2_var
        #my_constraint_var=state.get_variable_by_name(constraint.get_variable_i_name() if constraint.get_variable_i_name() != var.get_name() else constraint.get_variable_j_name())        
        for varvalue in my_constraint_var.get_domain():
            if constraint.check(state,value,varvalue)==False:
                    #print(type(my_constraint_var.get_domain()))
                my_constraint_var.reduce_domain(varvalue)
                    #print(my_constraint_var.get_domain())
            if my_constraint_var.domain_size()==0:
                return False
                    
                
        
    return True
#exec("moose_csp.py dfs")
#solve_csp_problem(moose_csp_problem,forward_checking)
#print(forward_checing(solve_csp_problem))
# Now Implement forward checking + (constraint) propagation through
# singleton domains.
def forward_checking_prop_singleton(state, verbose=False):
    # Run forward checking first.
    fc_checker = forward_checking(state, verbose)
    if not fc_checker:
        return False
    singleton_list=list()
    visited=list()
    # Add your propagate singleton logic here.
    for allvar in state.get_all_variables():
        if allvar.domain_size()==1:
            singleton_list.append(allvar)
    while singleton_list:
        singleton_var=singleton_list.pop()
        visited.append(singleton_var)
        for constraint in state.get_constraints_by_name(singleton_var.get_name()):
            my_constraint1=constraint.get_variable_i_name()
            my_constraint2=constraint.get_variable_j_name()
            my_constraint1_var=state.get_variable_by_name(my_constraint1)
            my_constraint2_var=state.get_variable_by_name(my_constraint2)
            my_constraint1_val=my_constraint1_var.get_assigned_value()
            my_constraint2_val=my_constraint2_var.get_assigned_value()
            if my_constraint1_var!=singleton_var:
                my_constraint_var=my_constraint1_var
            else:
                my_constraint_var=my_constraint2_var
            if singleton_var.domain_size() == 1:
                singe_value = singleton_var.get_domain()[0]    
            for varvalue in my_constraint_var.get_domain():
                if constraint.check(state,singe_value,varvalue)==False:
                    #print(type(my_constraint_var.get_domain()))
                    my_constraint_var.reduce_domain(varvalue)
                    #print(my_constraint_var.get_domain())
                if my_constraint_var.domain_size()==0:
                    return False
        for allvar1 in state.get_all_variables():
            if allvar1.domain_size()==1:
                if allvar1 not in visited and allvar1 not in singleton_list:
                    singleton_list.append(allvar1)
    #print(state)        
    return True        
#solve_csp_problem(map_coloring_csp_problem,forward_checking_prop_singleton)
## The code here are for the tester
## Do not change.
from moose_csp import moose_csp_problem
from map_coloring_csp import map_coloring_csp_problem
#from sudoku_csp import sudoku_csp_problem
solve_csp_problem(moose_csp_problem,forward_checking_prop_singleton,True)

def csp_solver_tree(problem, checker):
    problem_func = globals()[problem]
    checker_func = globals()[checker]
    answer, search_tree = problem_func().solve(checker_func)
    return search_tree.tree_to_string(search_tree)

##
## CODE for the learning portion of lab 4.
##

### Data sets for the lab
## You will be classifying data from these sets.
senate_people = read_congress_data('S110.ord')
senate_votes = read_vote_data('S110desc.csv')

house_people = read_congress_data('H110.ord')
house_votes = read_vote_data('H110desc.csv')

last_senate_people = read_congress_data('S109.ord')
last_senate_votes = read_vote_data('S109desc.csv')


### Part 1: Nearest Neighbors
## An example of evaluating a nearest-neighbors classifier.
senate_group1, senate_group2 = crosscheck_groups(senate_people)
#evaluate(nearest_neighbors(hamming_distance, 1), senate_group1, senate_group2, verbose=1)

## Write the euclidean_distance function.
## This function should take two lists of integers and
## find the Euclidean distance between them.
## See 'hamming_distance()' in classify.py for an example that
## computes Hamming distances.

def euclidean_distance(list1, list2):
    dist = 0

    # 'zip' is a Python builtin, documented at
    # <http://www.python.org/doc/lib/built-in-funcs.html>
    for item1, item2 in zip(list1, list2):
        dist+=(item1-item2)*(item1-item2)
    dist=math.sqrt(dist)
    return dist

#Once you have implemented euclidean_distance, you can check the results:
#evaluate(nearest_neighbors(euclidean_distance, 1), senate_group1, senate_group2)

## By changing the parameters you used, you can get a classifier factory that
## deals better with independents. Make a classifier that makes at most 3
## errors on the Senate.

my_classifier = nearest_neighbors(euclidean_distance, 1)
#evaluate(my_classifier, senate_group1, senate_group2, verbose=1)

### Part 2: ID Trees
#print (CongressIDTree(senate_people, senate_votes, homogeneous_disorder))

## Now write an information_disorder function to replace homogeneous_disorder,
## which should lead to simpler trees.

def information_disorder(yes, no):
    total_lenght=len(yes)+len(no)
    yesses=0
    noes=0
    democrat_val=0
    republican_val=0
    independent_val=0
    if not homogeneous_value(yes):
        for val in yes:
            if val=='Democrat':
                democrat_val+=1
            elif val=='Republican':
                republican_val+=1
            else:
                independent_val+=0
        democrat_val=democrat_val/len(yes)
        republican_val=republican_val/len(yes)
        independent_val=independent_val/len(yes)
        yes_democrat=-democrat_val*math.log(democrat_val,2) if democrat_val!=0 else 0
        yes_republican=-republican_val*math.log(republican_val,2) if republican_val!=0 else 0
        yes_independent=-independent_val*math.log(independent_val,2) if independent_val!=0 else 0
        yesses=(yes_democrat+yes_republican+yes_independent)*len(yes)/total_lenght
    democrat_val=0
    republican_val=0
    independent_val=0
    if not homogeneous_value(no):
        for val in no:
            if val=='Democrat':
                democrat_val+=1
            elif val=='Republican':
                republican_val+=1
            else:
                independent_val+=0
        democrat_val=democrat_val/len(no)
        republican_val=republican_val/len(no)
        independent_val=independent_val/len(no)
        no_democrat=-democrat_val*math.log(democrat_val,2) if democrat_val!=0 else 0
        no_republican=-republican_val*math.log(republican_val,2) if republican_val!=0 else 0
        no_independent=-independent_val*math.log(independent_val,2) if independent_val!=0 else 0
        noes=(no_democrat+no_republican+no_independent)*len(no)/total_lenght
    result=yesses+noes
    #result = -(PtoT)*math.log(PtoT,2)-(NtoT)*math.log(NtoT,2)
    return result
#print(information_disorder(['Democrat','Democrat','Democrat','Republican'],['Democrat','Republican',"Republican",]))
#print (CongressIDTree(senate_people, senate_votes, information_disorder))
#evaluate(idtree_maker(senate_votes, homogeneous_disorder), senate_group1, senate_group2)

## Now try it on the House of Representatives. However, do it over a data set
## that only includes the most recent n votes, to show that it is possible to
## classify politicians without ludicrous amounts of information.

def limited_house_classifier(house_people, house_votes, n, verbose = False):
    house_limited, house_limited_votes = limit_votes(house_people,
    house_votes, n)
    house_limited_group1, house_limited_group2 = crosscheck_groups(house_limited)

    if verbose:
        print ("ID tree for first group:")
        print (CongressIDTree(house_limited_group1, house_limited_votes,
                             information_disorder))
        print ()
        print ("ID tree for second group:")
        print (CongressIDTree(house_limited_group2, house_limited_votes,
                             information_disorder))
        print ()
        
    return evaluate(idtree_maker(house_limited_votes, information_disorder),
                    house_limited_group1, house_limited_group2)

                                   
## Find a value of n that classifies at least 430 representatives correctly.
## Hint: It's not 10.
N_1 = 44
rep_classified = limited_house_classifier(house_people, house_votes, N_1)
## Find a value of n that classifies at least 90 senators correctly.
N_2 = 70
senator_classified = limited_house_classifier(senate_people, senate_votes, N_2)
## Now, find a value of n that classifies at least 95 of last year's senators correctly.
N_3 = 50
old_senator_classified = limited_house_classifier(last_senate_people, last_senate_votes, N_3)

## The standard survey questions.
HOW_MANY_HOURS_THIS_PSET_TOOK = "5"
WHAT_I_FOUND_INTERESTING = "nothing"
WHAT_I_FOUND_BORING = "nothing"


## This function is used by the tester, please don't modify it!
def eval_test(eval_fn, group1, group2, verbose = 0):
    """ Find eval_fn in globals(), then execute evaluate() on it """
    # Only allow known-safe eval_fn's
    if eval_fn in [ 'my_classifier' ]:
        return evaluate(globals()[eval_fn], group1, group2, verbose)
    else:
        raise Exception( "Error: Tester tried to use an invalid evaluation function: '%s'" % eval_fn)

    
