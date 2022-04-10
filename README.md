# Battle Code
Ola boas vindas ao meu github aqui voce encontrará o repositorio  [BattleCode](http://battlecode.herokuapp.com)  
Atualmente hospedado no Heroku.  
## Destaque
o destaque do projeto fica na manipulação de dict/json para criar uma automação de geração de torneio de fases
#### Manualmente
```
from battle_code import Fase,createMap
jogadores = [
        Fase('',[
            Fase('',[
                Fase('Silvio',[]),
                Fase('Teste1',[])
            ]),
            Fase('',[
                Fase('Jonas',[]),
                Fase('Teste2',[])
            ]
            )]),
        Fase('',[
            Fase('',[
                Fase('Jubileu',[]),
                Fase('Teste3',[])
            ]),
            Fase('Maicon',[])
        ]),
        Fase('Igor',[]),
        Fase('Mayk',[])]
    Estrutura = createMap(jogadores)[0]
```
#### Automaticamente
```
from battle_code import Fase,createMap
jogadores  = ['silvio','henrique','olaf','maicon']
Estrutura = createMap(jogadores)[0]
```
#### Estrutura
> {"Title':str,'Anterior':[	{"Title':str,'Anterior':[]},	{"Title':str,'Anterior':[]}		]}

#### Progressão 
```
from battle_code import vencedor
Estrutura -> Object Fase
vencedor(Estrutura,name) -> Dict
```
#### Exibição HTML
```
# set Head -> <link href="https://unpkg.com/treeflex/dist/css/treeflex.css" rel="stylesheet">
Estrutura -> Object Fase
#Render Estrutura.to_html()
```
#### Class Fase
```
class Fase():
        def __init__(self,title:str,anterior:list):# anterior Estrutura ou uma lista de objetos Fase
```
