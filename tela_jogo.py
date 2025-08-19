import pygame
import random
import personagem
from config import BLACK_BG

# Classe para itens
class Item:
    def __init__(self, largura_tela):
        self.x = random.randint(20, largura_tela - 20)
        self.y = -20
        self.velocidade = random.randint(3, 6)
        self.tipo = random.choice(["verde", "vermelho"])  # verde = coletar, vermelho = desviar
        self.raio = 15

    def update(self):
        self.y += self.velocidade

    def desenhar(self, tela):
        if self.tipo == "verde":
            cor = (0, 255, 0)
        else:
            cor = (255, 0, 0)
        pygame.draw.circle(tela, cor, (self.x, self.y), self.raio)

    def get_rect(self):
        return pygame.Rect(self.x - self.raio, self.y - self.raio, self.raio * 2, self.raio * 2)


def tela_jogo(tela):
    largura_tela, altura_tela = 800, 600

    fundo = pygame.image.load("assets/fundo_jogo.jpg").convert()
    fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

    mascara = pygame.Surface((largura_tela, altura_tela))
    mascara.set_alpha(190)  
    mascara.fill((0, 0, 0)) 

    personagem_image = pygame.image.load("assets/personagem_correndo.png")
    jogador = personagem.Personagem(personagem_image)

    clock = pygame.time.Clock()

    animacao_list_direita = []
    animacao_list_esquerda = []
    animacao_steps = 6
    for x in range(animacao_steps):
        img = jogador.get_image(x, 24, 48, 4, BLACK_BG)
        animacao_list_direita.append(img)

        img_flip = pygame.transform.flip(img, True, False)
        img_flip.set_colorkey(BLACK_BG)
        animacao_list_esquerda.append(img_flip)

    frame = 0
    last_update = pygame.time.get_ticks()
    animacao_colldown = 100  

    rodando = True
    andando = False
    olhando_esquerda = False

    x_pos = 400
    y_pos = 400
    velocidade = 5

    largura_sprite = animacao_list_direita[0].get_width()
    altura_sprite = animacao_list_direita[0].get_height()

    # Lista de itens
    itens = []
    item_timer = 0
    spawn_cooldown = 1000  # ms

    # Pontuação
    pontos = 0
    fonte = pygame.font.SysFont(None, 36)

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

        teclas = pygame.key.get_pressed()
        andando = False

        if teclas[pygame.K_RIGHT]:
            x_pos += velocidade
            andando = True
            olhando_esquerda = False

        elif teclas[pygame.K_LEFT]:
            x_pos -= velocidade
            andando = True
            olhando_esquerda = True

        if x_pos < 0:
            x_pos = 0
        if x_pos > largura_tela - largura_sprite:
            x_pos = largura_tela - largura_sprite

        if andando:
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= animacao_colldown:
                frame = (frame + 1) % animacao_steps
                last_update = current_time
        else:
            frame = 0

        # --- Spawn de itens ---
        current_time = pygame.time.get_ticks()
        if current_time - item_timer >= spawn_cooldown:
            itens.append(Item(largura_tela))
            item_timer = current_time

        # Atualiza itens
        for item in itens[:]:
            item.update()
            if item.y > altura_tela:
                itens.remove(item)

        # --- Colisão ---
        rect_jogador = pygame.Rect(
            x_pos,
            y_pos + altura_sprite // 2,   # começa no meio do personagem
            largura_sprite,
            altura_sprite // 2            # só metade inferior
        )
        for item in itens[:]:
            if rect_jogador.colliderect(item.get_rect()):
                if item.tipo == "verde":
                    pontos += 1
                else:
                    pontos -= 1
                itens.remove(item)

        # Render
        tela.blit(fundo, (0, 0))
        tela.blit(mascara, (0, 0))

        if olhando_esquerda:
            imagem = animacao_list_esquerda[frame]
        else:
            imagem = animacao_list_direita[frame]

        tela.blit(imagem, (x_pos, y_pos))

        for item in itens:
            item.desenhar(tela)

        # Pontuação
        texto = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
        tela.blit(texto, (10, 10))

        pygame.display.flip()
        clock.tick(60)
