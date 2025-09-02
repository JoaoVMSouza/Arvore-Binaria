from graphviz import Digraph

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_rec(self.root, value)

    def _insert_rec(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_rec(current.left, value)
        elif value == current.value:
            return None
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_rec(current.right, value)

    def visualize(self):
        dot = Digraph()
        def add_nodes_edges(node):
            if node:
                dot.node(str(node.value))
                if node.left:
                    dot.edge(str(node.value), str(node.left.value))
                    add_nodes_edges(node.left)
                if node.right:
                    dot.edge(str(node.value), str(node.right.value))
                    add_nodes_edges(node.right)
        add_nodes_edges(self.root)
        return dot

    def search(self, current, value):
        if current is None:
            return None
        if value == current.value:
            return current
        elif value < current.value:
            return self.search(current.left, value)
        else:
            return self.search(current.right, value)

    def remove(self, value):
        self.root = self._remove_rec(self.root, value)

    def _remove_rec(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._remove_rec(node.left, value)
        elif value > node.value:
            node.right = self._remove_rec(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._remove_rec(node.right, min_larger_node.value)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def depth(self, value):
        return self._depth_rec(self.root, value, 0)

    def _depth_rec(self, node, value, depth):
        if node is None:
            return -1
        if value == node.value:
            return depth
        elif value < node.value:
            return self._depth_rec(node.left, value, depth + 1)
        else:
            return self._depth_rec(node.right, value, depth + 1)

    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def max_depth(self):
        return self._max_depth_rec(self.root)

    def _max_depth_rec(self, node):
        if node is None:
            return 0
        return 1 + max(self._max_depth_rec(node.left), self._max_depth_rec(node.right))

    def is_most_deep_node(self, value):
        node_depth = self.depth(value)
        max_depth = self.max_depth() - 1  # depth começa em 0
        return node_depth == max_depth

# ========================= EXECUÇÃO =========================

tree = BinaryTree()
list1 = [55, 30, 80, 20, 45, 70, 90]

for i in list1:
    tree.insert(i)

# Visualizar árvore inicial
dot = tree.visualize()
dot.render('Arvore_binaria', format='png', view=True)

# Buscar um valor
number = int(input("Escolha um número da árvore para buscar: "))
result = tree.search(tree.root, number)

if result:
    print(f"{number} foi encontrado na árvore!")
else:
    print(f"{number} não está na árvore.")

# Remover um valor fixo
tree.remove(80)
print("O valor 80 foi removido da árvore.")

# Profundidade de um nó fixo
prof = tree.depth(45)
print(f"Profundidade do nó 45: {prof}")

# Altura de um nó escolhido pelo usuário
number = int(input("Digite um número da árvore para calcular a altura: "))
no = tree.search(tree.root, number)
if no:
    altura = tree.height(no)
    print(f"Altura do nó {number}: {altura}")
else:
    print(f"Nó {number} não encontrado.")

# Verificar se um nó está na profundidade mais baixa
check = int(input("Digite um número para verificar se está na maior profundidade: "))
if tree.is_most_deep_node(check):
    print(f"O valor {check} está no nível mais profundo da árvore.")
else:
    print(f"O valor {check} NÃO está no nível mais profundo da árvore.")

dot = tree.visualize()
dot.render('Arvore_binaria', format='png', view=True)

newNode = int(input("Adicione um número novo a árvore: "))
tree.insert(newNode)

# Visualizar árvore final
dot = tree.visualize()
dot.render('Arvore_binaria', format='png', view=True)

