import pydot
import pyparsing
import json
import graphviz


path="/home/fmert/Praktikum/graphs/Lang/1.dot"
graph = pydot.graph_from_dot_file(path)
edgeList = graph.get_edge_list() 
for e in edgeList:
      tempAttr = json.dumps(e.get_attributes())
      edgeAttr = json.loads(tempAttr)
      edgeAttr['insert_label_here']