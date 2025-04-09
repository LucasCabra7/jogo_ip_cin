<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=66CDAA&height=120&section=header"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=FFFFFF&size=35&center=true&vCenter=true&width=1000&lines=Bem+vindo+ao+Projeto+de+Introdução+à+Programação+CIN)](https://git.io/typing-svg)
<div align="center">

  🤠 **EQUIPE 7:**
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/LucasCabra7">
        <img src="https://avatars.githubusercontent.com/u/155683708?v=4" width="115">
      </a><br>
      <sub>Lucas Cabral (<code>lsc9</code>)</sub>
    </td>
    <td align="center">
      <a href="https://github.com/lucasmatheus21">
        <img src="https://avatars.githubusercontent.com/u/101798673?v=4" width="115">
      </a><br>
      <sub>Lucas Matheus (<code>lmsf</code>)</sub>
    </td>
    <td align="center">
      <a href="https://github.com/Leonilso-Junior-1">
        <img src="https://avatars.githubusercontent.com/u/194504396?v=4" width="115">
      </a><br>
      <sub>Leonilson Souza(<code>lssj</code>)</sub>
    </td>
    <td align="center">
      <a href="https://github.com/joseivann">
        <img src="https://avatars.githubusercontent.com/u/84510651?v=4" width="115">
      </a><br>
      <sub>José Ivan (<code>jixvj</code>)</sub>
    </td>
        <td align="center">
      <a href="https://github.com/gabrielferraz87">
        <img src="https://avatars.githubusercontent.com/u/204758295?v=4" width="115">
      </a><br>
      <sub>Gabriel Ferraz (<code>gfaa</code>)</sub>
    </td>
        <td align="center">
      <a href="https://github.com/lmpaCsharp">
        <img src="https://avatars.githubusercontent.com/u/200678875?v=4" width="115">
      </a><br>
      <sub>Lucas Mendes (<code>lmpa</code>)</sub>
    </td>
  </tr>
</table>

<h2> 🔍 DESCRIÇÃO: </h2>

- A arquitetura do projeto **"Cadê o Calanguinho?"** foi desenvolvida com base nos princípios da **Programação Orientada a Objetos**, seguindo a seguinte estrutura:

1. Desenvolvemos a lógica geral para a construção da interface e funcionamento dos botões interativos;

2. Implementamos a **tela inicial**, com os elementos visuais e os botões **"INICIAR"** e **"SAIR"**, permitindo ao usuário começar ou encerrar o jogo;

3. Criamos a lógica para o personagem principal, o **"PLAYER"**, com a construção da interface utilizando **sprites**, permitindo a troca de animações ao se movimentar para a direita, esquerda, cima e baixo;

4. Desenvolvemos a lógica para o **inimigo**, incluindo a construção visual com **sprites** animados e um **bot de perseguição** que segue o **"PLAYER"**. Quando ocorre a **colisão**, o jogo é encerrado;

5. Estruturamos o **mapa** do jogo por meio de uma **matriz** composta por **0's** (espaços livres) e **1's** (paredes), que define o formato e as barreiras do cenário;

6. Criamos os elementos **coletáveis**:
   - **Calangos**: 5 aparecem aleatoriamente no mapa. Cada um possui uma **IA de fuga**, que os faz se afastar do **"PLAYER"** quando ele se aproxima. Ao ser coletado, o **"PLAYER"** recebe um **aumento de velocidade (+2)** por 2 segundos;
   - **Sacos de dinheiro**: 2 aparecem aleatoriamente no mapa. Quando coletados, o **"INIMIGO"** é **paralisado por 1 segundo**;

7. Implementamos a lógica de **colisão** entre o **"PLAYER"**, o **"INIMIGO"** e os **"CALANGOS"** com as áreas **sólidas** do mapa (as paredes), impedindo que atravessem barreiras. Para isso, utilizamos conceitos de **difereção cartesiana com vetores**;

8. Criamos a **tela final**. O jogo termina de duas formas: caso o **"PLAYER"** seja capturado pelo **"INIMIGO"** ou consiga coletar os 5 **"CALANGOS"**. Em ambos os casos, é exibida uma tela de encerramento com os botões **"JOGAR NOVAMENTE"** e **"SAIR"**, conforme o desfecho.

9. Por fim, criamos um arquivo **Main** que importa a tela inicial e verifica qual o botão está sendo precionado para iniciar o jogo ou sair.

<h2> ⚙️ FERRAMENTAS: </h2>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg" width="40" height="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="40" height="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" width="40" height="40" />

<h2> 📚 BIBLIOTECAS: </h2>
Pygame, Math para verificar as possíveis direções do INIMIGO para perseguição do PLAYER e Os para centralizar as telas principais do jogo.

<h2> 🎮 DIVISÕES: </h2>

1. Lucas Cabral (<code>lsc9</code>): Responsável pela criação da Tela inicial, criação do lógica geral dos botões, criação da lógica do Player e main.
2. Gabriel Ferraz (<code>gfaa</code>): Reponsável pela criação dos Sprites, correção da lógica geral e criação da lógica do Player.
3. Leonilso Souza (<code>lssj</code>): Responsável pela criação do Mapa, colisão do geral dos personagens com as paredes do mapa.
4. José Ivan (<code>jixvj</code>): Responsável pela criação do Inimigo e bot de perseguição do Inimigo contra o player.
5. Lucas Matheus (<code>lmsf</code>): Responsável pela criação da tela final e criação dos sprites dos personagens e coletavéis.
6. Lucas Mendes (<code>lmpa</code>): Responsável pela criação das coletáveis do calango e bot de fuga do calango.

<h2> 📋 CONCEITOS: </h2>

1. Lógica de condicionais utilizados em toda parte parte do código.
2. Loop de repetição utilizado para gerar as imagens e atualizar os Sprites dos personagens e coletáveis.
3. Listas para criação do Mapa e perseguição do Inimigo.
4. Lógica operacionais para incrementar valores de velocidade ou teclas para atualizações de sprites.
5. Funções para atribuir em todas as partes do código.

<h2> 😢 DESAFIOS E ERROS: </h2>   

Os maiores desafios foi entender a lógica para incrementar o  Player, Inimigo e Coletaveis tudo sobreposto ao Mapa. Contornamos a ideia, corrigindo a lógica utilizando corretamente Herançcas. Em seguida a outra maior dificuldade que enfretamos foi com o bot de perseguição do Inimigo para o Player e orienta-ló a percorrer sem colisão com as paredes, utilizamos outro metodo para orientar o bot de perseguição utilizando eixos cartesianos. 
Os maiores erros de inicio foi entender Orientação a Objetos.

 [![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=00FF7F&size=35&center=true&vCenter=true&width=1000&lines=CADÊ+O+CALANGUINHO? )](https://git.io/typing-svg)
<div align="center"> 

![tela incial](https://github.com/user-attachments/assets/2af143c1-7afd-4131-b166-664f1f61a33c)

![jogo](https://github.com/user-attachments/assets/ac9e24e7-626d-45b6-bd91-02e2d4aad07f)

