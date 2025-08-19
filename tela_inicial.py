import pygame
import sys
from config import LARGURA, ALTURA, GIZ_BRANCO, GIZ_AZUL, FUNDO_PATH, FONTE_TITULO_PATH, FONTE_TITULO_SIZE, FONTE_TEXTO_PATH, FONTE_TEXTO_SIZE

def tela_inicial(tela):
    # Criar fontes depois que o Pygame foi inicializado
    fonte_titulo = pygame.font.Font(FONTE_TITULO_PATH, FONTE_TITULO_SIZE)
    fonte_texto = pygame.font.Font(FONTE_TEXTO_PATH, FONTE_TEXTO_SIZE)

    # Carregar fundo
    fundo = pygame.image.load(FUNDO_PATH)
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

    clock = pygame.time.Clock()
    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rodando = False

        # Desenhar fundo e textos
        tela.blit(fundo, (0, 0))

        titulo = fonte_titulo.render("Sobrevivente do Semestre", True, GIZ_BRANCO)
        instrucao1 = fonte_texto.render("Você é um estudante universitário...", True, GIZ_BRANCO)
        instrucao2 = fonte_texto.render("Desvie das provas e livros pesados!", True, GIZ_AZUL)
        instrucao3 = fonte_texto.render("Colete cafés e lápis mágicos para ganhar pontos.", True, GIZ_BRANCO)
        instrucao4 = fonte_texto.render("Use as teclas:", True, GIZ_BRANCO)
        instrucao5 = fonte_texto.render("Pressione ENTER para começar.", True, GIZ_AZUL)

        tela.blit(titulo, (LARGURA//2 - titulo.get_width()//2, 80))
        tela.blit(instrucao1, (LARGURA//2 - instrucao1.get_width()//2, 170))
        tela.blit(instrucao2, (LARGURA//2 - instrucao2.get_width()//2, 220))
        tela.blit(instrucao3, (LARGURA//2 - instrucao3.get_width()//2, 270))
        tela.blit(instrucao4, (LARGURA//2 - instrucao4.get_width()//2, 360))
        tela.blit(instrucao5, (LARGURA//2 - instrucao5.get_width()//2, 490))

        # Teclas com borda
        teclas = ["<-", "->"]
        largura_tecla = 45
        altura_tecla = 40
        espaco = 15
        x_inicial = LARGURA//2 - ((largura_tecla + espaco) * len(teclas) - espaco)//2
        y_pos = 410

        for i, tecla in enumerate(teclas):
            retangulo = pygame.Rect(x_inicial + i*(largura_tecla + espaco), y_pos, largura_tecla, altura_tecla)
            pygame.draw.rect(tela, GIZ_BRANCO, retangulo, width=2, border_radius=12)
            texto_tecla = fonte_texto.render(tecla, True, GIZ_AZUL)
            tela.blit(texto_tecla, (retangulo.x + (largura_tecla - texto_tecla.get_width())//2,
                                     retangulo.y + (altura_tecla - texto_tecla.get_height())//2))

        pygame.display.flip()
        clock.tick(60)
