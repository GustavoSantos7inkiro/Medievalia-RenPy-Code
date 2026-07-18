


define kaiser1 = Character("Kaiser")


image kaiser11 = "Kaiser.png"


define ivy1 = Character("Ivy",who_color="#006400")


image ivy11 = "Ivy.png"


define warlock1 = Character("Warlock",who_color="#CD5C5C")

image warlock11 = "Warlock.png"


define burok1 = Character("Burok",who_color="#A0522D")

image burok11 = "Burok.png"


define revelação1 = Character("Revelação",who_color="#800080")

image revelacao11 = "Revelação.png"


define sabetudo1 = Character("Sabe tudo",who_color="#556B2F")

image sabetudo11 = "Sabetudo.png"


define adaga1 = Character("Adaga")

image adaga11 = "Adaga.png"


define portal1 = Character("Portal")

image portal11 = "Portal.png"


define coelhowarlock1 = Character("Coelhowarlock")

image coelhowarlock11 = "Coelhowarlock.png"


define coelhoivy1 = Character("Coelhoivy")

image coelhoivy11 = "Coelhoivy.png"


define coelhoburok1 = Character("Coelhoburok")

image coelhoburok11 = "Coelhoburok.png"

define kaisermagia1 = Character("Kaisermagia")

image kaisermagia11 = "Kaisermagia.png"

define adagatrack1 = Character("Adagatrack")

image adagatrack11 = "Adagatrack.png"

define capuz1 = Character("Capuz")

image capuz11 = "Capuz.png"

define bauprimeiro1 = Character("Bauprimeiro")

image bauprimeiro11 = "Bauprimeiro.png"

define bausegundo1 = Character("Bausegundo")

image bausegundo11 = "Bausegundo.png"

define bauterceiro1 = Character("Bauterceiro")

image bauterceiro11 = "Bauterceiro.png"

define kaiseradaga1 = Character("Kaiseradaga")

image kaiseradaga11 = "Kaiseradaga.png"


define bauterceirodois1 = Character("Bauterceirodois")

image bauterceirodois11 = "Bauterceirodois.png"


define bausegundodois1 = Character("Bausegundodois")

image bausegundodois11 = "Bausegundodois.png"

define kaiserinvert1 = Character("Kaiserinvert")


image kaiserinvert11 = "Kaiserinvert.png"

define burokinvert1 = Character("Burokinvert")

image burokinvert11 = "Burokinvert.png"



define warlocknvert1 = Character("Warlockinvert")

image warlockinvert11 = "Warlockinvert.png"

define kaiseradagainvert1 = Character("Kaiseradagainvert")

image kaiseradagainvert11 = "Kaiseradagainvert.png"



define kaiseranim = Character("Kaiseranim")


image kaiseranim11 = "Kaiseranim.png"


define ivyanim1 = Character("Ivyanim")


image ivyanim11 = "Ivyanim.png"


define burokanim1 = Character("Burokanim")


image burokanim11 = "Burokanim.png"


define warlockanim1 = Character("Warlockanim")


image warlockanim11 = "Warlockanim.png"


image Bau:

    "images/Bauprimeiro.png"
    linear 1.3
    "images/Bauprimeirodois.png"
    linear 1.3
    "images/Bauprimeirotres.png"
    linear 1.3
    "images/Bauprimeiroquatro.png"
    linear 1.3
    "images/Bauprimeirocinco.png"
    linear 1.3
    "images/Bauprimeiroseis.png"
    linear 1.3
    "images/Bauprimeirosete.png"
    linear 1.3
    "images/Bauprimeirooito.png"


image Bauu:

    "images/Bausegundo.png"
    linear 1.3
    "images/Bausegundodois.png"
    linear 1.3


image Bauuu:

    "images/Bauterceiro.png"
    linear 1.3
    "images/Bauterceirodois.png"
    linear 1.3


image Esfera:

    "images/Esfera.png"
    linear 1.3
    "images/Esferadois.png"
    linear 1.3
    "images/Esferatres.png"
    linear 1.3
    



    
    









