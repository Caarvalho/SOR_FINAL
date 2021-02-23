import json
def lerPersonagens():
    try:
        arquivo = open('personagens.json', 'r')
    except:
        print("DEU RUIM")
    else:
       return arquivo

personagens = []
arquivo = lerPersonagens()
personagens = json.loads(arquivo.read())
print(personagens)

print("Content-type:text/html\r\n\r\n")
print("""<html>
                <head>
                    <meta charset=\"UTF-8\">
                    <title>Lista de Personagens</title>
                </head>
                <body>""")
print("<div class='center'>")
print("<h1>Personagens Cadastrados</h1><hr>")
print("<br>")

print("<br>")

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
for item in personagens:
    print("""<tr>
                    <td id="nome">{}</td>
                    <td id="senha">{}</td>
                    <td id="genero">{}</td>
                    <td id="classe">{}</td>
                    <td id="dificuldade">{}</td>
                    <td id="servidor">{}</td>
                </tr>""".format(item["nome"], item["senha"], item["genero"], item["classe"], item["dificuldade"], item["server"]))
print("</table>")

print('<a href="../index.html">VOLTAR A TELA INICIAL </a>')
print("</div>")
print(""" <style>
    .center {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
</style>""")

print("</body>")
print("</html>")
arquivo.close() 