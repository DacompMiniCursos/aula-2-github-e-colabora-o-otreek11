# Autoclicker Simples

Pequeno script python para clicar automaticamente alguma tecla ou botão do teclado ou mouse

## Autor

João Guilherme Raposo Lobato

## Pré-requisitos

O script tem como pré-requisito as bibliotecas `mouse`, `keyboard` e `pygame` do python, por questões de conflito em decorrência da versão do python, o script é mais estável quando executado nas versões `3.11.X` do python

## Instalando

Primeiramente você deve confirmar que está utilizando uma versão 3.11.X do python com o comando:

    python --version

Caso apareça qualquer versão que não seja uma 3.11 (ou não apareça nada, caso não tenha python instalado), você deverá instalar uma dessas versões em seu computador, você pode utilizar o [site oficial do python](https://www.python.org) como referência para fazer isso.

Após confirmar que está utilizando a versão correta, eu recomendo criar um ambiente virtual python antes de prosseguir, utilizando o comando (opcional, mas recomendado):

    python -m venv venv

E então ativar o ambiente com seu respectivo comando:

    .\venv\Scripts\Activate.ps1 (Windows/PowerShell)
    venv\Scripts\activate (Windows/CMD)
    source ./venv/bin/activate (Linux)

Seu terminal deve mostrar agora algo como:

    (venv) C:/algum/caminho/aqui/

Agora, você deve instalar as dependências com o comando:

    python -m pip install -r requirements.txt

Após instalar as dependências, você pode executar o script com:

    python autoclicker.py

## Como usar

O script permite você configurar algumas opções internas, como documentado abaixo:

```py
CPS: int = 180                  # quantidade de clicks por segundo
QUIT_KEY: str = 'q'             # tecla de encerramento do script
ONOFF_KEY: str = 'k'            # tecla para ativar/desativar script
CLICKER: str = 'm'              # o dispositivo a clicar, 'k' representa o teclado, 'm' representa o mouse
CLICKED_KEY: str = 'left'       # a tecla ou botão a ser clicada no dispositivo escolhido
```

Após configurar, basta executar novamente o script com `python autoclicker.py` que ele estará ativo novamente com as novas configurações.

## Código de Ética

O script foi criado apenas por fins de aprendizado e de uma forma muito simplificada, por favor não utilize tal script para trapaças ou automações indevidas!