label start:

    play music "medievalha.ogg"

    scene bggpark:
        zoom 0.7

    "{i}Tudo começou nas terras distantes e geladas da Noruega Cristalina no ano de 1200 da quinta Era do mundo de Cataris.
    Nosso povo sempre viveu em absoluta paz e felicidade. Até que ultimamente uma sombra teima em pairar sobre nosso reino.{/i}"
    
    
    
    scene bggpark:
        zoom 0.7

    "{i}Para piorar nosso guerreiro sagrado está desaparecido já faz seis anos. E Muitos do nosso povo já o tomam como morto.
    Logo nossas terras geladas, que sempre foram acalentadoras e quentes, agora estão frias e apagadas.{/i}"
    




    scene ferenia:
        zoom 0.7
    show capuz11 at truecenter:
        zoom 1.5
        yalign 0.07



    "{i}Mas em um dia frio, mais precisamente na cidade de Ferenia, a principal cidade da Noruega Cristalina, um homem com um capuz negro encobrindo o rosto caminha pela cidade.{/i}"





    scene ferenia:
        zoom 0.7
    show capuz11 at truecenter:
        zoom 1.5
        yalign 0.07

    "{i}Quem esperava que esse dia chegaria, o Guerreiro sagrado que havia outrora sumido por seis anos retorna à cidade de Ferenia em segredo, seu nome é Kaiser.{/i}"


    scene ferenia:
        zoom 0.7
    show capuz11 at truecenter:
        zoom 1.5
        yalign 0.07

    kaiser1 "Preciso anunciar meu retorno, rever meus grandes amigos e tomar uma bela cerveja. Irei agora à Taverna Central. Tenho boas lembranças deste local. "



    scene taverna:
        zoom 0.7


    stop music fadeout 4.0
    play background "32.ogg"


    show capuz11 at truecenter:
        zoom 1.5
        yalign 0.07

    "{i}A Taverna Central, um dos lugares mais conhecidos do nosso reino, serve como ponto de encontro para os heróis e os moradores locais, onde histórias heroicas são compartilhadas e planos são traçados.{/i}"


    scene taverna:
        zoom 0.7
    show capuz11 at truecenter:
        zoom 1.5
        yalign 0.07


    kaiser1 "Tirarei meu capuz agora e me revelarei ao meu povo e aos meus amigos."


    scene taverna:
        zoom 0.7
    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    "{i}Kaiser então tira seu capuz negro. De repente, todos ali reconhecem Kaiser pelo seu rosto e sua cicatriz no rosto.{/i}"


    scene taverna:
        zoom 0.7

    
    play music "The_Old.ogg"
    play background "32.ogg"
        
   
    show burok11 at right:

        zoom 1.2
        yalign 0.07
        ypos 100
          
    show warlockinvert11 at left:

        zoom 1.5
        ypos 850  
        

    "{i}Logo de cara Kaiser vê em sua frente dois velhos amigos, o anão bárbaro Burok e o mago sábio Warlock.{/i}"

    scene taverna:
        zoom 0.7

    
    show ivy11 at truecenter:

        zoom 1.5
        yalign 0.07
        ypos -50
        

    "{i}Em meio a multidão Kaiser avista uma mulher com orelhas pontudas, ele então reconhece sua velha amiga, a elfa arqueira Ivy. Então o povo começa a festejar a volta do guerreiro Kaiser ao reino da Noruega Cristalina.{/i}"


    scene taverna:
        zoom 0.7

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    "{i}O povo não está feliz à toa, Kaiser é um dos guerreiros sagrados que protegeu por anos a Noruega Cristalina.
    Sua espada e escudo já foram testadas em inúmeras batalhas.{/i}"


    scene taverna:
        zoom 0.7

    show ivy11 at right:

        zoom 1.2
        yalign 0.02
        ypos 50
    show burokinvert11 at left:

        zoom 1.2
        ypos 950
    show warlock11 at center:
        zoom 1.5
        ypos 850


    "{i}Assim também como seus amigos que ele acaba de encontrar na Taverna Central. Todos eles são guerreiros sagrados também. Kaiser, Ivy, Burok e Warlock tem protegido por anos a Noruega Cristalina.{/i}"


    scene taverna:
        zoom 0.7

    show burok11 at truecenter:
        zoom 1.4
        yalign 0.07
        ypos -20

    burok1 "Kaiser, gostaria de falar com você, estamos há muito tempo aqui bebendo e festejando, mas preciso perguntar a você: por onde você andou esse tempo todo?"



    menu:

        "Dizer a verdade":
                jump verdade

        "Mentir":
            jump mentira




label verdade:

    scene taverna:
        zoom 0.7

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    kaiser1 "É difícil de acreditar, mas a pura verdade é que fui feito prisioneiro de um ser cósmico de outra dimensão por seis longos anos."


    scene taverna:
        zoom 0.7

    show ivy11 at truecenter:
        zoom 1.5
        yalign 0.07
        ypos -50

    ivy1 "Acabei escutando a conversa de vocês rapazes, isso é sério Kaiser? E qual o nome deste ser?"



    stop music fadeout 4.0
    stop background fadeout 4.0
    play music "Mysterious.ogg"

    scene dimendoiss:
        zoom 0.7

    


    kaiser1 "{color=#808080}Este ser maligno se autoproclama de A Revelação, ele me ordenou absorver a energia de todos os habitantes da Noruega Cristalina com um artefato que ele me deu.
    Se eu não fizer o que ele quer, ele vai destruir toda alma vivente daqui.{/color}"

    kaiser1 "{color=#808080}Este ser está ficando fraco sem absorver a energia de outros seres, mas pelo que pude presenciar, ele mesmo fraco ainda é muito poderoso.{/color}"

    kaiser1 "{color=#808080}Por isso, temos que nos preparar bem para essa batalha, pois este ser é aterrorizante. Ele me fez escravo por anos porque eu não pude vencer ele sozinho.{/color}"


    scene taverna:
        zoom 0.7

    stop music fadeout 4.0
    play music "The_Old.ogg"
    play background "32.ogg"

    show warlock11 at truecenter:
        zoom 1.5
        ypos 450

    

    warlock1 "Burok acabou de me contar sobre este ser maligno chamado de A Revelação e o plano dele. O que vamos fazer agora?"



    scene taverna:
        zoom 0.7

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    kaiser1 "Precisamos consultar o duende ancião chamado o Sabe-tudo, ele já nos ajudou em outras batalhas contra inimigos terríveis.
    Vamos agora na casa dele que fica a algumas quadras daqui."

    menu:

        "Sair da Taverna":
            jump sair



