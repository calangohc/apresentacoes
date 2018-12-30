%title: VIM - Não é apenas um editor
%author: Magnun Leno
%date: 2015-12-25



\    *·······················* .//.  *·······················*
\    *·VVVVVVVVVVVVVVVVVVVVV·*////// *·VVVVVVVVVVVVVVVVVVVVVVV·*
\    *·VVVVVVVVVVVVVVVVVVVVV·*////// *·VVVVVVVVVVVVVVVVVVVVVVV·*
\    *·VVVVVVVVVVVVVVVVVVVVV·*////// *·VVVVVVVVVVVVVVVVVVVVVVV·*
\     *\··VVVVVVVVVVVVVVVV·*/////////// *·VVVVVVVVVVVVVVVVVV/·*
\       *·VVVVVVVVVVVVVVV·*/////////// *·VVVVVVVVVVVVVVVV/·*
\       *·VVVVVVVVVVVVVVV·*///////// *·VVVVVVVVVVVVVVVV/·*
\       *·VVVVVVVVVVVVVVV·*/////// *·VVVVVVVVVVVVVVVV/`·*
\       *·VVVVVVVVVVVVVVV·*///// *·VVVVVVVVVVVVVVVVV·*
\       *·VVVVVVVVVVVVVVV·*// *·VVVVVVVVVVVVVVVVVV·*
\       *·VVVVVVVVVVVVVVV· ·VVVVVVVVVVVVVVVVVV·*-/////·
\       *·VVVVVVVVVVVVVVV·VVVVVVVVVVVVVVVVVV·*-/////////·
\    ·/ *·VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV·*-/////////////·
\ ///// *·VVVVVVVVVVVVVVVVVVVVVVVVVV*.....//////////////////·
\  ·/// *·VVVVVVVVVVVVVVVVVVVVVVVVV*-iii-·/////////////////·
\    // *·VVVVVVVVVVVVVVVVVVVVVVV*-iiiii-////////////////·
\     / *·VVVVVVVVVVVVVVVVVVVVVVV*-iiii-.///////////////·
\       *·VVVVVVVVVVVVVVVVVVVVV*....... .....////....·  ....
\       *·VVVVVVVVVVVVVVVVVVV*:iiiiiii: :mmmm·..·mmmm·.·mmmm.
\       *·VVVVVVVVVVVVVVVVVV·*/:iiiii`: :mmmmmmmmmmmmmmmmmmm`
\       *·VVVVVVVVVVVVVVVV·*-//:iiii:///:mmm:/ /:mmm:   :mmm:
\       *·VVVVVVVVVVVVVV·*-///:iiii:///:mmm:/  :mmm:   :mmm:
\       *·VVVVVVVVVVVV·*-////:iiiii://:mmm:   :mmm:   :mmm:
\       *·VVVVVVVVVV·* .////:iiiiii://:mmmmm: :mmmmm: :mmmmm:
\       *·VVVVVVVV·*     .//:......://:.....: :.....: :.....:
\        *·······*         .//////////.
\                          .//////.
\                            .//.

-------------------------------------------------

-> Quem sou eu? <-
==================

Graduação       *Engenharia de Elétrica/Telecomunicações*
                 *Analise de Sistemas Orientados a Objeto*

GNU/Linux        *2001*

Atuação          *Analista de Infraestrutura GNU/Linux*

Programador FOSS *Anarchy*, *USB Manager*, *Tiamat*, *C-CairoPlot*
                 *CairPlot*, *Web2py* e *Pelican*

