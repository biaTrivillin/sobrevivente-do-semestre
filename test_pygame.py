import pygame
import sys

pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Teste Pygame - Desvie dos Obstáculos")

clock = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 36)

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill((30, 30, 30))
    texto = fonte.render("Se você está vendo esta janela, deu certo! :)", True, (220, 220, 220))
    tela.blit(texto, (40, 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