label mentira:

    scene taverna:
        zoom 0.7

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07


    "{i}Kaiser não quer estragar o clima de alegria na Taverna devido a sua volta, e decide mentir por enquanto para Burok.{/i}"


    scene taverna:
        zoom 0.7

    show kaiserinvert11 at left:
        zoom 1.3
        yalign 0.07

    show burok11 at right:
        zoom 1.2
        yalign 0.07
        ypos 70

    kaiser1 "Burok meu amigo, estive viajando por lugares fantásticos, em uma missão secreta para destruir um grande mal, me perdoe por eu nunca ter mandado cartas para vocês falando sobre meu paradeiro."

    burok1 "Sem problemas Kaiser, o importante é que você está aqui."


    scene taverna:
        zoom 0.7

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    "Então, após comer muito e beber fartamente. Kaiser começa a ouvir uma voz estranha na sua mente. Uma voz de um duende."


    scene taverna:
        zoom 0.7

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    kaiser1 "Que tipo de telepatia é essa?"

    sabetudo1 "Kaiser. Eu sei. Eu sei de tudo. Você precisa contar a verdade para seus amigos o mais rápido possível, e vim até a minha casa, sou eu o duende Sabe-tudo, eu tenho as respostas que você procura."

    kaiser1 "Tudo bem, Sabe-tudo, farei o que você está pedindo."


    scene taverna:
        zoom 0.7

    show kaiserinvert11 at left:
        zoom 1.3
        yalign 0.07

    show burok11 at right:
        zoom 1.2
        yalign 0.07
        ypos 70


    kaiser1 "Burok tenho que lhe falar algo, eu não queria estragar o clima da festa. Então eu menti. Me desculpe. Mas a verdade é o que lhe direi a seguir."

    kaiser1 "É difícil de acreditar, mas a pura verdade é que fui feito prisioneiro de um ser cósmico de outra dimensão por seis longos anos."

    burok1 "Pelas minhas barbas Kaiser!"


    scene taverna:
        zoom 0.7

    show ivy11 at truecenter:
        zoom 1.5
        yalign 0.07
        ypos -50

    ivy1 "Acabei escutando a conversa de vocês rapazes, isso é sério Kaiser? E qual o nome deste ser?"





    stop music fadeout 4.0
    stop background fadeout 4.0
    play music "Mysterious.ogg"
 
    scene dimendoiss:
        zoom 0.7

    

    kaiser1 "{color=#808080}Este ser maligno se autoproclama de A Revelação, ele me ordenou absorver a energia de todos os habitantes da Noruega Cristalina com um artefato que ele me deu.
    Se eu não fizer o que ele quer, ele vai destruir toda alma vivente daqui.{/color}"

    kaiser1 "{color=#808080}Este ser está ficando fraco sem absorver a energia de outros seres, mas pelo que pude presenciar, ele mesmo fraco ainda é muito poderoso.{/color}"


    kaiser1 "{color=#808080}Por isso, temos que nos preparar bem para essa batalha, pois este ser é aterrorizante. Ele me fez escravo por anos porque eu não pude vencer ele sozinho.{/color}"




    scene taverna:
        zoom 0.7

    stop music fadeout 4.0
    play music "The_Old.ogg"
    play background "32.ogg"

    show warlock11 at truecenter:
        zoom 1.5
        ypos 450

    warlock1 "Burok acabou de me contar sobre este ser maligno chamado de A Revelação e o plano dele. O que vamos fazer agora?"


    

    scene taverna:
        zoom 0.7

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    kaiser1 "Precisamos consultar o duende ancião chamado o Sabe-tudo, ele já nos ajudou em outras batalhas contra inimigos terríveis.
    Vamos agora à casa dele, que fica a algumas quadras daqui."

    menu:

        "Sair da Taverna":
            jump sair





label sair:

    


    scene taverna:
        zoom 0.7

    stop background 


    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    menu:

        "Ir andando com Burok até a casa do Sabe-tudo":
                    jump ruaBurok

        "Ir andando com Ivy até a casa do Sabe-tudo":
                    jump ruaIvy

        "Ir andando com Warlock até a casa do Sabe-tudo": 
                    jump ruaWarlock
        


