"""Gerador de permutação.

Esse script vai gerar recursivamente todas as possibilidades de combinações
possíveis de size_max 1 até n.

exemplo de uso:
>>> gerador = GeradorDePermutacoes(alphabet = "ab")
>>> gerador.gerar_permutacoes(2)
['a', 'b', 'aa', 'ab', 'ba', 'bb']

"""
class GeradorDePermutacoes:
    
    def __init__(self, alphabet="ab"):
        self._alphabet = list(set(alphabet))
        self._total_permutacoes = []

    def gerar_permutacoes(self, size_max):
        """Gera todas as combinacoes de palavras de tamanho 1 ate n."""
        for size_word in range(1, size_max+1):
            self.gerar_letras_iniciais_de_cada_palavra(size_word)
    
        return self._total_permutacoes

    def gerar_letras_iniciais_de_cada_palavra(self, size_word):
        """Inseri a letra inicial da palavra.

            size_word: int -> Tamanho desejado para as palavras.
        """
        for letter in self._alphabet:
            self.gerar_palavras(letter, 1, size_word)

    def gerar_palavras(self, word, size_current, size_target):
        """Gera todas a combinacoes de palavras dada a letra."""
        if size_current == size_target:
            self._total_permutacoes.append(word)

        else:
            for letter in self._alphabet:
                self.gerar_palavras(word+letter, size_current+1, size_target)