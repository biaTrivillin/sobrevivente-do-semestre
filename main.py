import pygame
from tela_inicial import tela_inicial
from tela_jogo import tela_jogo
from tela_final import tela_final

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sobrevivente do Semestre")

if __name__ == "__main__":
    tela_inicial(tela)

    tela_jogo(tela)

    tela_final(tela)