label ruaBurok:

    scene ferenia:
        zoom 0.7

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    kaiser1  "Precisarei da sua força em batalha Burok, seu machado e escudo nos ajudarão nesse grande luta."

    

    hide kaiser11

    show burok11 at truecenter:
        zoom 1.4
        yalign 0.07
        ypos -20

    burok1  "Meu machado arderá pelas chamas da justiça, e nós venceremos mais essa batalha meu amigo."


    

    hide burok11

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    kaiser1 "Chegamos, veja, Ivy e Warlock já estão aqui. Esta é a casa do duende ancião chamado o Sabe-tudo."

    menu:
        "Bater na porta da casa do Sabe-tudo":
                jump casaSabetudo


label ruaIvy:

    scene ferenia:
        zoom 0.7

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    kaiser1  "Precisarei da sua agilidade em batalha, Ivy, seu arco e flecha nos ajudarão nessa grande luta."

    

    hide kaiser11

    show ivy11 at truecenter:
        zoom 1.5
        yalign 0.07
        ypos -50

    ivy1 "Meu arco será tão veloz como a luz e minhas flechas serão certeiras como a primavera, e nós venceremos mais essa batalha Kaiser."


   

    hide ivy11

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    kaiser1 "Chegamos, veja, Burok e Warlock já estão aqui. Esta é a casa do duende ancião chamado o Sabe-tudo."

    menu:
        "Bater na porta da casa do Sabe-tudo":
            jump casaSabetudo


label ruaWarlock:

    scene ferenia:
        zoom 0.7

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07
        



    kaiser1  "Precisarei da sua magia Warlock, sua manipulação do elemento fogo nos ajudará nessa grande luta."

    

    hide kaiser11

    show warlock11 at truecenter:
        zoom 1.5
        ypos 450

    warlock1 "Meu cajado iluminará o caminho mais escuro e nós venceremos mais essa batalha Kaiser."


    

    hide warlock11

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    kaiser1 "Chegamos, veja, Burok e Ivy já chegaram. Esta é a casa do duende ancião chamado o Sabe-tudo."

    menu:
        "Bater na porta da casa do Sabe-tudo":
            jump casaSabetudo      


label casaSabetudo:


    
    

    scene ferenia:
        zoom 0.7


    stop music fadeout 4.0
    play music "31.ogg" noloop
    

    "Toc.. Toc.. Toc.."

    "..."
    


    kaiser1 "Sabe tudo, sou eu, Kaiser! Abra a porta por favor, preciso dos seus conselhos!"

    stop music 
    play music "porta.ogg" noloop
    

    "{i}O Sabe tudo então abre a porta para os quatro guerreiros.{/i}"

    


    scene casasabetudo1

    stop music fadeout 4.0
    play music "nature.ogg"

    show sabetudo11 at truecenter:
        zoom 1.4
        yalign 0.07
        ypos -80

    sabetudo1 "Sejam bem vindos pequenos gafanhotos, eu já sabia que vocês viriam, pois uma sombra vem se instalando em nosso reino e chegou a hora de combater este mal."

    

    sabetudo1 "Porém, lhes aviso de antemão, vocês não conseguirão derrotar este ser por vias normais."


    hide sabetudo11

    show warlock11 at truecenter:
        zoom 1.5
        ypos 450

    warlock1 "Então você já sabia quem era esse ser chamado de A REVELAÇÃO e o plano dele contra a Noruega Cristalina? Realmente, você não tem esse nome em vão."


    hide warlock11

    show sabetudo11 at truecenter:
        zoom 1.4
        yalign 0.07
        ypos -80

    sabetudo1 "Sim. Eu já sabia, pequeno gafanhoto, e lhe aviso que vocês só conseguirão derrotar este ser se tiverem em mãos a Adaga dimensional e a esfera dourada.
    Sorte de vocês que eu tenho esses dois artefatos guardados em algum lugar aqui em casa." 

    sabetudo1 "Deixa eu só procurar a chave que abre os possíveis baús que tem o que vocês precisam."

    sabetudo1 "Hummm."

    sabetudo1 "Aqui talvez."

    sabetudo1 "Ou aqui nesta gaveta talvez."

    sabetudo1 "Achei!"

    sabetudo1 "Aqui está a chave."

    sabetudo1 "Só que você, Kaiser como líder, terá que passar num teste feito por mim. Sim. Isso mesmo."

    hide sabetudo11

    show bauprimeiro11 at right:

        yalign 0.07

    show bausegundo11 at left:

        yalign 0.07

    show bauterceiro11 at truecenter:

        yalign 0.07

    sabetudo1 "Aqui temos três baús. Em um deles está a Adaga dimensional e a esfera dourada. Tome a chave e faça sua escolha e tente descobrir qual é o baú correto que contém os artefatos que vocês precisam."

    menu: 
        "Fazer o teste":
            jump escolha


