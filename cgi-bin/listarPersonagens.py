
def lerPersonagens():
    try:
        arquivo = open('personagens.txt', 'r')
    except:
        print("DEU RUIM")
    else:
       return arquivo


arquivo = lerPersonagens()


print("Content-type:text/html\r\n\r\n")
print("""<html>
                <head>
                    <meta charset=\"UTF-8\">
                    <title>Lista de Personagens</title>
                </head>
                <body>""")

print("<h1>Personagens Cadastrados</h1><hr>")
print("<br>")
print('<a href="../index.html">VOLTAR A TELA INICIAL </a>')
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
for item in arquivo:
    item = item.split(",")
    print("""<tr>
                <td id="nome">{}</td>
                <td id="senha">{}</td>
                <td id="genero">{}</td>
                <td id="classe">{}</td>
                <td id="dificuldade">{}</td>
                <td id="servidor">{}</td>
            </tr>""".format(item[0].replace("{'nome':", "").replace("'", ""),
            item[1].replace("'senha':", "").replace("'", ""), 
            item[2].replace("'genero':","").replace("'", ""),
            item[3].replace("'classe':", "").replace("'", ""),
            item[4].replace("'dificuldade':", "").replace("'", ""),
            item[5].replace("'server':", "").replace("'", "").replace("}", "")))
print("</table>")


print("</body>")
print("</html>")
arquivo.close() 