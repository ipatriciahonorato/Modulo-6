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
 - Bibliotecas: Bibliotecas: rclpy (python), math (math), geometry_msgs (ROS), nav_msgs (ROS). 

O código é executado no subsistema WSL com as distribuições Ubuntu e o Debian. O python é responsável por controlar a movimentação o robô TurtleBot3 Burger no ambiente de simulação Gazebo por meio do ROS, utilizado para comunicação entre os componentes.



## Código/Pacote

Para acessar esse código é necessário executar dois comandos em dois terminais no ubuntu.


Para execução do script `controller.py` , é necessário baixar o pacote para o computador e executar o código de controle do robô no vscode, pois a movimentação do robô ocorre apenas após essa execução.

O ambiente de simulação do gazebo é iniciado por meio do comando abaixo:

    ros2 launch turtlebot3_gazebo empty_world.launch.py


O objetivo desse projeto foi controlar a movimentação do robô TurtleBot3 em um ambiente de simulação do Gazebo por meio do ROS, fazendo-o mover-se para frente por 5 metros e depois retornar à posição inicial. 

Foram criadas uma classe para controle e movimentação do TurtleBot3, e funções com método para controle da velocidade e redirecionamento do robô.

 1. Classe `TurtleController`: Essa classe é definida com um nó do ROS 2 e cria um tópico para enviar informações de publicação da velocidade angular e linear do TurtleBot3. As mensagens são criadas por meio do `Twist` da biblioteca `geometry_msgs`.
 
 2. Função `__init__(self)`: A função define a criação de um publicador que publica mensagens no tópico "/cmd_vel" e um subscritor que se inscreve no tópico "/odom". Estes tópicos são usados para controle de movimento de robôs e recebimento de informações de odometria.
 
 4. Função `odom_callback(self, msg)`: Essa função é um callback chamada quando nova mensagem é recebida no tópico "/odom". A mensagem recebida é passada para a função como o parâmetro `msg`.
 
 5. Função `move_straight e stop_moving`: função move_straight envia mensagens de controle de velocidade do TurtleBot3 considerando a velocidade linear e publica essas informações no método move_straight, fazendo o robô mover-se para frente ou para trás. A função stop_moving é utilizada para parar o movimento do robô. Ademais, é utilizado o math.sqrt para calcular a distância percorrida pelo robô. 
 
 6. Função `main`: instância a classe `TurtleController`e realiza a execução do nó e o encerra após a execução do programa. 

A execução do programa completo pode ser visto no link disposto a seguir: [Ponderada 2 - execução do programa](https://drive.google.com/file/d/1KqXuVnSn0EWh397fOX4JjLtbeFyAlC9c/view?usp=sharing)

O código principal do projeto está disponível em: [Código Ponderada 2](https://github.com/ipatriciahonorato/Modulo-6/blob/main/Ponderada%202/ponderada_2/controller.py)