label escolha:

    hide Bau

    hide Bauu

    show bauprimeiro11 at right:

        yalign 0.07

    show bausegundo11 at left:

        yalign 0.07

    show bauterceiro11 at truecenter:

        yalign 0.07     

    menu:
        "Escolho o baú da direita":
            jump direita

        "Escolho o baú do meio":
            jump meio

        "Escolho o baú da esquerda":
            jump esquerda



label direita:


    scene casasabetudo1

    stop music fadeout 4.0
    play music "falso.ogg" noloop
    

    show Bau at truecenter:
        yalign 0.07

    $ renpy.pause(15)



    sabetudo1 "Você errou. Este baú, na verdade, é o meu Mimic de estimação... hihihi... Não tenha medo, ele só está com um pouco de sono. Tente outra vez."

    

    menu:
        "Tentar de novo":
            jump escolha

    
       




label meio:


    scene casasabetudo1

    stop music fadeout 4.0
    play music "tesouro.ogg" noloop
    

    show Bauuu at truecenter:
    
        yalign 0.07


    $ renpy.pause(10)

    sabetudo1 "Você conseguiu!! Aí está a Adaga Dimensional e a Esfera Dourada!! Errando ou não neste teste eu iria lhe dar eles de qualquer jeito. Só foi uma brincadeira de duende... hihihi... espero que entenda."

    menu:
        "Pegue os itens":
            jump pegar 




label esquerda:


    scene casasabetudo1

    stop music fadeout 4.0
    play music "falso.ogg" noloop
    

    show Bauu at truecenter:
        yalign 0.07


    $ renpy.pause(10)

    sabetudo1 "Você errou. Não tem nada aí. Não faz mal. Tente outra vez."

    menu:
        "Tentar de novo":
            jump escolha






label pegar:

    scene casasabetudo1

    stop music 
    play music "tesouro.ogg" noloop

    show adaga11 at truecenter

    sabetudo1 "Aí está. Esta é a Adaga dimensional, ela servirá para abrir o portal para a dimensão deste ser cósmico e para destruir ele de vez."

    hide adaga11


    play music "tesouro.ogg" noloop

    show Esfera at truecenter:
        yalign 0.07

    sabetudo1 "Esta é a esfera dourada, ela servirá para selar A REVELEÇÃO para sempre."

    hide Esfera




    show burok11 at truecenter:
        zoom 1.4
        yalign 0.07
        ypos -20

    play music "nature.ogg"

    burok1 "Então já temos o necessário, não podemos perder tempo, Kaiser, pois a criatura pode a qualquer momento atacar nosso reino ou ficar mais forte."
    
    hide burok11

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    kaiser1 "Tem razão Burok, vamos abrir logo este portal e ir para a grande batalha!"

    hide kaiser11

    show ivy11 at truecenter:
        zoom 1.5
        yalign 0.07
        ypos -50
    
    ivy1 "Vamos nessa pessoal! Você vem conosco Sabe tudo?"

    hide ivy11

    show sabetudo11 at truecenter:
        zoom 1.4
        yalign 0.07
        ypos -80

    sabetudo1 "Não irei, esta batalha é apenas de cada um de vocês, tão somente de vocês."


    scene ferenia:
        zoom 0.7

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07


    "{i}Então o grupo de heróis deixa casa do Sabe tudo com uma grande esperança em seus corações. Kaiser pergunta então se todos estão preparados para a batalha e todos dizem que sim.{/i}"


    "{i}Kaiser então usa a Adaga dimensional e abre um portal para a dimensão do ser cósmico.{/i}"


    scene ferenia:
        zoom 0.7


    stop music 
    play music "portalsom.ogg"

    show portal11 at truecenter:

        zoom 2.0
        yalign 0.07

    kaiser1 "Vamos, pessoal... Entrem no portal."

    kaiser1 "Chegou o momento."

    ivy1 "Avante!"


    scene dimen:

        zoom 0.7

    stop music fadeout 4.0
    play music "Mysterious.ogg"
    

    show kaiserinvert11 at left:
        zoom 1.2
        ypos 900

    show burok11 at truecenter:
        
        zoom 1.2
        ypos 500

    show ivy11 at right:
        

        zoom 1.2
        yalign 0.02
        ypos 50


    ivy1 "Que lugar mais caótico."

   
    scene dimen:
        zoom 0.7

    show warlock11 at right:
        zoom 1.6
        ypos 870

    show kaiserinvert11 at left:
        zoom 1.5
        yalign 0.07
        



    warlock1 "Existe muita magia nesta dimensão, nunca vi nada igual."


    scene dimen:
        zoom 0.7


    stop music fadeout 4.0
    play music "Menace.ogg"

    show revelacao11 at truecenter:
        zoom 0.7
        yalign 0.07

    "{i}De repente se houve um grande estrondo, e um ser com um grande tentáculo na cabeça aparece. Em vez de pernas, ele tem tentáculos abaixo da cintura. Ele não usa roupas. Sua aparência é assustadora.{/i}"


    scene dimen:
        zoom 0.7

    show revelacao11 at truecenter:
        zoom 0.7
        yalign 0.07

    revelação1 "HA HA HA, Não achei que seriam tão espertos a ponto de conseguirem adentrar no meu reino, mas não adianta, toda a esperança hoje morrerá com a Noruega Cristalina destruída!"

    revelação1 "Sou eu que manipulo emoções e pensamentos, eu que crio a confusão em suas mentes, meus poderes das trevas destrói tudo e a todos."

    scene dimen:
        zoom 0.7

    hide revelacao11


    stop music fadeout 4.0
    play music "FLS.oga"

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    kaiser1 "Vamos amigos, ao ataque!"


    menu:

        "Atacar com Warlock":
            jump War

        "Atacar com Ivy":
            jump Iv

        "Atacar com Burok":
            jump Bur



