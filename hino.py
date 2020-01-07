texto = """\
Salve, lindo pendão da esperança,
Salve, símbolo augusto da paz!
Tua nobre presença à lembrança
A grandeza da Pátria nos traz.

Recebe o afeto que se encerra
Em nosso peito juvenil,
Querido símbolo da terra,
Da amada terra do Brasil!

Em teu seio formoso retratas
Este céu de puríssimo azul,
A verdura sem par destas matas,
E o esplendor do Cruzeiro do Sul.

Recebe o afeto que se encerra
Em nosso peito juvenil,
Querido símbolo da terra,
Da amada terra do Brasil!

Contemplando o teu vulto sagrado,
Compreendemos o nosso dever;
E o Brasil, por seus filhos amado,
Poderoso e feliz há de ser.

Recebe o afeto que se encerra
Em nosso peito juvenil,
Querido símbolo da terra,
Da amada terra do Brasil!

Sobre a imensa Nação Brasileira,
Nos momentos de festa ou de dor,
Paira sempre, sagrada bandeira,
Pavilhão da Justiça e do Amor!

Recebe o afeto que se encerra
Em nosso peito juvenil,
Querido símbolo da terra,
Da amada terra do Brasil!
"""

texto = texto.lower() #converte para minúsculas
#removem espaços, linhas e símbolos de pontuação
texto = texto.replace(" ","")
texto = texto.replace("\n","")
texto = texto.replace(".","")
texto = texto.replace("!","")
texto = texto.replace("?","")
texto = texto.replace(",","")
texto = texto.replace(";","")

#removem acentos e cedilha
texto = texto.replace("á","a")
texto = texto.replace("à","a")
texto = texto.replace("ã","a")
texto = texto.replace("é","e")
texto = texto.replace("ê","e")
texto = texto.replace("í","i")
texto = texto.replace("ó","o")
texto = texto.replace("ô","o")
texto = texto.replace("ú","u")
texto = texto.replace("ç","c")

vogais = 0
consoantes = 0

for caracter in texto:
    if caracter in 'aeiou':
       vogais = vogais + 1
    else:
       consoantes = consoantes + 1
        
print ("Vogais: %d" %vogais)
print ("Consoantes: %d" %consoantes)
print ("Total de letras: %d - %d" %(len(texto), (vogais+consoantes)))
print ('Letra a:', texto.count("a"))
print ('Letra e:', texto.count("e"))
print ('Letra i:', texto.count("i"))
print ('Letra o:', texto.count("o"))
print ('Letra u:', texto.count("u"))