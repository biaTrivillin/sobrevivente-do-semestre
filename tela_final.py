import pygame
import sys
import math
from config import LARGURA, ALTURA, GIZ_BRANCO, GIZ_AZUL, FONTE_TITULO_PATH, FONTE_TITULO_SIZE, FONTE_TEXTO_PATH, FONTE_TEXTO_SIZE

def tela_final(tela):
    pygame.font.init()
    fonte_titulo = pygame.font.Font(FONTE_TITULO_PATH, FONTE_TITULO_SIZE)
    fonte_texto = pygame.font.Font(FONTE_TEXTO_PATH, FONTE_TEXTO_SIZE)

    clock = pygame.time.Clock()
    rodando = True

    # Valores fictícios para teste
    pontos = 75
    status = "APROVADO" if pontos >= 60 else "REPROVADO"
    cor_status = (0, 255, 0) if status == "APROVADO" else (255, 0, 0)

    inicio = pygame.time.get_ticks()
    animacao_status = False
    escala_status = 5.0  # Começa grande para efeito de carimbo
    status_apareceu = False

    while rodando:
        tempo_atual = pygame.time.get_ticks() - inicio

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and tempo_atual > 3500:
                    rodando = False

        # Fundo preto
        tela.fill((0, 0, 0))

        # Fim do jogo - aparece com fade-in
        alpha_titulo = min(255, int((tempo_atual / 1000) * 255))
        titulo_surface = fonte_titulo.render("Fim de Jogo", True, GIZ_BRANCO)
        titulo_surface.set_alpha(alpha_titulo)
        tela.blit(titulo_surface, (LARGURA//2 - titulo_surface.get_width()//2, 80))

        # Pontos - aparece depois de 1s com fade-in
        if tempo_atual > 1000:
            alpha_pontos = min(255, int(((tempo_atual - 1000) / 1000) * 255))
            pontos_surface = fonte_texto.render(f"Seus pontos: {pontos}", True, GIZ_BRANCO)
            pontos_surface.set_alpha(alpha_pontos)
            tela.blit(pontos_surface, (LARGURA//2 - pontos_surface.get_width()//2, 200))

        # Status (APROVADO/REPROVADO) - efeito carimbo depois de 2s
        if tempo_atual > 2000:
            if not animacao_status:
                animacao_status = True
                status_apareceu = True

            if status_apareceu and escala_status > 1.0:
                escala_status -= 0.3  # Diminui rápido até 1.0

            if escala_status < 1.0:
                escala_status = 1.0  # Trava no tamanho normal

            texto_status = fonte_titulo.render(status, True, cor_status)
            largura = int(texto_status.get_width() * escala_status)
            altura = int(texto_status.get_height() * escala_status)
            texto_animado = pygame.transform.scale(texto_status, (largura, altura))

            tela.blit(texto_animado, (LARGURA//2 - texto_animado.get_width()//2, 300))

        # Instrução - aparece depois de 3s
        if tempo_atual > 3000:
            alpha_instrucao = min(255, int(((tempo_atual - 3000) / 1000) * 255))
            instrucao_surface = fonte_texto.render("Pressione ENTER para sair", True, GIZ_AZUL)
            instrucao_surface.set_alpha(alpha_instrucao)
            tela.blit(instrucao_surface, (LARGURA//2 - instrucao_surface.get_width()//2, 500))

        pygame.display.flip()
        clock.tick(60)