label War:

    scene dimen:
        zoom 0.7


    show warlockanim11 at truecenter:
        zoom 1.5
        ypos 450

    "{i}Warlock então conjura uma grande bola de fogo com poder sagrado e lança contra a Revelação.{/i}" 

    menu:
        "Atacar com todas as forças":
            jump Revelaçãoataca



label Iv:


    scene dimen:
        zoom 0.7

    show ivyanim11 at truecenter:
        zoom 2.0
        yalign 0.07
        ypos -210

    "{i}Ivy então lança várias flechas imbuídas com poder sagrado contra a Revelação.{/i}"

    menu:
        "Atacar com todas as forças":
            jump Revelaçãoataca


label Bur:

    scene dimen:
        zoom 0.7

    show burokanim11 at truecenter:
        zoom 1.0
        yalign 0.07
        ypos 220

    "{i}Burok então investe com seu machado poderoso com toda brutalidade contra a Revelação.{/i}"


    menu:
        "Atacar com todas as forças":
            jump Revelaçãoataca


label Revelaçãoataca:



    scene dimen:
        zoom 0.7

    show revelacao11 at truecenter:
        zoom 0.7
        yalign 0.07

    "{i}Os guerreiros continuam atacando A REVELAÇÃO só que ela mostra todo o seu poder e transforma Burok, Ivy e Warlock em formas alteradas. Eles são transformados em inofensivos coelhos!{/i}"


    scene dimen:
        zoom 0.7

    show coelhoburok11 at truecenter

    show coelhoivy11 at left

    show coelhowarlock11 at right

    kaiser1 "O que aconteceu com vocês, meus amigos? Seu miserável!"


    scene dimen:
        zoom 0.7



    show revelacao11 at right:

        zoom 0.7
        yalign 0.07



    show kaiseradagainvert11 at left:

        zoom 1.3
        ypos 920



    


    "{i}Kaiser então parte para cima da Revelação e tenta o atacar com a Adaga dimensional.{/i}"

    kaiser1 "Tome isto!"

    
    scene dimen:
        zoom 0.7

    show revelacao11 at truecenter:
        zoom 0.7
        yalign 0.07
    
    "{i}Só que o ser maligno tem outra carta na manga e desfere um dos seus mais poderosos ataques.{/i}"

    

    "{i}O Feitiço da corrupção{/i}"

    scene dimen:
        zoom 0.7


    show kaisermagia11 at truecenter:
        zoom 1.5
        yalign 0.07

    "{i}É agora que Kaiser terá que lutar com todas as forças da sua alma e não se corromper a este maligno feitiço.{/i}"

    

    "{i}A alma de Kaiser agora será testada... Qual lado da balança pesará mais?{/i}"

    

    "{i}Diversas promessas do ser maligno para Kaiser são feitas em sua mente, tentações muito grandes, poder, mulheres, riquezas.{/i}"

    

    "{i}Existem dois caminhos agora.{/i}"

    

    "{i}O caminho Shura onde Kaiser se corrompe pelo poder da Revelação.{/i}"

    "{i}ou{/i}"

    "{i}O caminho do Retorno da paz aonde Kaiser não se deixa levar pelas promessas enganadoras do ser maligno.{/i}"

    

    "{i}É hora de escolher Kaiser.{/i}"



    scene dimen:
        zoom 0.7

    show kaisermagia11 at truecenter:
        zoom 1.5
        yalign 0.07

    menu:
    
        "Escolho o caminho O Retorno da paz":
                    jump paz


        "Escolho o caminho Shura":
                    jump shura


