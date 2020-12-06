# Desafios-pessoais
Alguns scripts em python com desafios pessoais.



### file_explorer.py
Simples buscador de arquivos que utiliza arvores para montar a hierarquia de diretórios.
```
>>> from file_explorer import FileExplorer
>>> f = FileExplorer()
>>> f.search("a.pdf", "test/")
test/a/b/a.pdf
test/c/d/a.pdf
test/e/f/a.pdf
>>> print(f._ROOT_NODE)
childs: 3 # a c e, respectivamente
```