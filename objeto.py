import pygame                                                        #importando biblioteca pygame#
import random


class Personagem(pygame.sprite.Sprite):                              # cria o objeto  rato #
    def __init__(self, x, y ):                                       #construtor do objeto onde x simboliza o plano em x e o y simboliza o plano em y nas coordenadas#
        super().__init__()                                           # chamando construturo da super classe mae#
        self.image = pygame.image.load('rato.png').convert_alpha()   #objeto com imagem do personagem rato#
        self.rect = self.image.get_rect()                            #armazena o retângulo da imagem em rect
        self.rect.x = x                                              #posiciona a imagem nas coordenadas passadas como parâmetro
        self.rect.y = y                                              #posiciona a imagem nas coordenadas passadas como parâmetro

    #método para movimentar o bloco

    def mover(self, x, y):
        self.rect.x = x                                              #posiciona a imagem nas coordenadas passadas como parametro
        self.rect.y = y                                              #posiciona a imagem nas coordenadas passadas como parametro

    #método para movimentar o bloco

    def colide(self, other_sprite):                                  #usando opcao de verificacao de colicao se houve  a colicao e a permanença ele soma
        col = self.rect.colliderect(other_sprite)                    #vai verificar se houve colisão entre os objetos
        if col:                                                      # if para verificar se houvw a colisao se houve a colisa returna 1 se nao retorna 0
            return 1                                                 #retorno 1 para a verdadeiro#
        else:
            return 0                                                 #retorno 0 para falso#

    def morte(self, other_sprite):
        col = self.rect.colliderect(other_sprite)                    #vai verificar se houve colisão entre os objetos e se ocorrer o obejto no caso o rato morre#
        if col:                                                      #if para verificar se houvw a colisao se houve a colisa returna 1 se nao retorna 0 #
            return 1                                                 #retorno 1 para a verdadeiro#
        else:
            return 0                                                 #retorno 0 para a verdadeiro#