label paz:

    

    scene dimen:
        zoom 0.7

    show revelacao11 at right:

        zoom 0.7
        yalign 0.07



    show kaiseradagainvert11 at left:

        zoom 1.3
        ypos 920



    "{i}Kaiser resiste ao feitiço e não é corrompido pelo ser maligno. Ele então parte para cima da Revelação e tenta o atacar com a Adaga dimensional outra vez. Agora Kaiser está com todo seu poder e coragem.{/i}"

    kaiser1 "Tome isto! Isto acaba agora!"

    "{i}A adaga perfura o corpo do ser cósmico maligno.{/i}"


    scene dimen:
        zoom 0.7

    show revelacao11 at truecenter:
        zoom 0.7
        yalign 0.07

    stop music
    play music "explosao.ogg"

    "{i}A Revelação começa a entrar em colapso.{/i}"

    "{i}O ser maligno começa a gritar constantemente de dor.{/i}"

    "{i}Sua aura sombria começa a ficar muito fraca.{/i}"


    scene dimen:
        zoom 0.7

    show Esfera at truecenter:
        yalign 0.07



    "{i}Kaiser então abre o dispositivo da esfera dourada e usa a esfera dourada para selar o ser para sempre.{/i}"



    stop music fadeout 4.0
    play music "detemi.ogg"

    scene dimen:
        zoom 0.7



    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    "{i}Kaiser resistiu ao feitiço e atacou A REVELAÇÃO com a Adaga dimensional, depois Kaiser selou o ser para sempre na esfera dourada. 
    Seus amigos voltaram a suas formas normais e toda Noruega Cristalina foi salva mais uma vez.{/i}"


    menu:
        "Comemorar a vitória na casa do Sabe-tudo":
                jump casaSabe 
        "Comemorar a vitória na Taverna Central":
                jump tavernaCent



label casaSabe:

    scene casasabetudo1
        

    show kaiserinvert11 at left:

        
        zoom 1.2
        ypos 900


    show sabetudo11 at center:

        zoom 1.0
        ypos 800

    show ivy11 at right:
        zoom 1.2
        yalign 0.02
        ypos 50

    sabetudo1 "Que dia, meus pequenos gafanhotos!! Vocês destruíram um grande mal. Vamos festejar."

    ivy1 "Finalmente acabou. Que alívio."

    kaiser1 "A Noruega Cristalina está a salvo mais uma vez. Viva."


    scene casasabetudo1

    show kaiserinvert11 at left:
        zoom 1.3
        yalign 0.07

    show burok11 at right:
        zoom 1.2
        yalign 0.07
        ypos 70

    

    burok1 "Façamos um brinde ao guerreiro Kaiser que nos salvou mais uma vez."

    

    kaiser1 "Eu não teria conseguido sem vocês."



    scene casasabetudo1
          


    show warlock11 at truecenter:
        zoom 1.5
        ypos 450

    warlock1 "Viva a Noruega Cristalina!"


    scene dimen:
        zoom 0.7

    "{i}Um grande mal se foi. Todo o mundo de Cataris está a salvo agora. E todos estão em festa. O que será que o futuro reserva para os nossos guerreiros? Mais batalhas épicas? Só o futuro dirá.{/i}"
    
    
    scene bggpark:
        zoom 0.7


   
    jump final


label tavernaCent:



    scene taverna:
        zoom 0.7

    show kaiserinvert11 at left:

        
        zoom 1.2
        ypos 900


    show sabetudo11 at center:

        zoom 1.0
        ypos 800

    show ivy11 at right:
        zoom 1.2
        yalign 0.02
        ypos 50

    sabetudo1 "Que dia meus pequenos gafanhotos!! Vocês destruíram um grande mal Vamos festejar."

    ivy1 "Finalmente acabou. Podemos comemorar."

    kaiser1 "A Noruega Cristalina está a salvo mais uma vez. Viva."


    scene taverna:
        zoom 0.7
   
    show kaiserinvert11 at left:
        zoom 1.3
        yalign 0.07

    show burok11 at right:
        zoom 1.2
        yalign 0.07
        ypos 70
    
               

    burok1 "Façamos um brinde ao guerreiro Kaiser que nos salvou mais uma vez."


    kaiser1 "Eu não teria conseguido sem vocês. Hoje as bebidas na Taverna é por minha conta. Bebam e comemorem meu povo."


    scene taverna:
        zoom 0.7
          


    show warlock11 at truecenter:
        zoom 1.5
        ypos 450

    warlock1 "Viva a Noruega Cristalina!"


    scene dimen:
        zoom 0.7

    "{i}Um grande mal se foi. Todo o mundo de Cataris está a salvo agora e todos estão em festa. O que será que futuro reserva para os nossos guerreiros? Mais batalhas épicas? Só o futuro dirá.{/i}"
    
    
    scene bggpark:
        zoom 0.7

          
    
    jump final





