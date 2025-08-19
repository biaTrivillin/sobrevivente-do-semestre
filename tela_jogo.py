import pygame
import personagem
from config import BLACK_BG

def tela_jogo(tela):
    # Carrega e redimensiona o fundo
    fundo = pygame.image.load("assets/fundo_jogo.jpg").convert()
    fundo = pygame.transform.scale(fundo, (800, 600))


    # Cria a máscara semi-transparente
    mascara = pygame.Surface((800, 600))
    mascara.set_alpha(190)  # 0 = totalmente transparente, 255 = totalmente opaco
    mascara.fill((0, 0, 0))  # cor da máscara

    # Cria o personagem (tamanho de cada frame: 64x64)
    # jogador = Personagem("assets/personagem_correndo.png", 64, 64, 100, 500)

    personagem_image = pygame.image.load("assets/personagem_correndo.png")
    # personagem = Personagem.get_image(personagem_image, 1, 48, 48, 3, BLACK_BG)
    jogador = personagem.Personagem(personagem_image)

    clock = pygame.time.Clock()
    last_update = pygame.time.get_ticks()
    animacao_colldown = 500
    frame = 0
    rodando = True

    
        
    animacao_list = []

    animacao_steps = 6

    for x in range(animacao_steps):
        animacao_list.append(jogador.get_image(x, 48, 48, 3, BLACK_BG))


    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Detecta teclas pressionadas
        teclas = pygame.key.get_pressed()
        # jogador.mover(teclas)

        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animacao_colldown:
            frame += 1
            last_update = current_time

        # Desenha fundo, máscara e personagem
        tela.blit(fundo, (0, 0))
        tela.blit(mascara, (0, 0))

        # for x in range(animacao_steps):
        tela.blit(animacao_list[frame], (0, 0))
        # tela.blit(jogador, (0, 0))
        # jogador.desenhar(tela)

        pygame.display.flip()
        clock.tick(10)  # controla a velocidade da animação (fps)
