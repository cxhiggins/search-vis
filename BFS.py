import networkx as nx
import matplotlib.pyplot as plt
import queue
import time

plt.ion()

G = nx.erdos_renyi_graph(10, 0.15, directed=True)
pos = nx.circular_layout(G)
##pos = nx.kamada_kawai_layout(G)
l = len(list(G)) # max val for d[u]
d = []
p = []
x = []
i = 0

for node in G:
    d.append(l)
    p.append(-1)
    x.append([])
d[0] = 0
p[0] = -1

nx.draw(G, node_color='#d1f1ff', pos=pos, with_labels=True)
plt.savefig("graph"+str(i)+".png")

q = queue.Queue(0)
q.put(0) # start from node 0
while not q.empty():
    u = q.get()
    x[d[u]].append(u)
    
    for v in G[u]:
        if d[v] == l:
            d[v] = d[u] + 1
            p[v] = u
            q.put(v)

lastnodes = []
for nodes in x:
    if not nodes == []:
        i+=1
        nx.draw_networkx_nodes(G, nodelist=nodes, node_color='#69d1ff', pos=pos, with_labels=True)
        plt.savefig("graph"+str(i)+".png")
    lastnodes = nodes
    nx.draw_networkx_nodes(G, nodelist=lastnodes, node_color='#1e7da5', pos=pos, with_labels=True)
plt.savefig("graph"+str(i)+".png")
