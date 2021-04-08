BLACK = 0
RED = 1
# From ProgrammerSought at https://www.programmersought.com/article/68933874096/

import os
from graphviz import Digraph


class Rbtree:
    root = None
    name = None
    op_num = 0

    def __init__(self, name='rbtree'):
        self.name = name

    def insert(self, point):
        self.op_num += 1
        if self.root is None:
            point.color = BLACK
            self.root = point
            # self.view()
            return
        self.root.add_child(point)
        # self.view()

    def find(self, key):
        self.op_num += 1
        if self.root is None:
            print('The tree is empty!')
            return None
        res = self.root.find(key)
        # self.view()
        return res

    # def select(self, point):
    # def print(self):
    def view(self):
        graph = Digraph(self.name, format='png')
        if self.root is not None:
            self.root.draw(graph)
##            graph.render("rbt"+str(self.op_num).zfill(3), cleanup=True)
            graph.view("final_rbt", cleanup=True)


class RbPoint:
    parent = None
    left = None
    right = None
    color = -1  # Node color 0 black 1 red
    key = None
    tree = None

    def __init__(self, key, tree):
        self.key = key

    def view(self):
        pg = Digraph('find')
        pg.node(str(self.key), style='filled', color=('red' if self.color == RED else 'BLACK'), fontcolor='white',
                shape='circle')
        pg.view()

    def draw(self, graph):
        if self.color == BLACK:
            s = 'black'
        else:
            s = 'red'
        # Draw your own point, including value and color
        graph.node(str(self.key), style='filled', color=('red' if self.color == RED else 'BLACK'), fontcolor='white',
                   shape='circle')
        if self.left is not None:
            graph.edge(str(self.key), str(self.left.key))
            self.left.draw(graph)
        if self.right is not None:
            graph.edge(str(self.key), str(self.right.key))
            self.right.draw(graph)

    def change_color(self):
        if self.color == BLACK:
            self.color = RED
        else:
            self.color = BLACK

    def rotate(self, child):
        # Rotate with the left child
        if child == self.left:
            print('Turn from left to right')
            if self.parent is not None:
                if self.parent.left == self:
                    self.parent.left = child
                else:
                    self.parent.right = child
            child.parent = self.parent
            self.parent = child
            self.left = child.right
            child.right = self
            if child.parent is None:
                # The node becomes the root node
                print('Root node changed')
                tree.root = child
        # Rotate with the right child
        else:
            print('Turn right to left')
            if self.parent is not None:
                if self.parent.left == self:
                    self.parent.left = child
                else:
                    self.parent.right = child
            child.parent = self.parent
            self.right = child.left
            child.left = self
            self.parent = child
            if child.parent is None:
                # The node becomes the root node
                print('Root node changed')
                tree.root = child

    def find(self, key):
        print('Current node value:', self.key, 'Find value:', key)
        if key == self.key:
            return self
        if key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(key)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(key)

    def add_child(self, child):
        if child.key < self.key:
            if self.left is None:
                self.left = child
                child.parent = self
                print('Key is', child.key, 'The node inserted into the key is', self.key, 'The left child of the node')
                self.adjust(child)
            else:
                self.left.add_child(child)
            return

        if child.key > self.key:
            if self.right is None:
                self.right = child
                child.parent = self
                print('Key is', child.key, 'The node inserted into the key is', self.key, 'The right child of the node')
                self.adjust(child)
            else:
                self.right.add_child(child)

    def adjust(self, child):
        def handle1(g, p):
            g.rotate(p)
            g.change_color()
            p.change_color()
            print('Condition 1 is adjusted')

        def handle2(g, p, n):
            p.rotate(n)
            # Condition 2 -> Condition 1
            g.rotate(n)
            n.change_color()
            g.change_color()
            print('Situation 2')

        def handle3(g, p, u):
            print('Situation 3')
            p.change_color()
            u.change_color()
            g.change_color()
            if g.parent is not None:
                g.parent.adjust(g)
            else:
                # g is the root node
                g.color = BLACK

        def handle4(g, p):
            p.change_color()
            g.change_color()
            if g.parent is not None:
                g.parent.adjust(g)
            else:
                # g is the root node
                g.color = BLACK

        print('Start adjustment')
        # Child node default red
        child.color = RED
        # According to the p node (parent node) color to determine whether it needs to be adjusted
        if self.color == BLACK:
            # Black, no need to adjust
            return

        # The parent node is also red and must be adjusted
        # The parent node is red, the G node (parent node of the parent node) must exist and must be black
        # Condition 1: U node (uncle node) is black, n node (newly added node) is inserted outside
        # Condition 2: u is black, n is inserted inside
        # Condition 3: u is red
        g = self.parent
        if self == g.left:
            # The parent node is the left child of the grandfather node, and the uncle node is the right child of the grandfather node
            u = g.right
            if u is None or u.color == BLACK:
                # u node is black, status 1 or 2
                if child == self.left:
                    # Condition 1
                    handle1(g, self)
                else:
                    # Condition 2
                    handle2(g, self, child)
            else:
                # u node is red, status 3
                handle3(g, self, u)
        # The child node is the left child of the parent node, status 1
        else:
            # The parent node is the right child of the grandfather node
            u = g.left
            if u is None or u.color == BLACK:
                if child == self.right:
                    # Condition 1
                    handle1(g, self)
                else:
                    # Condition 2
                    handle2(g, self, child)
            else:
                # Condition 3, the u node is red
                handle3(g, self, u)


if __name__ == '__main__':
    tree = Rbtree('t2')
    for i in range(20, -1, -1):
        p = RbPoint(i, tree)
        tree.insert(p)
    tree.view()
##    os.system("magick convert -delay 50 rbt*.png rbt.gif")
##    os.system("rm rbt*.png")
