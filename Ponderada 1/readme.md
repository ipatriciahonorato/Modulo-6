# Atividade 1: Turtlesim: simulando um ambiente robótico integrado no ROS
# Enunciado

Crie um script em Python capaz de interagir com o nó de simulação do turtlesim e enviar mensagens nos tópicos que regem a locomoção da tartaruga principal. Utilize este script para reproduzir um desenho de sua autoria. Utilize a estrutura de dados que preferir para representar a “imagem” a ser desenhada. O uso de programação orientada a objetos é obrigatório.

## Tecnologias utilizadas

- WSL (Windows Subsystem for Linux);
-  Distribuições Ubuntu e o Debian;
 - Python;
 - ROS (Robot Operating System);
 - Bibliotecas: rclpy (python), time (tempo), geometry_msgs (ROS).

O código é executado no subsistema WSL com as distribuições Ubuntu e o Debian. O python é responsável por controlar a movimentação da tartaruga no ambiente de simulação por meio do ROS, utilizado para comunicação entre os componentes. 

## Código

Para acessar esse código é necessário executar dois comandos em dois terminais no ubuntu.


O primeiro comando abaixo, executa o código que movimenta a simulação:

    cd exemplo
    .
    └── exemplo
        ├── exemplo.py
        └── requirements.txt

1 directory, 2 files

O segundo comando executa a simulação do projeto:

    ros2 run demo_nodes_cpp listener

O código desenvolvido realiza a movimentação de uma tartaruga em um ambiente de simulação por meio do ROS. O objetivo geral desse projeto foi desenhar uma casa com a tartaruga. O programa utiliza o ROS através da biblioteca rclpy em python.

Foram criadas uma classe para controle e movimentação da tartaruga, e funções com método para controle da velocidade e redirecionamento da tartaruga . 

 1. Classe `TurtleController`: Essa classe é definida com um nó do ROS 2 e cria um tópico para enviar informações de publicação da velocidade angular e linear da tartaruga. As mensagens são criadas por meio do `Twist` da biblioteca `geometry_msgs`.
 
 2. Função `move_turtle` e `move`: a função`move` envia mensagens de controle de velocidade da tartaruga considerando a velocidade angular e linear e publica essas informações no método `move_turtle`, e assim, se é realizado a movimentação da tartaruga para as direções desejadas, afim de se formar o objeto de uma casa. Ademais, é utilizado o `time.sleep()` para definir um intervalo de tempo para a movimentação da tartaruga. 
 
 4. Função `main`: instância a classe `TurtleController`e realiza a execução do nó e o encerra após a execução do programa. 

A execução do programa completo pode ser visto no link disposto a seguir: [Ponderada 1 - execução do programa]

O código está disponibilizado em: [Código Ponderada 1]

## Arquivo de referências

Para desenvolvimento desse exercício foi utilizado o material de apoio disponibilizado pelo professor Rodrigo Nicola. O material está presente em: [Ponderada 1 - Módulo 6](https://github.com/Murilo-ZC/Questoes-Trabalhos-Inteli-M6/tree/main/ponderada1)
