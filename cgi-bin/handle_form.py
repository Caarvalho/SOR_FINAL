#!/usr/bin/env python3

import cgitb
import cgi

personagem = {}
form = cgi.FieldStorage()

username = form.getvalue('apelido')
password = form.getvalue('senha')
genero = form.getvalue('gender')
classe = form.getvalue('class')
dif = form.getvalue('dif')
server = form.getvalue('server')
confirmed = form.getvalue("confirmed")

def salvarPersonagem():
    personagem["nome"] = username
    personagem["senha"] = password
    personagem["genero"] = genero
    personagem["classe"] = classe
    personagem["dificuldade"] = dif
    personagem["server"] = server
        
    try:
        arquivo = open('personagens.txt', 'a', encoding='utf-8')
    except:
        print("DEU RUIM")
    else:
        arquivo.write(f'{personagem}\n')
        arquivo.close()

cgitb.enable()

def montarTabela():
    print("Content-type:text/html\r\n\r\n")
    print("""<html>
                <head>
                    <meta charset=\"UTF-8\">
                    <title>Confirmacao</title>
                </head>
                <body>""")

    print("<h1>Voce confirma esses dados?</h1><hr>")

    print("<table border=1>")
    print("""
            <tr>
            <th>Apelido</th>
            <th>Senha</th>
            <th>Genero</th>
            <th>Classe</th>
            <th>Dificuldade</th>
            <th>Servidor</th>
            </tr>""")
    print("""<tr>
            <td id="nome">{}</td>
            <td id="senha">{}</td>
            <td id="genero">{}</td>
            <td id="classe">{}</td>
            <td id="dificuldade">{}</td>
            <td id="servidor">{}</td>
            </tr>""".format(username, password, genero, classe, dif, server))
    print("</table>")
    print('<a href="../index.html"> Voltar a tela inicial </a>')
    print("<br>")
    print("""
        <button onclick="confirmed()" name="confirmar"> CONFIRMAR</button>
    """)
    print("""<script type="text/javascript">
        function confirmed(){
            var form = document.createElement('form');
            form.method = 'post';
            
            var nome = document.createElement('input');
            nome.name = 'apelido';
            nome.value = document.getElementById("nome").innerHTML;
            form.appendChild(nome);

            var senha = document.createElement('input');
            senha.name = 'senha';
            senha.value = document.getElementById("senha").innerHTML;
            form.appendChild(senha);

            var genero = document.createElement('input');
            genero.name = 'gender';
            genero.value = document.getElementById("genero").innerHTML;
            form.appendChild(genero);

            var classe = document.createElement('input');
            classe.name = 'class';
            classe.value = document.getElementById("classe").innerHTML;
            form.appendChild(classe);

            var dificuldade = document.createElement('input');
            dificuldade.name = 'dif';
            dificuldade.value = document.getElementById("dificuldade").innerHTML;
            form.appendChild(dificuldade);

            var servidor = document.createElement('input');
            servidor.name = 'server';
            servidor.value = document.getElementById("servidor").innerHTML;
            form.appendChild(servidor);

            var confirmado = document.createElement('input');
            confirmado.name = 'confirmed';
            confirmado.value = 'True';
            form.appendChild(confirmado);
                
            form.action = './handle_form.py';
            form.style = 'display: none;';
            document.body.appendChild(form);
            form.submit();
            }
            </script>"""
            )
    print("</body>")
    print("</html>")

def aposConfirmacao():
    print("Content-type:text/html\r\n\r\n")
    print("""<html>
                <head>
                    <meta charset=\"UTF-8\">
                    <title>Confirmacao</title>
                </head>
                <body>""")
    print("<h1> CADASTRO CONCLUIDO </h1>")
    print("<br>")
    print('<a href="../index.html"> Voltar a tela inicial </a>')
    print("</body></html>")


if confirmed != 'True':
    montarTabela()
else:
    salvarPersonagem()
    aposConfirmacao()