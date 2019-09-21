from search import *
import collections
NEWGRAPH1 = Graph(edgesdict=[ 
        { 'NAME': 'e1',  'LENGTH':  6, 'NODE1': 'S', 'NODE2': 'A' },
        { 'NAME': 'e2',  'LENGTH':  4, 'NODE1': 'A', 'NODE2': 'B' },
        { 'NAME': 'e3',  'LENGTH':  7, 'NODE1': 'B', 'NODE2': 'F' },
        { 'NAME': 'e4',  'LENGTH':  6, 'NODE1': 'C', 'NODE2': 'D' },
        { 'NAME': 'e5',  'LENGTH':  3, 'NODE1': 'C', 'NODE2': 'A' },
        { 'NAME': 'e6',  'LENGTH':  7, 'NODE1': 'E', 'NODE2': 'D' },
        { 'NAME': 'e7',  'LENGTH':  6, 'NODE1': 'D', 'NODE2': 'H' },
        { 'NAME': 'e8',  'LENGTH':  2, 'NODE1': 'S', 'NODE2': 'C' },
        { 'NAME': 'e9',  'LENGTH':  2, 'NODE1': 'B', 'NODE2': 'D' },
        { 'NAME': 'e10', 'LENGTH': 25, 'NODE1': 'E', 'NODE2': 'G' },
        { 'NAME': 'e11', 'LENGTH':  5, 'NODE1': 'E', 'NODE2': 'C' } ],
                  heuristic={"G":{'S': 11,
                                  'A': 9,
                                  'B': 6,
                                  'C': 12,
                                  'D': 8,
                                  'E': 15,
                                  'F': 1,
                                  'H': 2},
                             "H":{'S': 11,
                                  'A': 9,
                                  'B': 6,
                                  'D': 12,
                                  'E': 8,
                                  'F': 15,
                                  'G': 14},
                             'A':{'S':5, # admissible
                                  "B":1, # h(d) > h(b)+c(d->b) ...  6 > 1 + 2
                                  "C":3,
                                  "D":6,
                                  "E":8,
                                  "F":11,
                                  "G":33,
                                  "H":12},
                             'C':{"S":2, # consistent
                                  "A":3,
                                  "B":7,
                                  "D":6,
                                  "E":5,
                                  "F":14,
                                  "G":30,
                                  "H":12},
                             "D":{"D":3}, # dumb
                             "E":{} # empty
                             })
NEWGRAPH2 = Graph(edgesdict=
                  [ { 'NAME': 'e1', 'LENGTH': 2, 'NODE1': 'D', 'NODE2': 'F' },
                    { 'NAME': 'e2', 'LENGTH': 4, 'NODE1': 'C', 'NODE2': 'E' },
                    { 'NAME': 'e3', 'LENGTH': 2, 'NODE1': 'S', 'NODE2': 'B' },
                    { 'NAME': 'e4', 'LENGTH': 5, 'NODE1': 'S', 'NODE2': 'C' },
                    { 'NAME': 'e5', 'LENGTH': 4, 'NODE1': 'S', 'NODE2': 'A' },
                    { 'NAME': 'e6', 'LENGTH': 8, 'NODE1': 'F', 'NODE2': 'G' },
                    { 'NAME': 'e7', 'LENGTH': 5, 'NODE1': 'D', 'NODE2': 'C' },
                    { 'NAME': 'e8', 'LENGTH': 6, 'NODE1': 'D', 'NODE2': 'H' } ],
                  heuristic={"G":{'S': 9,
                                  'A': 1,
                                  'B': 2,
                                  'C': 3,
                                  'D': 6,
                                  'E': 5,
                                  'F': 15,
                                  'H': 10}})
