from random import randint, sample
from graphviz import Digraph

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    def build_from_infix(self, expr):
        # Remove espaços e tokeniza
        tokens = expr.replace('(', ' ( ').replace(')', ' ) ').split()
        self.root = self._build(tokens)

    def _build(self, tokens):
        stack = []
        ops = []
        for token in tokens:
            if token == '(':
                ops.append(token)
            elif token.isdigit():
                stack.append(Node(token))
            elif token in '+-*/':
                ops.append(token)
            elif token == ')':
                while ops and ops[-1] != '(':
                    op = ops.pop()
                    right = stack.pop()
                    left = stack.pop()
                    node = Node(op)
                    node.left = left
                    node.right = right
                    stack.append(node)
                ops.pop()  # Remove '('
        return stack[0] if stack else None

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
        
    
def gerar_expressao_aleatoria():
    operators = ['+', '-', '*', '/']
    operand = [str(randint(1, 20)) for _ in range(3)]
    op1, op2 = sample(operators, 2)
    # Forma: ( ( a op1 b ) op2 c )
    expr = f"( ( {operand[0]} {op1} {operand[1]} ) {op2} {operand[2]} )"
    return expr

# Exemplo de uso:
# Aqui é pra poder testar um de cada vez, gerando uma imagem por vez

def fixValue():
    
    expr = "( ( 7 + 3 ) * ( 5 - 2 ) )"
    tree = ExpressionTree()
    tree.build_from_infix(expr)
    
    dot = tree.visualize()
    dot.render('atividade_1_ArvoreExpressao', format='png', view=True)
    
def randomValue():
    expr_aleatoria = gerar_expressao_aleatoria()
    print("Expressão gerada:", expr_aleatoria)
    tree2 = ExpressionTree()
    tree2.build_from_infix(expr_aleatoria)
    
    dot2 = tree2.visualize()
    dot2.render('atividade_1_ArvoreExpressao_Aleatoria', format='png', view=True)    


while True:
    choice = int(input("Escolha a árvore de valores fixos ou de valores aleatórios\n-> [1] Valores fixos\n-> [2] Valores aleatórios\n-> "))
    
    if choice == 1:
        fixValue()
        
    elif choice == 2:
        randomValue()
        
    else:
        print("Nenhuma árvore foi gerada. ERROR!!!")
        break
