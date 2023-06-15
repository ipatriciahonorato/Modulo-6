# Atividade 4: Backend para transmissão e armazenamento de imagens

# Enunciado

Desenvolva o software de um backend capaz de receber imagens e armazená-las adequadamente. Não há restrições com relação à tecnologia utilizada.

## Tecnologias utilizadas

-   HTML
-   JavaScript
-   Python
-   YOLOv8 
-   Flask
-   SQLite3
-   Bibliotecas: PIL (Python Imaging Library), Waitress, Ultralytics YOLO.

## Projeto

Este projeto é uma aplicação web que utiliza o modelo YOLOv8 para detecção de objetos em imagens carregadas pelo usuário. Após o processamento no backend e a detecção dos objetos, as coordenadas das caixas delimitadoras são retornadas, desenhadas na imagem e exibidas ao usuário. As imagens processadas também são armazenadas em um banco de dados SQLite3.

## Funcionalidades

-   **Upload de imagem:** O usuário pode fazer upload de uma imagem para ser processada pelo backend.
    
-   **Detecção de objetos:** A imagem é processada pelo modelo YOLOv8 no backend para detecção de objetos. Os objetos detectados e as coordenadas das suas caixas delimitadoras são retornados para o frontend.
    
-   **Exibição dos resultados:** O frontend desenha as caixas delimitadoras dos objetos detectados na imagem e exibe o resultado ao usuário.
    
-   **Armazenamento de resultados:** Os resultados das detecções de objetos são armazenados em uma base de dados SQLite3 com os parâmetros da probabilidade da detecção.

## Principais Funções
 
 ### Script Frontend:
 
1. `EventListener:` Acionada ao selecionar um arquivo de imagem no campo de upload. O arquivo selecionado é então enviado para o servidor através de uma solicitação HTTP POST, utilizando a função `fetch()` do JavaScript.

2. `draw_image_and_boxes()`: Esta função recebe o arquivo de imagem e um array de caixas delimitadoras como parâmetros. E em seguida, desenha as caixas delimitadoras sobre os objetos detectados na imagem.

### Script Servidor:

1. `root():` Esta função é a responsável por lidar com as solicitações GET para a página inicial ("/") do servidor. Ela retorna o conteúdo do arquivo index.html.

3. `detect():` Esta função é o handler para o endpoint "/detect" e é ativada quando uma solicitação POST é enviada para esse endpoint. Ela extrai a imagem do corpo da solicitação, passa a imagem pelo modelo YOLOv8 para detectar objetos, e retorna as coordenadas das caixas delimitadoras dos objetos detectados.

4. `detect_objects_on_image():` Esta função é responsável por aplicar o modelo YOLOv8 em uma imagem e retornar uma lista de caixas delimitadoras dos objetos detectados na imagem. A função também é responsável por salvar as detecções no banco de dados.

A execução do projeto em tempo real pode ser vista no seguinte link: [Execução do Projeto](https://drive.google.com/file/d/122q_V_ry1g4XoiNjRhTc_TD2hSj3DV-m/view?usp=sharing)

A pasta contendo o backend e frontend do projeto está presente em: [Frontend e Backend](https://github.com/ipatriciahonorato/Modulo-6/tree/main/Ponderada%204/Public)

# Material de apoio

-   FreeCodeCamp.org. (2023). "How to Detect Objects in Images Using the YOLOv8 Neural Network". Disponível em: [https://www.freecodecamp.org/news/how-to-detect-objects-in-images-using-yolov8/](https://www.freecodecamp.org/news/how-to-detect-objects-in-images-using-yolov8/). Acesso em: 14 jun. 2023.
    
-   Towards Data Science. (2023). "Enhanced Object Detection: How To Effectively Implement YOLOv8". Disponível em: [https://towardsdatascience.com/enhanced-object-detection-how-to-effectively-implement-yolov8-afd1bf6132ae](https://towardsdatascience.com/enhanced-object-detection-how-to-effectively-implement-yolov8-afd1bf6132ae). Acesso em: 14 jun. 2023.
