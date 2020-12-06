"""Simples explorador de arquivos.

O arquivo utiliza uma simples algoritmo de busca em nível para mapear a 
hierarquia de arquivos e diretórios e também buscar algum arquivo específico 
após esse mapeamento.

Exemplo:

>>> f = FileExplorer()
>>> f.search("a.pdf", "test/")
test/a/b/a.pdf
test/c/d/a.pdf
test/e/f/a.pdf

>>> print(f._ROOT_NODE)
childs: 3 # a c e, respectivamente

"""
import os

class ArchiveNode:
    
    def __init__(self, name):
        self._name = name
        self._nodes = []
        self._is_leaf = not os.path.isdir(name)

    def __str__(self):
        return f"childs: {len(self.nodes)}"
    
    @property
    def is_leaf(self):
        return self._is_leaf

    @property
    def name(self):
        return self._name

    def add_node(self, node):
        self._nodes.append(node)

    @property
    def nodes(self):
        return self._nodes


class FileExplorer:

    _QUEUE = []
    _ROOT_NODE: ArchiveNode

    def search(self, file_name, start_location):
        try:
            self._ROOT_NODE = self._map_dirs_hierarchy_using_in_level_search(start_location)
            self._search_file_through_in_level_search(file_name)
        
        except Exception as err:
            print(f"Error: {err}")

    def _search_file_through_in_level_search(self, file_name):
        self._QUEUE = [self._ROOT_NODE]

        while len(self._QUEUE) != 0:
            current_node = self._QUEUE.pop(0)
            if self._is_node_a_dir(current_node):
                self._QUEUE.extend(current_node.nodes)

            if file_name in os.path.basename(current_node.name):
                print(current_node.name)

    def _map_dirs_hierarchy_using_in_level_search(self, start):
        self._ROOT_NODE = ArchiveNode(start)
        self._QUEUE = [self._ROOT_NODE]

        while len(self._QUEUE) != 0:
            current_node = self._QUEUE.pop(0)
            if self._is_node_a_dir(current_node):
                father_path = current_node.name
                for archive in os.listdir(father_path):
                    child_path = self._generate_absolute_path(father_path, archive)
                    child_node = ArchiveNode(child_path)
                    self._QUEUE.append(child_node)
                    current_node.add_node(child_node)

        return self._ROOT_NODE

    def _generate_absolute_path(self, origin_path, dest_path):
        return os.path.join(origin_path, dest_path)

    def _is_node_a_dir(self, node):
        return not node.is_leaf