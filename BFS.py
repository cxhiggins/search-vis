import networkx as nx
import matplotlib.pyplot as plt
import queue, time, math, os

def gen_bfs_graph():

    # Plot Initialization
    plt.ion()                   # makes plot interactive
    plt.figure(figsize=(10,10))   # squares plot
    node_size = 500
    num_nodes = 100
    max_digits = math.ceil(math.log(num_nodes, 10))

    # Graph setup
    G = nx.erdos_renyi_graph(num_nodes, 2/num_nodes, directed=True)
    pos = nx.kamada_kawai_layout(G)
    # Note: many other types of layouts are supported, including
    #       kamada_kawai_layout
    
    d = []              # d[v] = num edges in shortest path from source to v
    p = []              # p[v] = predecessor in shortest path from source to v
    x = []              # x[v] = [u | u in G.nodes, d[u] == v]
    y = [[]]            # y[w] = [(u,v) | (u,v) in G.edges, d[v] == l, d[u] == w] := edges from all nodes of dist w to undiscovered nodes
    l = len(list(G))    # num nodes in G
    i = 0               # frame number
    
    def update_graph(nodes=G.nodes, edges=G.edges, nodecolor='#d1f1ff', edgecolor='black'):
        nx.draw_networkx(G, nodelist=nodes, node_color=nodecolor, node_size=node_size, edgelist=edges, edge_color=edgecolor, pos=pos, with_labels=True)
        
    def save_image():
        plt.savefig("graph"+str(i).zfill(max_digits)+".png")

    for node in G:
        d.append(l)     # d[v] = l means v isn't reachable from source
        p.append(-1)    # p[v] = -1 means v has no predecessor
        x.append([])
        y.append([])
    d[0] = 0            # 0 is the specified starting node

    # Graphics

    # Initial graph drawing, all nodes undiscovered
    nx.draw(G, node_color='#d1f1ff', node_size=node_size, pos=pos, with_labels=True)
    save_image()  

    # Run BFS, adding nodes and edges to x and y appropriately
    q = queue.Queue(0)
    q.put(0) # start from node 0
    while not q.empty():
        u = q.get()
        x[d[u]].append(u)
        
        for v in G[u]:
            if d[v] == l:
                y[d[u]+1].append((u,v))
                d[v] = d[u] + 1
                p[v] = u
                q.put(v)

    # Iterate through x and y simultaneously, updating graph and saving frames
    lastnodes = []; lastedges = []
    for i in range(l):
        nodes = x[i]
        if not nodes == []:
            i+=1
            update_graph(nodes, lastedges, '#69d1ff', '#69d1ff')
            save_image()
        lastnodes = nodes
        update_graph(lastnodes, lastedges, '#1e7da5', 'black')
        lastedges = y[i]
    save_image()  

def main():
    gen_bfs_graph()
    os.system("magick convert -delay 50 graph*.png test.gif")
    os.system("rm graph*.png")

if __name__ == "__main__":
    main()