AGRAPH = Graph(nodes = ['S', 'A', 'B', 'C', 'G'],
               edgesdict = [{'NAME': 'eSA', 'LENGTH': 3, 'NODE1': 'S', 'NODE2': 'A'},
                            {'NAME': 'eSB', 'LENGTH': 1, 'NODE1': 'S', 'NODE2': 'B'},
                            {'NAME': 'eAB', 'LENGTH': 1, 'NODE1': 'A', 'NODE2': 'B'},
                            {'NAME': 'eAC', 'LENGTH': 1, 'NODE1': 'A', 'NODE2': 'C'},
                            {'NAME': 'eCG', 'LENGTH': 10, 'NODE1': 'C', 'NODE2': 'G'}],
               heuristic = {'G':{'S': 12,
                                 'A': 9,
                                 'B': 12,
                                 'C': 8,
                                 'G': 0}})
NEWGRAPH4 = Graph(nodes=["S","A", "B", "C", "D", "E", "F", "H", "J", "K",
            "L", "T" ],
                 edgesdict = [{ 'NAME': 'eSA', 'LENGTH': 2, 'NODE1': 'S', 'NODE2': 'A' },
              { 'NAME': 'eSB', 'LENGTH': 10, 'NODE1': 'S', 'NODE2':'B' },
              { 'NAME': 'eBC', 'LENGTH': 5, 'NODE1': 'B', 'NODE2':'C' },
              { 'NAME': 'eBF', 'LENGTH': 2, 'NODE1': 'B', 'NODE2':'F' },
              { 'NAME': 'eCE', 'LENGTH': 5, 'NODE1': 'C', 'NODE2':'E' },
              { 'NAME': 'eCJ', 'LENGTH': 12, 'NODE1': 'C', 'NODE2':'J' },
              { 'NAME': 'eFH', 'LENGTH': 8, 'NODE1': 'F', 'NODE2':'H' },
              { 'NAME': 'eHD', 'LENGTH': 3, 'NODE1': 'H', 'NODE2':'D' },
              { 'NAME': 'eHK', 'LENGTH': 5, 'NODE1': 'H', 'NODE2':'K' },
              { 'NAME': 'eKJ', 'LENGTH': 1, 'NODE1': 'K', 'NODE2':'J' },
              { 'NAME': 'eJL', 'LENGTH': 4, 'NODE1': 'J', 'NODE2':'L' },
              { 'NAME': 'eKT', 'LENGTH': 7, 'NODE1': 'K', 'NODE2':'T' },
              { 'NAME': 'eLT', 'LENGTH': 5, 'NODE1': 'L', 'NODE2':'T' },
              ],
                 heuristic={"T":{'S': 10,
                                 'A': 6,
                                 'B': 5,
                                 'C': 2,
                                 'D': 5,
                                 'E': 1,
                                 'F': 100,
                                 'H': 2,
                                 'J': 3,
                                 'K': 100,
                                 'L': 4,
                                 'T': 0,}})
# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.           

def bfs(graph, start, goal):
    listem=list()
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        #print(queue)
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == goal:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get_connected_nodes(node):
            if adjacent not in listem:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
                listem.append(adjacent)
            
## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    listem=list()
    stack=[]
    stack.append([start])
    while stack:
        path=stack.pop()
        node=path[-1]
        if node==goal:
            return path
        if node not in listem:
            listem.append(node)
            for adjacent in graph.get_connected_nodes(node):            
                new_path=list(path)
                new_path.append(adjacent)
                stack.append(new_path)


## Now we're going to add some heuristics into the search.  
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    listem=list()
    path_includer=[]
    path=list()
    stack=[]
    stack.append([start])
    dictofheuristic=graph.heuristic.get(goal)
    while stack:
        path_includer.clear()
        temppathincluder=list()
        path=stack.pop()
        node=path[-1]
        my_dict=dict()
        if node==goal:
            if path==None:
                return list()
            return path
        if node not in listem:
            listem.append(node)
            for adjacent in graph.get_connected_nodes(node):            
                new_path=list(path)
                new_path.append(adjacent)
                path_includer.append(new_path)
            if dictofheuristic==None:
                for elem in path_includer:
                    stack.append(elem)
            else:
                for element in path_includer:
                     my_dict.update({element[-1]:dictofheuristic.get(element[-1])})
                for key,value in zip(my_dict.keys(),my_dict.values()):
                    if value==None:
                        my_dict.update({key:0})
                my_dict = sorted(my_dict.items(), key=lambda x: x[1],reverse=True)
                for elem in my_dict:
                    for element in path_includer:
                        if element[-1]==elem[0]:
                            temppathincluder.append(element)
                            break
                for elem in temppathincluder:
                    stack.append(elem)
## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the 
## graph get_heuristic function, with lower values being better values.
def sortSecond(val): 
    return val[1]
def beam_search(graph, start, goal, beam_width):
    listem=list()
    # maintain a queue of paths
    queue = []
    path=list()
    # push the first path into the queue
    queue.append([start])
    path_includer=[]
    dictofheuristic=graph.heuristic.get(goal)
    while queue:
        #print(queue)
        path_includer.clear()
        temppathincluder=list()
        deneme=list()
        my_dict1=list()
        # get the first path from the queue
        for t in range(len(queue)):
            path = queue.pop(0)
            #queue.clear()
            # get the last node from the path
            node = path[-1]
            listem.append(node)
            # path found
            my_dict=dict()
            if node == goal:
                return path
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for adjacent in graph.get_connected_nodes(node):
                if adjacent not in listem:
                    new_path = list(path)
                    new_path.append(adjacent)
                    path_includer.append(new_path)
            if dictofheuristic==None:
                i=0
                for elem in path_includer:
                    if i==beam_width:
                        break
                    temppathincluder.append(elem)
                    i+=1
            else:
                for element in path_includer:
                        my_dict.update({element[-1]:dictofheuristic.get(element[-1])})
        if dictofheuristic==None:
            queue=list(temppathincluder)
        else:
            i=0
            if my_dict=={}:
                return list('')
            for key,value in zip(my_dict.keys(),my_dict.values()):
                        if value==None:
                            my_dict.update({key:0})
            my_dict1=sorted(my_dict.items(), key=lambda x: x[1],reverse=False)
            for elem in my_dict1:
                        if i==beam_width:
                            break
                        for element in path_includer:
                            if element[-1]==elem[0] :
                                temppathincluder.append(element)
                                i+=1
                                break
            for elem in temppathincluder:
                listem.append(elem[-1])
                deneme.append(elem)        
            queue=list(deneme)
## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    lenofnodes=0
    i=1
    namesofedges=list()
    if len(node_names)==1:
        return 0
    nodefirst=node_names[0]
    nodesecond=node_names[1]
    for j in range(len(node_names)):
        for edge in graph.edges:
            if (nodefirst==edge.node1 and nodesecond ==edge.node2) or (nodesecond==edge.node1 and nodefirst ==edge.node2):
                lenofnodes+=edge.length
                if i+1==len(node_names):
                    return lenofnodes
                nodefirst=node_names[i]
                nodesecond=node_names[i+1]
                i+=1
                break


def branch_and_bound(graph, start, goal):
    listem=list()
    stack=[]
    stack.append([start])
    while stack:
        tempstack=[]
        unsorteddict=dict()
        for j in range(len(stack)):
            lenghtofpath=path_length(graph,stack[j])
            unsorteddict.update({j:lenghtofpath})
        sorteddict=sorted(unsorteddict.items(), key=lambda x: x[1],reverse=True)
        for elem in  sorteddict:
            tempstack.append(stack[elem[0]])
        stack=list(tempstack)
        path=stack.pop()
        node=path[-1]
        temppathincluder=list()
        if node==goal:
            return path
        if node not in listem:
            listem.append(node)
            for adjacent in graph.get_connected_nodes(node):            
                new_path=list(path)
                new_path.append(adjacent)
                stack.append(new_path)

