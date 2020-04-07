import networkx as nx
import matplotlib.pyplot as plt
import queue, time, math

def gen_dfs_graph():

    # Plot Initialization
    plt.ion()                   # makes plot interactive
    plt.figure(figsize=(10,10))   # squares plot
    node_size = 500
    num_nodes = 10
    max_digits = math.ceil(math.log(num_nodes, 10))

    # Graph setup
    G = nx.erdos_renyi_graph(num_nodes, 2/num_nodes, directed=True)
    pos = nx.circular_layout(G)
    # Note: many other types of layouts are supported, including
    #       kamada_kawai_layout
    
    d = []              # d[v] = discovery time
    f = []              # f[v] = finish time
    p = []              # p[v] = predecessor of v
    colour = []          # color[v] = white if undiscovered
    time = 0
    i = 0               # frame number
    l = len(list(G))    # num nodes in G
    
    def update_graph(nodes=[], edges=[], nodecolor='#d1f1ff', edgecolor='black'):
        nx.draw_networkx(G, nodelist=nodes, node_color=nodecolor, node_size=node_size, edgelist=edges, edge_color=edgecolor, pos=pos, with_labels=True)
        
    def save_image():
        nonlocal i
        plt.savefig("graph"+str(i).zfill(max_digits)+".png")
        i+=1

    # Initialization
    for node in G:
        d.append(l)     # d[v] = infinity = l
        f.append(l)     # f[v] = infinity = l
        p.append(-1)
        colour.append("white")

    # Graphics

    # Initial graph drawing, all nodes undiscovered
    nx.draw(G, node_color='#d1f1ff', node_size=node_size, pos=pos, with_labels=True)
    save_image()  

    # Run DFS

    def dfs_visit(x):
        nonlocal time
        time += 1
        colour[x] = "gray"
        d[x] = time
        # color node gray
        update_graph([x], nodecolor='#69d1ff')
        save_image()
        
        for y in G[x]:
            if colour[y] == "white":
                update_graph(edges=[(x,y)], edgecolor='#69d1ff')
                save_image()
                p[y] = x
                dfs_visit(y)
                update_graph(edges=[(x,y)], edgecolor='#1e7da5')

        time += 1
        colour[x] = "black"
        update_graph([x], nodecolor='#1e7da5')
        f[x] = time
        if p[x] == -1:
            save_image()

    for node in G.nodes:
        if colour[node] == "white":
            dfs_visit(node)  

def main():
    gen_dfs_graph()
