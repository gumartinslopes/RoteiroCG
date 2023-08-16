## Roteiro de Computação gráfica
Implementação de transformações geométricas visualmente em python.

## Setup
Dependências:
 - Python 3

Instalando o projeto
```sh
pip install -r requirements.txt
```
### Executando 
```
python main.py
```

## Transformações geométricas
As transformações geométricas permitem alterar a posição, orientação, tamanho e forma dos objetos em um dado plano.

### Translação
A operação de translação é uma transformação geométrica que move todos os pontos de um objeto ou figura em uma determinada direção e distância a partir de um dado vetor. Soma-se a cada coordenada a distância de translação:

$$
x' = x + t_x, \space 
y' = y +t_y
$$

### Rotação
A rotação é o deslocamento circular de um objeto sobre um ponto.Seja $`\theta`$ o ângulo de rotação, essa operação é definida da seguinte forma no centro do plano cartesiano:
$$
x' = x.cos(\theta) - y .sin(\theta), \newline \space
y' = x.sin(\theta) + y.cos(\theta)
$$

### Espelhamento

Também conhecida como reflexão, representa uma das transformações secundárias. Ela consiste na inversão dos valores das coordenadas referentes à um eixo. Sua operação é definida das seguintes formas:

Espelhamento em relação ao eixo x:

$$
x' = x\space, 
y' = -y
$$

Espelhamento em relação ao eixo y:

$$
x' = -x \space
y' = y
$$

Espelhamento em relação a ambos os eixos

$$
x' = -x\space
y' = -y
$$