def a_star(graph, start, goal):
    listem=list()
    goalincluder=[]
    heuristiclenght=0
    stack=[]
    stack.append([start])
    #listem.append(start)
    dictofheuristic=graph.heuristic.get(goal)
    unsortedgoaldict=dict()
    tempgoal=list()
    while stack:
        tempstack=[]
        unsorteddict=dict()
        path=stack.pop()
        node=path[-1]
        if node==goal:
            goalincluder.append(path)
            continue
        if node not in listem:
            listem.append(node)
            for adjacent in graph.get_connected_nodes(node):            
                new_path=list(path)
                new_path.append(adjacent)
                stack.append(new_path)
        for j in range(len(stack)):
            lenghtofpath=path_length(graph,stack[j])
            if dictofheuristic==None or node not in dictofheuristic:
                unsorteddict.update({j:lenghtofpath})
            else:
                unsorteddict.update({j:lenghtofpath+dictofheuristic[node]})
        sorteddict=sorted(unsorteddict.items(), key=lambda x: x[1],reverse=True)
        for elem in  sorteddict:
            tempstack.append(stack[elem[0]])
        stack=list(tempstack)
        counter=1
        for eleman in stack[0:-2]:
            for element in stack[counter:]:
                if eleman[-1]==element[-1]:
                    pathlenght1=path_length(graph,element)
                    pathlenght2=path_length(graph,eleman)
                    if pathlenght1>pathlenght2:
                        stack.remove(eleman)
                        break
                    else:
                        stack.remove(element)
                counter+=1
        #print(stack)
                    
    for j in range(len(goalincluder)):
            lenghtofpath=path_length(graph,goalincluder[j])
            unsortedgoaldict.update({j:lenghtofpath})
    sortedgoaldict=sorted(unsortedgoaldict.items(), key=lambda x: x[1],reverse=False)
    for elem in sortedgoaldict:
            tempgoal.append(goalincluder[elem[0]])
    #print(tempgoal)
    if len(tempgoal)>0:
        return tempgoal[-1]
    else:
        return list('')
## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    heuristiclenght=0
    dictofheuristic=graph.heuristic.get(goal)
    for node in graph.nodes:
        pathlist=a_star(graph,node,goal)
        lenghofpath=path_length(graph,pathlist)
        if dictofheuristic==None or node not in dictofheuristic:
            heuristiclenght=0
        else:
            heuristiclenght=dictofheuristic[node]
        if heuristiclenght>lenghofpath:
            return False
    return True
        

def is_consistent(graph, goal):
    minuslenght=0
    dictofheuristic=graph.heuristic.get(goal)
    for edge in graph.edges:
        if dictofheuristic==None:
            minuslenght=0
        elif edge.node1 not in dictofheuristic:
            minuslenght1=0
            if edge.node2 not in dictofheuristic:
                minuslenght2=0
            else:
                minuslenght2=dictofheuristic[edge.node2]
            minuslenght=abs(minuslenght1-minuslenght2)
        elif edge.node2 not in dictofheuristic:
            if edge.node1 not in dictofheuristic:
                minuslenght1=0
            else:
                minuslenght1=dictofheuristic[edge.node1]
            minuslenght2=0
            minuslenght=abs(minuslenght1-minuslenght2)
        else:
            minuslenght1=dictofheuristic[edge.node1]
            minuslenght2=dictofheuristic[edge.node2]
            minuslenght=abs(minuslenght1-minuslenght2)
        if minuslenght>edge.length:
            return False
    return True

HOW_MANY_HOURS_THIS_PSET_TOOK = '20'
WHAT_I_FOUND_INTERESTING = 'To write search algorithms shown in lectures'
WHAT_I_FOUND_BORING = 'Too many functions to complete'

#print(dfs(NEWGRAPH1, 'S', 'G'))
#print(hill_climbing(NEWGRAPH1, 'F', 'G'))
#print(beam_search(NEWGRAPH1, 'S', 'G',2))
#print(path_length(NEWGRAPH1, list('SASAS')))
#print(branch_and_bound(NEWGRAPH1, 'S', 'G'))
print(a_star(NEWGRAPH4, 'S', 'T'))
#print(a_star(AGRAPH, "S", "G"))
#print(is_consistent(NEWGRAPH1, "D"))
