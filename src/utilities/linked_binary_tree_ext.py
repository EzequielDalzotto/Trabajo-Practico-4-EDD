from typing import Any, List
from .linked_binary_tree_abstract import LinkedBinaryTreeExtAbstract
from .data_structures import LinkedBinaryTree
from .data_structures import BinaryTreeNode



class LinkedBinaryTreeExt(LinkedBinaryTreeExtAbstract,LinkedBinaryTree):

    def hermanos(self, nodo1: BinaryTreeNode, nodo2: BinaryTreeNode) -> bool:
        if self.is_empty():
            return False

        if not self._contains(nodo1) or not self._contains(nodo2):
            return False

        if nodo1 == nodo2:
            return False #No puede ser hermano de si mismo

        return self._search_parent(nodo1) == self._search_parent(nodo2)

    def hojas(self) -> List[Any]:
        retorno = []

        for node in self._preorder_traversal_nodes(self._root) :
            if node.children_count() == 0:
                retorno.append(node.element)

        return retorno

    def internos(self) -> List[Any]:
        retorno = []
        
        for node in self._preorder_traversal_nodes(self._root) :
            if node.children_count() > 0 and not self._search_parent(node) == None:
                retorno.append(node.element)

        return retorno

    def profundidad(self, nodo: BinaryTreeNode) -> int:
        
        i = 0
        while self._search_parent(nodo):
            nodo = self._search_parent(nodo)
            i+=1

        return i

    def altura(self, nodo: BinaryTreeNode) -> int:
        izq = self._calculo_altura_nodo_por_izq(nodo)
        der = self._calculo_altura_nodo_por_der(nodo)

        return izq if izq > der else  der





    #########################################################################
    #							MÉTODOS NO PÚBLICOS
    #########################################################################
        
    def _preorder_traversal_nodes(self, node : BinaryTreeNode): 
        if node:
            yield node
            
            yield from self._preorder_traversal_nodes(node.left_child)
            yield from self._preorder_traversal_nodes(node.right_child)

    def _calculo_altura_nodo_por_izq(self, node : BinaryTreeNode, cont = 0 ) -> int:
        if node.children_count() == 0:
            return cont

        if node.left_child:
            return self._calculo_altura_nodo_por_izq(node.left_child,(cont+1))
        
        if node.right_child:
            return self._calculo_altura_nodo_por_izq(node.right_child,(cont+1))

        if not node.left_child and node.right_child:
            return self._calculo_altura_nodo_por_izq(node.right_child,(cont+1))
        
        if not node.right_child and node.left_child:
            return self._calculo_altura_nodo_por_izq(node.left_child,(cont+1))

    def _calculo_altura_nodo_por_der(self, node : BinaryTreeNode, cont = 0 ) -> int:
        if node.children_count() == 0:
            return cont

        if node.right_child:
            return self._calculo_altura_nodo_por_der(node.right_child,(cont+1))

        if node.left_child:
            return self._calculo_altura_nodo_por_der(node.left_child,(cont+1))
        
        if not node.left_child and node.right_child:
            return self._calculo_altura_nodo_por_der(node.right_child,(cont+1))
        
        if not node.right_child and node.left_child:
            return self._calculo_altura_nodo_por_der(node.left_child,(cont+1))
