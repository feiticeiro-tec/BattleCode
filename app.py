from flask import Flask,render_template,request,session,redirect,url_for
from battle_code import Fase,createMap,vencedor
import json
app = Flask(__name__)
app.secret_key='secreto'

@app.route('/')
def index():
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
    session['Estrutura'] = Estrutura.to_dict()
    Estrutura = Estrutura.to_html()
    return render_template('index.html',Estrutura=Estrutura)
@app.route('/start',methods=['GET','POST'])
def start():
    if request.method == 'POST':
        jogadores  = list(nome for nome in request.form)
        if len(jogadores) >1:
            Estrutura = createMap(jogadores)[0]
            session['Estrutura'] = Estrutura.to_dict()
            Estrutura = Estrutura.to_html()
        else:
            Estrutura = ''
    else:
        Estrutura =  session.get('Estrutura') or ''
        if Estrutura:
            Estrutura = Fase(Estrutura['Title'], Estrutura['Anterior'])
            Estrutura = Estrutura.to_html()
        else:
            return redirect(url_for('index'))
    return render_template('battle.html',Estrutura=Estrutura)

@app.route('/ganhador',methods=['GET','POST'])
def ganhou():
    if request.method == 'POST':
        Estrutura =  session.get('Estrutura') or ''
        if Estrutura:
            Ganhador =  request.form.get('ganhador')
            if Ganhador:
                Estrutura = Fase(Estrutura['Title'], Estrutura['Anterior'])
                Estrutura = vencedor(Estrutura,Ganhador)
                Estrutura = Fase(Estrutura['Title'],Estrutura['Anterior'])
                session['Estrutura'] = Estrutura.to_dict()
    return redirect(url_for('start'))
@app.route('/zerar')
def zerar():
    session['Estrutura'] = None
    return redirect(url_for('index'))




