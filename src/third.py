from models.node import Node

class LowestCommonAncestor(object):
    
    def __key_exist(self, dictionary, key):
        val = dictionary.get(key, None)
        return val != None

    def __get_parent_nodes(self, node):
        parent_nodes = {}
        
        if(isinstance(node, Node) == False):
            return parent_nodes
        
        while(node != None):
            key = str(node.value)
            if(self.__key_exist(parent_nodes, key) == False):
                parent_nodes[key] = 1 
            node = node.parent
        
        return parent_nodes


    def lca(self, a, b):
        if(isinstance(a, Node) == False or isinstance(b, Node) == False):
            return None

        parent_nodes = self.__get_parent_nodes(a)

        while(b != None):
            key = str(b.value)
            if(self.__key_exist(parent_nodes, key)):
                return b.value
            b = b.parent
        
        return None