# Atividade 2: Simulação de robôs móveis com Gazebo
# Enunciado

Crie um pacote em ROS capaz de interagir com uma simulação feita no Gazebo de modo que a plataforma simulada do turtlebot3 seja capaz de mover-se de maneira controlada.

-   Interagir com os tópicos e/ou serviços do turtlebot3 de modo a conseguir mandar comandos de velocidade e extrair dados de odometria.
-   Conceber uma estrutura de dados capaz de armazenar a série de movimentos que devem ser feitos pelo robô para chegar no objetivo.
-   Implementar uma rota pré-estabelecida

## Tecnologias utilizadas
- WSL (Windows Subsystem for Linux);
- Distribuições Ubuntu e o Debian;
- Python;
- ROS (Robot Operating System);
- Gazebo;
 - Bibliotecas: Bibliotecas: rclpy, math, geometry_msgs, nav_msgs. 

## Código/Pacote

O objetivo desse projeto foi controlar a movimentação do robô TurtleBot3 em um ambiente de simulação do Gazebo por meio do ROS, fazendo-o mover-se para frente por 5 metros e depois retornar à posição inicial. 

Foram criadas uma classe para controle e movimentação do TurtleBot3, e funções com método para controle da velocidade e redirecionamento do robô.

 1. Classe `TurtleController`: Essa classe é definida com um nó do ROS 2 e cria um tópico para enviar informações de publicação da velocidade angular e linear do TurtleBot3. 
 
 2. Função `__init__(self)`: A função define a criação de um publicador que publica mensagens no tópico "/cmd_vel" e um subscritor que se inscreve no tópico "/odom". 
 
 4. Função `odom_callback(self, msg)`: Essa função é um callback chamada quando nova mensagem é recebida no tópico "/odom". 
 
 6. Função `move_straight e stop_moving`: função move_straight envia mensagens de controle de velocidade do TurtleBot3 considerando a velocidade linear e publica essas informações no método move_straight, fazendo o robô mover-se para frente ou para trás. A função stop_moving é utilizada para parar o movimento do robô. Ademais, é utilizado o math.sqrt para calcular a distância percorrida pelo robô. 
 

A execução do programa completo pode ser visto no link disposto a seguir: [Ponderada 2 - execução do programa]()

O código principal do projeto está disponível em: [Código Ponderada 2](https://github.com/ipatriciahonorato/Modulo-6/blob/main/Ponderada%202/ponderada_2/controller.py)
