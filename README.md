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

### gerador_de_combinacoes.py
Um algoritmo bem simples que gera todas as permutacoes 
possíveis de tamanho 1 até um limite informado. As combinações são geradas por meio da recursão.
```
>>> from gerador_de_combinacoes import GeradorDePermutacoes
>>> gerador = GeradorDePermutacoes(alphabet = "ab")
>>> gerador.gerar_permutacoes(2)
['a', 'b', 'aa', 'ab', 'ba', 'bb']
```