from pprint import pprint


class Fase():
    
    def __init__(self,title,anterior):
        """
        Cria Um Objeto Fase
        :input:
            :title: str
            :anterior: list com Objetos Fase ou list com dicts da Estrutura do Objeto Fase
        """
        self.title = title
        self.anterior = [elemento.to_dict() for elemento in  anterior] if anterior and type(anterior[0]) is Fase else anterior
    
    def to_dict(self):
        """
        Retorna a Estrutura do Objeto Fase
        :return:
            {"Title":str,"Anterior":list}
        """
        return {"Title":self.title,'Anterior':self.anterior}
    def to_html(self,mask={}):
        """
        Retorna a Estrutura HTML para A Visualização Usando o 
        <link href="https://unpkg.com/treeflex/dist/css/treeflex.css" rel="stylesheet">
        """
        return f"""
        <li>
            <span class="tf-nc">{mask[self.title] if self.title in mask else self.title}</span>
            {
            f"<ul>{''.join(list(Fase(elemento['Title'],elemento['Anterior']).to_html(mask) for elemento in self.anterior))}</ul>" if len(self.anterior) > 0 else ""
            }
        </li>
        """


    def win(self,map:list,nome:str):
        """
        Navegação pela Estrutura
        :input:
            :map: list [0,0,1,0,1]
            :nome: str é oque sera definido no Title
        """
        start = 'self.anterior'
        mid = ''.join([f'[{i}]["Anterior"]' for i in map[:-1]])
        end = f"[{map[-1]}]['Title'] = '{nome}'"
        exec(start+mid+end)

def createMap(elementos:list):
    """Recebe Uma Lista Delementos string ou Fase e Cria Uma Estrutura"""
    fases =[]
    childrens = []
    for elemento in elementos:
        user = elemento
        if type(elemento) == str:
            user = Fase(elemento,[])
        childrens.append(user)
        if len(childrens) == 2:
            fases.append(Fase('',childrens))
            childrens = []
    if len(childrens) >= 1:
        return createMap([*fases,*childrens])
    elif len(fases) > 1:
        return createMap(fases)
    return fases

def vencedor(elemento:dict,ganhador:str) -> dict:
    """Recebe um dict ou um objeto Fase e retorna a progreção do ganhador"""
    if type(elemento) == Fase:
        elemento = elemento.to_dict()
    if elemento['Title'] == '':
        if (elemento['Anterior'][0]['Title'] == ganhador and elemento['Anterior'][1]['Title'] != '') or (elemento['Anterior'][1]['Title'] == ganhador and elemento['Anterior'][0]['Title'] != ''):
            elemento['Title'] = ganhador
        else:
            new_elemento = []
            for el in elemento['Anterior']:
                new_elemento.append(vencedor(el, ganhador))
            elemento['Anterior'] = new_elemento
    return elemento
