# Gerador de Senhas (Pwdgen)
Este é um projeto Python simples chamado "Pwdgen" que foi criado para gerar senhas aleatórias e salvá-las em um arquivo JSON. Além disso, o projeto inclui uma interface gráfica usando a biblioteca PySimpleGUI, que permite ao usuário gerar senhas, visualizar senhas anteriores e associar as senhas a um site ou aplicativo.


## Funcionalidades
* **Geração de Senhas Aleatórias**: O programa gera senhas aleatórias com base na configuração padrão de 12 caracteres, que consiste em letras maiúsculas e minúsculas, dígitos e caracteres especiais.

* **Salvando Senhas em um Arquivo JSON**: As senhas geradas são salvas em um arquivo JSON chamado 'passwords.json' junto com a data e a hora em que foram geradas.

* **Interface Gráfica Simples**: O programa utiliza o PySimpleGUI para criar uma interface gráfica amigável. Ele permite ao usuário inserir o nome do site ou aplicativo, gerar senhas e visualizar senhas anteriores associadas a esse site.

## Como Usar
1. Execute o programa.
2. Insira o nome do site ou aplicativo para o qual deseja gerar uma senha no campo "Site/Aplicativo".
3. Clique no botão "Gerar Senha" para criar uma senha aleatória e associá-la ao site.
4. Para visualizar senhas anteriores associadas ao mesmo site, clique no botão "Ver Senhas Anteriores".
5. As senhas geradas e as senhas anteriores são exibidas na janela da interface gráfica.

## Dependências
O projeto depende da biblioteca PySimpleGUI para criar a interface gráfica. Você pode instalá-la usando o seguinte comando:
```pip install PySimpleGUI```