Passatempos      *[MindBending Blog](http://mindbending.org)*
                 *[Hack 'n' Cast](http://hackncast.org)*

-------------------------------------------------

-> # Objetivo da Palestra <-

<br>
* Acabar com a ideia "Everybody hates VIM";
<br>
* Entender o seu "cerne" e design;
<br>
* Acabar com os beeps;
<br>
* Destruir o conceito do i<digita digita digita>ESC:wq<ENTER>
<br>
* Entender que o VIM é o editor DIY;
<br>
* Não tente absorver tudo!


-------------------------------------------------

-> # Sério mesmo?! VIM??? <-

Sim! Motivos...

* Ele é onipresente;
* Não exige ambiente gráfico;
* É leve;
* É oldschool;
* Suporta inúmeras linguagens;
* Customizável, extensível e escriptável;
* Supera até editores atuais (Atom, I'm looking at you!);

-------------------------------------------------




# A long time ago in a galaxy
# far far away...

<br>

* Existiam apenas computadores "centrais"
* Eram utilizados "terminais burros"
* Não era comum o uso de "monitores"
* Os terminais eram lentos!
* O "padrão" de comunicação era a TTY:
	* Teletypewriter ou Teleprinter (imagem!)

<br>
* *1971:* Ken Thompson cria "ed", um line editor
	* Implementa o conceito de modos
	* Quem?
<br>
		* Co-Criador do Unix
		* Co-Criador da linguagem C
<br>
* *1976:* Bill Joy cria "ex", outro line editor
	* Implementa os comandos mais conhecidos do vi
	* Quem?
<br>
		* Co-Criador do BSD-Unix
		* Co-Criador da Sun Microsystems
	* Bill Joy implementa o comando *:visual* ( *:vi* )
<br>
* *1979:* a situação se inverte...
<br>
* *1991:* Bram Moolenaar cria o VIM




-------------------------------------------------

-> # After this, there is no turning back. <-


You take the *blue pill* - the story ends
 you wake up in your bed and believe whatever you want to believe.

You take the *red pill* - you stay in Wonderland
 and I show you how deep the rabbit-hole goes


-> ## Make your choice! <-

-------------------------------------------------

-> # Down the hole we go... <-

Principais modos:
* Comando
* Inserção
* Normal

Mas...
<br>
* Visual
* Select
* Insert
* Ex
* Operator-pending
* Replace
* Virtual Replace
* Insert Normal
* Insert Visual
* Insert Select

<br>
Por quê?
* Bill Joy programava em um ADM-3A terminal.

<br>
Por consequência ele é ergonômicamente correto!
* Keep your damn hands in the Home Row

-------------------------------------------------

-> # Os Modos e o Teclado <-

Você para de trabalhar com o texto e passa a comandar um editor
<br>

Imagem obrigatória...
<br>

Não só pro modo normal...
* para todos os modos o teclado funciona de maneira diferente

-------------------------------------------------

-> # Mudanças de Modos <-

O Modo Normal
* é o centro, permaneça nele o máximo possível.
* Gateway para todos os outros.
* é onde você "esculpe" o código/texto.

Modo de inserção é para pequenas incursões no código/texto.

Exemplos de teclas que te levam para o modo inserção:
* *i* e *I*
* *o* e *O*
* *a* e *A*
* *s* e *S*
* *C*

Teclas que te levam ao modo visual
* *v*, *V*, *Ctrl-v*

Tecla que te levam ao modo de comando
* *:*

Qual tecla que te tira de qualquer modo?

*Exemplo 001*

-------------------------------------------------







-> You have to let it all go, Neo.
-> Fear, doubt, and disbelief.
-> Free your mind.

-------------------------------------------------

-> # Se Movimentando no VIM <-

Paginação *gg* e *G*
Paginação *<ctrl-u>* e *<ctrl-d>*
<br>
Ir diretamente para número de linha *<numer>G*
Ir para porcentagem do arquivo *<numer>%*
<br>
Parágrafos *{* e *}*
Frases *(* e *)*
<br>
Palavras *w*, *W*, *e*, *E*, *b*, *B* e etc
Inicio e fim de linha *0*, *$* e *^*
<br>
Centralizando *zb*, *zt*, *zz*
Saltos na "página virtual" *H*, *m* e *L*
<br>
Saltos entre classes *[[*, *]]*
Saltos entre métodos *[m*, *]m*
<br>
Entre pares *%*
Achar par não "casado" \[(, \[{
<br>
Última inserção *gi*
Último salto *<Ctrl-o>* e *<ctrl-i>*
<br>

Infinitas mais... *:help cursor-motions*

-------------------------------------------------

-> # Conversando com o VIM <-

Similaridade com a linguagem escrita
* Verbos, substantivos, adjetivos, quantitativos...
<br>

<quantitativo><verbo><substantivo><adjetivo>
<br>

Ex:
* apague palavra ( *dw* )
* apague ao redor chaves ( *da}* )
* 3 vezes apague palavra ( *3dw* )
* apague até > ( *dt>* )
* mude dentro da tag ( *cit* )

*Exemplo 002*

-------------------------------------------------

-> # Outras "Teclas Legais" <-

Incremento ( *<Ctrl-a>* ) e decremento ( *<Ctrl-i>* )
<br>
Autocompletar palavra ( *<ctrl-x><ctrl-n>* )
<br>
Autocompletar linha ( *<ctrl-x><ctrl-l>* )
<br>
Autocompletar Sistema de Arquivos ( *<ctrl-x><ctrl-f>* )
<br>
Autocompletar dicionário ( *<ctrl-x><ctrl-k>* )



-------------------------------------------------

-> # Macros <-

As macros no VIM são extremamente poderosas.
Elas gravam uma edição e permitem que esta seja repitida.

*Exemplo 003*
<br>
*Exemplo 004*
<br>
*Exemplo 005*


-------------------------------------------------

-> # Buffers <-

Abra novos arquivos com *:e <fname>*

Liste os buffers com *:ls*

Mude de buffer com *:b1*, *:b2*, *:b3*

Cycle: *:bnext* e *:bprev*

Crie atalhos:
* *nmap <c-tab> :bn<CR>*
* *nmap <c-tab> :bp<CR>*

Execuções batch com bufdo!

-------------------------------------------------

-> # Splits and Windows <-

Vertical/Horizontal: *<c-w>v* / *<c-w>s*

Abrir novos arquivos: *:sp <fname>* / *:vs <fname>*

Movimentação: *<c-w>h*, *<c-w>j*, *<c-w>k* e *<c-w>l*

-------------------------------------------------

-> # Tabs <-

Nova: *:Tabnew*

Listagem: *:Tabs*

Tabs compartilham buffers

Criam “visões” específicas do seu código

-------------------------------------------------

-> # Folds <-

Metodos:
* Manual, Indent, Expression, Marker, Syntax e Diff

Configurar: *:set foldmethod=indent*

Manipulação:
* Toggle: *za*
* Abrir/Fechar: *zo* / *zc*
* Abrir Todas/Fechar Todas: *zR* / *zM*

-------------------------------------------------

-> # UNIX Filosofy <-

Integração com Bash

* sort, uniq, ls, host...

-------------------------------------------------

-> # Conceitos importantes <-

* Marks
* Registers
* Jumps
* Tags (ctags)
* Mappings
* Spell Check
* Formatação

-------------------------------------------------

-> # Plugins <-

Não utilize plugins sem um sistema de plugins!
* vundle
* pathogen
* neobundle
* vim-plug

Plugins Uteis
* Airline
* Emmet-vim
* Syntastic
* UltiSnips
* YouCompleteMe
* NERDTree
* TagBar
* GitGutter
* Rainbow Parenthesis
* Fugitive
* Surround
* Matchit
* Lexima
* Ctrl-P
* EasyMotion
* ZoomWin
* Python PEP8 Indent
* E muitos outros...


-------------------------------------------------

-> # Games <-

* Matrix
* TeTrls
* Sokoban
* Rogue
* Snake
* HJKL
* FlappyVird

-------------------------------------------------

-> # Fontes de Aprendizado <-

Livros Gratuitos
* A Bite of VIM
* VIM Cookbook
* VIM Book

Livros Pagos
* Learing VI and VIM Editors
* Hacking VIM
* Pratical VIM

Vídeos
* VIMCasts
* Derek Wyatt's Videos
* VIMBits

Sites:
* VIM Ninjas
* USE VIM
* VIM Bits
* VIM Awsome
* TIL VIM
* r/vim
* r/vimplugins
* r/vim_magic
* VIM | Stack Overflow

.vimrc's

-------------------------------------------------






-> # Obrigado! <-
