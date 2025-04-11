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

4. Desenvolvemos a lógica para o **INIMIGO**, incluindo a construção visual com **sprites** animados e um **bot de perseguição** que segue o **"PLAYER"** utilizando coordenadas cartesianas (vetores);
5. utilizando a distância mínima entre o Player e o Inimigo. Quando ocorre a **colisão**, o jogo é encerrado e aparece uma Tela final de Derrota;

6. Estruturamos o **mapa** do jogo por meio de uma **matriz** composta por **0's** (espaços livres) e **1's** (paredes), que define o formato e as barreiras do cenário;

7. Criamos os elementos **coletáveis**:
   - **Calangos**: 5 aparecem aleatoriamente no mapa. Cada um possui uma **IA de fuga**, que os faz se afastar do **"PLAYER"** utilizando a distância máxima entre o Calango e o Player. Ao ser coletado, o **"PLAYER"** recebe um **aumento de velocidade (+0.5)** por 1 segundos;
   - **Sacos de dinheiro**: 2 aparecem aleatoriamente no mapa. Quando coletados, o **"INIMIGO"** é **paralisado por 1 segundo**;

8. Implementamos a lógica de **colisão** entre o **"PLAYER"**, o **"INIMIGO"** e os **"CALANGOS"** com as áreas **sólidas** do mapa (as paredes), impedindo que atravessem barreiras. Para isso, utilizamos conceitos de **direção cartesiana com vetores**;

9. Criamos a tela final do jogo, que é exibida quando ele chega ao fim. O encerramento pode ocorrer de duas maneiras: se o jogador (PLAYER) for capturado por um inimigo (INIMIGO) ou se conseguir coletar os 5 calangos (CALANGOS). Em ambos os casos, uma tela de finalização é exibida por 17 segundos, podendo o jogador aguardar esse tempo ou clicar em "Sair". Independentemente da escolha, o jogo retorna automaticamente para a tela inicial.

10. Por fim, criamos um arquivo **Main** que iremos explicar sua funcionalidade através de um Diagrama de Estados:

![Sem título](https://github.com/user-attachments/assets/e4dda6ca-f37f-49c7-8887-9f2dda50185d)

<h2> ⚙️ FERRAMENTAS: </h2>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg" width="40" height="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="40" height="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" width="40" height="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/trello/trello-original.svg" width="40" height="40" />
          

<h2> 📚 BIBLIOTECAS: </h2>
Pygame, Math para verificar as possíveis direções do INIMIGO para perseguição do PLAYER e Os para centralizar as telas principais do jogo.

<h2> 🎮 DIVISÕES: </h2>

Todos os membros da equipe participaram ativamente do desenvolvimento do projeto, contribuindo de forma colaborativa por meio de canais como Discord e WhatsApp para tirar dúvidas, trocar ideias e propor melhorias. Cada integrante auxiliou na construção do código e na realização de alterações importantes, demonstrando comprometimento e trabalho em equipe ao longo de todo o processo.

Todos os membros da equipe participaram ativamente do desenvolvimento do projeto, contribuindo de forma colaborativa por meio de canais como Discord e WhatsApp para tirar dúvidas, trocar ideias e propor melhorias. Cada integrante auxiliou na construção do código e na realização de alterações importantes, demonstrando comprometimento e trabalho em equipe ao longo de todo o processo.

1. Lucas Cabral <lsc9> : Responsável pela criação da Tela inicial, criação do lógica geral dos botões, criação da lógica do Player e main.
 
2. Gabriel Ferraz <gfaa> : Responsável pela criação dos Sprites, correção da lógica geral e criação da lógica do Player, Lógica da Colisão e Coletáveis.
   
3. Leonilso Souza <lssj> : Responsável pela criação do Mapa, colisão do generalizada do jogo e Bot de perseguição do Inimigo.
 
4. José Ivan <ixvj> : Responsável pela criação do bot de perseguição do Inimigo e coletáveis.

5. Lucas Matheus <lmsf> : Responsável pela criação da tela final de caso de derrota, e auxílio na lógica geral do jogo e criação dos sprites dos personagens e coletáveis.
 
6. Lucas Mendes <lmpa> : Responsável pela criação das coletáveis com Bot de fuga do calango, criação de Sprites e Lógica geral do código.


<h2> 📋 CONCEITOS: </h2>

1. Lógica condicional foi amplamente utilizada em diversas partes do código, permitindo controlar o fluxo do jogo com base em diferentes situações e decisões do jogador.

2. Laços de repetição foram empregados para gerar e atualizar as telas do jogo, bem como para atualizar continuamente os sprites dos personagens e dos itens coletáveis.

3. Listas desempenharam um papel fundamental na construção do mapa, no controle do bot de perseguição do inimigo, no armazenamento das coordenadas cartesianas para detecção de colisões e na organização dos sprites para animações.

4. Operações lógicas e aritméticas foram utilizadas para incrementar valores de velocidade e capturar eventos do teclado, permitindo a atualização dinâmica dos sprites e o controle dos movimentos no jogo.

5. Funções foram definidas e aplicadas em todas as partes do código, contribuindo para a modularização, reutilização e melhor organização da lógica do jogo.

<h2> 😢 DESAFIOS E ERROS: </h2>   

Os maiores desafios encontrados durante o desenvolvimento do projeto envolveram a implementação da lógica que permite a sobreposição correta do Player, Inimigo e Coletáveis sobre o Mapa. Inicialmente, tivemos dificuldades para organizar essa estrutura de forma eficiente. Conseguimos superar esse obstáculo ao corrigir a lógica por meio do uso adequado de herança e da distribuição organizada dos loops em arquivos distintos do projeto, garantindo uma melhor separação de responsabilidades no código.

Outro grande desafio foi a criação do bot de perseguição do Inimigo, que deveria seguir o Player sem colidir com as paredes. A solução inicial não funcionou como esperado, o que nos levou a adotar uma abordagem alternativa baseada na utilização de eixos cartesianos para guiar o inimigo com mais precisão e realismo pelo mapa.

Além disso, um dos maiores entraves no início do desenvolvimento foi compreender e aplicar corretamente os conceitos de Orientação a Objetos (POO). Com o tempo, e com a prática constante, conseguimos assimilar melhor esses conceitos e aplicá-los de maneira mais eficaz na estrutura do nosso jogo.

 [![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=00FF7F&size=35&center=true&vCenter=true&width=1000&lines=CADÊ+O+CALANGUINHO? )](https://git.io/typing-svg)
<div align="center">
  
TELA INICIAL:
![tela inicial](https://github.com/user-attachments/assets/b7a2bc1b-c007-4ecc-bd9a-e2e7c57cf2ab)


TELA DO JOGO COM COLETÁVEIS (CALANGO E BOLSA DE DINHEIRO) E INIMIGO:      
![jogo](https://github.com/user-attachments/assets/34942fd8-e72e-4b12-a3e6-6ba3c13fe3b1)



TELA FINAL DE DERROTA: 
![tela de derrota](https://github.com/user-attachments/assets/c86ff76d-775f-46d1-99f4-51b4c6e0800b)

