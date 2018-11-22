import pygame                      #usado para importar bibliteca do pygame#
from objeto import Personagem      #usado para importa obeto do meu arquivo objeto.py#
from random import randrange

#Definindo cores
PRETO = (0, 0, 0)                  #cor usada para determinar o objeto que tira a vida do rato#
BRANCO = (255, 255, 255)           #cor usada para a tela de resultado apos o fim do jogo#
AMARELO = (255,255,0)              #cor usada para determina o alimento do rato no caso o objeto#
AZUL = (0,0,156)                   #cor usada para determinar as cores do placar de pontos durante o jogo #

ImagemFundo = pygame.image.load('fundo.jpeg')  #variavel usada para determinar a cor de fundo do jogo#

#criação da tela

pygame.init()

LARGURA = 600                       #variavel usada para determinar a largura da tela#
ALTURA = 400                        #variavel usada para determinar a largura da tela#
pontos = 0
fonte = pygame.font.SysFont("comicsansms", 30)     #variavel usada  para determinar na tela a fonte do placar durante o jogo#
fonteFim= pygame.font.SysFont("comicsansms", 70)   #variavel usada para determinar o tamanaho da fonte na tela final de jogo#
tela = pygame.display.set_mode([LARGURA, ALTURA])  #variavial que busca as variavies largura e altura e controem a tela#
pygame.display.set_caption("Ratão maluco")         # funcao usada para colocar o Nome do projeto no quanto superiror esquerdo#
mouse = pygame.mouse                               # variavel mouse crida para determinar a funcao do uso de mouse o que encurta encurta o nome
mouse.set_visible(False)                           # funcao usada para esconder  esconde o ponteiro do mouse
clock = pygame.time.Clock()                        # varivael usada para determinar  o tempo da atualizacao da pagina do jogo#


todosObjetos = pygame.sprite.Group()               #lista de objetos na tela#
rato = Personagem(50, 50)                          #determinacao do nascimento do rato na tela quando se inicia#
todosObjetos.add(rato)                             #adcionando rato na lista de objeto para aparecer na tela


def things(thingx, thingy, thingw, thingh, color): #funcao usada para objetos cairem na tela e poderem tanto somar pontos quanto retirar pontos#
    return pygame.draw.rect(tela, color, [thingx, thingy, thingw, thingh])

thing_startx = randrange(0, LARGURA)               #largura em que obistaculo ira nascer
thing_startx2 = randrange(0, LARGURA)              #largura em que obistaculo ira nascer
thing_starty = ALTURA                              #A partir de qual altura vai cair
thing_speed = 7                                    #velocidade que obejeto ira cair
thing_width = 40                                   #tamanho do objeto que esta caindo
thing_width2 = 20                                  #tamanho do objeto que esta na tela  nesse caso o que mata o rato
thing_height = 60                                  #tamanho do objeto que esta na tela  nesse caso o que mata o rato
thing_height2 = 20

morreu = False                                     #se morrer for false ele vai para o final do loop#
sair = False                                       #se for solicitado o fechamento do jogo o jogo fecha

while not sair:                                    #loop para o jogo poder rodar#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    while not morreu:                           #loop usado para verificar se o rato bateu no obstuculo que ira acasionar sua morte#
        filaEventos = pygame.event.get()

        amarelo = things(thing_startx, thing_starty, thing_width, thing_height, AMARELO) #gerar objetos preto que tira a vida do rato#

        preto = things(thing_startx2, thing_starty, thing_width2, thing_height2, PRETO) #funcao para que o objeto na cor amarela almente os pontos do meu rato#

        # percorre a fila de eventos
        for evento in filaEventos:                       #verificar se minha tela esta recendo o evento de fechara tela
            if evento.type == pygame.QUIT:               #if para verificar se o evento e o de quit se for a tela deve ser fechada e finalizado o jogo
                pygame.quit()                            #funcao que faz o jogo fechar se selicionado
                exit()                                   #funcao sair
            if evento.type == pygame.MOUSEMOTION:        #funcao usada para para o rat se mover pelo uso do mouse
                pos = mouse.get_pos()                    #declaracao da variavel para economizar tempo #
                if pos[0] <= 600 and pos[1] <= 600:      #if usado para o rato se mover em determinado espaço dentro da tela#'
                    rato.mover(pos[0], pos[1])
                    if rato.colide(amarelo):               # se o rato colidir com preto retorna 1 e isso faz com q o jogo acabe
                        pontos += 1                      #retorno para determinar que o rato morreu#
                    if rato.morte(preto):              #se o rato estiver no amarelo#
                        morreu = True                    #retorna verdadeiro para que se saiba que o rato continua no jogo#



        tela.blit(ImagemFundo, (0,0))                    # funcao usada para gerar blocos aleatoriamente
        amarelo = things(thing_startx, thing_starty, thing_width, thing_height, AMARELO)

        preto = things(thing_startx2, thing_starty, thing_width2, thing_height2, PRETO)

        thing_starty += thing_speed

        if thing_starty > ALTURA:
            thing_starty = 0 - thing_height
            thing_startx = randrange(0, LARGURA)
            thing_startx2 = randrange(0, LARGURA)

        todosObjetos.draw(tela)
        tela.blit(fonte.render("Pontos: " + str(pontos), True, (AZUL)), (0, 0))
        pygame.display.update()
        clock.tick(60)


    tela.fill(BRANCO)                                                                 # funcao para determina a cor da tela no fim do jogo #
    tela.blit(fonteFim.render("Morreu", True, (PRETO)), (170, 70))                    # funcao para determinar o tamanho da fonte ao  fim do jogo #
    tela.blit(fonteFim.render("Pontos: " + str(pontos), True, (PRETO)), (120, 200))   #funcao para determinar o tamanh da fonte dos ponto durante o jogo#
    pygame.display.update()                                                           #funcao usada para ficar atualizando o q ocorre na tela do jogo#