label shura:

    stop music fadeout 4.0
    play music "end.ogg"

    scene dimen:
        zoom 0.7

    show kaisermagia11 at truecenter:
        zoom 1.5
        yalign 0.07

    "{i}Kaiser escolheu o caminho Shura, todo heroísmo se foi com o poder da Revelação.{/i}"


    scene dimen:
        zoom 0.7

    show revelacao11 at truecenter:
        zoom 0.7
        yalign 0.07

    revelação1 "Sim. Sim. Kaiser. Você está agora sob meu comando."

    

    revelação1 "Agora lhe ordeno que destrua a Adaga dimensional. Quero ver você destruindo ela com as próprias mãos."

    scene dimen:
        zoom 0.7

    show kaisermagia11 at truecenter:
        zoom 1.5
        yalign 0.07

    "{i}Kaiser escuta o que o ser cósmico ordena.{/i}"

    

    "{i}No entanto{/i}"

    

    "{i}Algo mágico começa a acontecer. Kaiser começa a ouvir uma voz em sua mente, uma telepatia estranha, é a voz do duende Sabe-tudo sussurrando para Kaiser resistir com todas as forças à corrupção.{/i}"


    menu:
        "Resistir com todas as forças do seu ser ao feitiço da corrupção":
                        jump resistir

        "Obedecer à Revelação e destruir a Adaga dimensional":
                        jump destruir


label destruir:


    scene dimen:
        zoom 0.7

    show adagatrack11 at truecenter

       

    "{i}Kaiser destrói a Adaga dimensional, destruindo também toda a esperança do ser cósmico maligno ser destruído.{/i}"

    scene dimen:
        zoom 0.7

    show revelacao11 at truecenter:
        zoom 0.7
        yalign 0.07

    revelação1 "Muito bem Kaiser."


    scene noruegad:
        zoom 0.7

    stop music fadeout 4.0
    play music "end.ogg"
        


    "{i}O Sabe tudo tentou acordar Kaiser do feitiço, mas não conseguiu, Kaiser se tornou um tirano e lutou com a Revelação em várias guerras. A Noruega Cristalina foi destruída.{/i}"

    
    
    "{i}Agora os reinos estão sobre os comandos da Revelação e Kaiser é seu braço direito.{/i}"

    


    
    jump final2


label resistir:

    stop music fadeout 4.0
    play music "FLS.oga"


    scene dimen:
        zoom 0.7

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    "{i}Kaiser luta dentro de si contra o mal. As palavras de incentivo do Sabe tudo na sua mente começa a dar a Kaiser um poder mágico de enfrentar a corrupção.{/i}"

    

    "{i}Kaiser de repente se liberta do feitiço, assustando a Revelação.{/i}"

    hide kaiser11

    show revelacao11 at right:

        zoom 0.7
        yalign 0.07



    show kaiseradagainvert11 at left:

        zoom 1.3
        ypos 920


       

    "{i}Kaiser rapidamente sem dar tempo de reação ao ser o ataca com a Adaga dimensional.{/i}"

    

    kaiser1 "Tome isto!"

    kaiser1 "Isto é por toda alma bondosa do mundo de Cataris."

    scene dimen:
        zoom 0.7

    show revelacao11 at truecenter:
        zoom 0.7
        yalign 0.07

    stop music
    play music "explosao.ogg"

    "{i}A Revelação começa a entrar em colapso.{/i}"

    "{i}O ser maligno começa a gritar constantemente de dor.{/i}"

    "{i}Sua aura sombria começa a ficar muito fraca.{/i}"

    scene dimen:
        zoom 0.7

    show Esfera at truecenter:
        yalign 0.07



    "{i}Kaiser então abre o dispositivo da esfera dourada e usa a esfera dourada para selar o ser para sempre.{/i}"


    scene dimen:
        zoom 0.7

    stop music fadeout 4.0
    play music "detemi.ogg"

    show kaiser11 at truecenter:
        zoom 1.5
        yalign 0.07

    "{i}Kaiser resistiu ao feitiço e atacou A REVELAÇÃO com a Adaga dimensional, depois Kaiser selou o ser para sempre na esfera dourada. 
    Seus amigos voltaram a suas formas normais e toda Noruega Cristalina foi salva mais uma vez.{/i}"


    


    menu:
        "Comemorar a vitória na casa do Sabe-tudo":
                jump casaSabe 
        "Comemorar a vitória na Taverna Central":
                jump tavernaCent



label final:


    scene noruegarestaurada:
        zoom 0.7

    stop music fadeout 4.0
    play music "fogos.ogg"

    "{i}FIM{/i}"
    "..."
    "{i}Obrigado por jogar{/i}"


    stop music

    

    jump finalend


label final2:


    play music "end.ogg"

    scene noruegad:
        zoom 0.7

    
    

    "{i}FIM{/i}"
    "..."
    "{i}Obrigado por jogar{/i}"


    stop music


    jump finalend




label finalend:

    stop music 

    
    
    window hide

    
    scene 1:
        zoom 0.7



    
    $ renpy.pause()






    
    scene 2:
        zoom 0.7



    
    $ renpy.pause()



    scene 3:
        zoom 0.7



    
    $ renpy.pause()



    scene 4:
        zoom 0.7



    
    $ renpy.pause()



    scene 5:
        zoom 0.7



    
    $ renpy.pause()



    scene 6:
        zoom 0.7



    
    $ renpy.pause()
    

    


    return

