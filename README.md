# gravitus2D

O *gravitus* é um protótipo de simulação de interações gravitacionais feito com a biblioteca [Pygame](https://www.pygame.org/wiki/about).

# Dependências (bibliotecas)
* random
* math
* pygame _v1.9.6_

# Funcionamento

O simulador possui 4 principais módulos:
* Constants
* Particle
* Simulator
* Vector

O primeiro módulo é responsável por armazenar as constantes do programa, como por exemplo, constante gravitacional (**G**), cores e configurações da tela de simulação.

O Módulo **Particle** representa o objeto no espaço (**Simulator**) e faz as interações com outras particulas ao seu redor.

O **Simulator** é o espaço de simulação e é reponsável por fazer com que as parículas possam interagir entre si.

Finalmente, o módulo **Vector** é um módulo auxiliar para trabalhar com vetores bidimensionais.