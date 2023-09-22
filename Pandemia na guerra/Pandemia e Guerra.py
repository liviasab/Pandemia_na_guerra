import enum
import random

from PIL import Image

# Definindo enumeração para os estados dos soldados
class Estado(enum.Enum):
    saudavel = 0
    ferido = 1
    morto = 2
    doente = 3

# Classe que representa um soldado
class Soldado:
    def __init__(self, estado):
        self.estado = estado

# Classe do Modelo de Propagação de Doenças durante a Primeira Guerra Mundial com Pandemia
class ModeloPropagacaoGuerraEPandemia:
    def __init__(self, tamanhoCampoBatalha):
        self.populacao = []  # Matriz representando o campo de batalha
        self.geracaoAtual = 0

        # Taxa de mortalidade durante a guerra
        self.taxaMortalidade = 0.2

        # Taxa de contágio da pandemia
        self.taxaContagioPandemia = 0.4

        for i in range(tamanhoCampoBatalha):
            self.populacao.append([])
            for j in range(tamanhoCampoBatalha):
                # Inicialmente, todos os soldados estão saudáveis
                self.populacao[i].append(Soldado(Estado.saudavel))

        # Introduzindo a pandemia (alguns soldados começam doentes)
        for i in range(tamanhoCampoBatalha):
            for j in range(tamanhoCampoBatalha):
                if random.random() < 0.05:
                    self.populacao[i][j].estado = Estado.doente

    def propagarDoenca(self, linha, coluna):
        soldado = self.populacao[linha][coluna]

        # Se um soldado estiver saudável, ele pode ficar doente com uma certa probabilidade
        if soldado.estado == Estado.saudavel:
            if random.random() < self.taxaContagioPandemia:
                self.populacao[linha][coluna].estado = Estado.doente

    def proximaGeracao(self):
        for i in range(len(self.populacao)):
            for j in range(len(self.populacao[i])):
                self.propagarDoenca(i, j)

        self.geracaoAtual += 1

    def relatorio(self):
        totalSoldados = sum(1 for linha in self.populacao for soldado in linha)
        totalDoentes = sum(1 for linha in self.populacao for soldado in linha if soldado.estado == Estado.doente)
        return totalSoldados, totalDoentes

    def simulation(self, geracoes):
        for i in range(geracoes):
            self.proximaGeracao()
            totalSoldados, totalDoentes = self.relatorio()
            print(f"Geração {i + 1}: Total de Soldados={totalSoldados}, Doentes={totalDoentes}")


# Parâmetros da simulação
tamanhoCampoBatalha = 100  # Tamanho do campo de batalha
numeroDeGeracoes = 50  # Número de gerações a simular

# Executando a simulação
modelo = ModeloPropagacaoGuerraEPandemia(tamanhoCampoBatalha)
modelo.simulation(numeroDeGeracoes)