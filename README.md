# Imagery Messenger :postbox:

[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)


Ferramenta para fazer o envio de imagens para API do facebook

## Setup

Para instalar o pacote utilize <code> pip install . </code> na raiz do repositório

A instalação das dependências pode ser necessário, utilizando o <code>pip</code>, pode ser feito com

```shell
pip install -r requirements.txt
```

## Implementação

Há uma implementação feita utilizando o pacote, e pode ser utilizado através do <code> app.py </code>

### Argumentos 

A implementação base trabalha através de argumentos, sendo eles

```shell
--input 
```
Utilizado para definir o caminho onde estão as imagens

```shell
--output
```
Utilizado para definir o caminho de saída dos ids

```shell
--token
```
Define o token da API do Facebook

```shell
-h ou --help
``` 
Pode ser utilizado para obter ajuda

```shell
python app.py -h

usage: app.py [-h] [--input INPUT] [--output OUTPUT] [--token TOKEN]

Tool to perform sending images to Facebook API

optional arguments:
  -h, --help       show this help message and exit
  --input INPUT    Sets the path of the folder containing the images that will
                   be sent
  --output OUTPUT  Location where json with ids will be generated
  --token TOKEN    Set the token that will be used
```

## Criando sua própria implementação usando o pacote

Para utilizar o pacote, após realizar a instalação basta importá-lo no código com

```python
from imagery import Imagery
```

Crie a instância da classe, passando obrigatoriamente o <code>token</code> e o <code>input_path</code>
```python
img = Imagery(token, input_path)

# Para enviar as imagens
img.send_image()
```

# ToDo

- :ballot_box_with_check: Envio de imagens
    - JPG;
    - PNG;
    - BMP;
    - TIFF.

- :black_square_button: Envio de vídeos