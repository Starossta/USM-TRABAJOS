import re
patron=r"^[\d\s+\-*/()ANS,CUPON]*$"
problemas=open("problemas.txt")
match=re.findall(patron,problemas.read())
sentencias=match[0].strip().split("\n")   #este match es para tener todo el txt en una lista de largo 0 y despues los divido en las sentencia
def filtro(sentencia):
	operador=r"(?:\s+(?:\+|\-|\*|\/\/)\s+)"
	entero=r"\d+"
	clave=r"(?:ANS|(?:CUPON\(\s*(?:\d+|ANS)(?:\s*\,\s*(?:\d+|ANS)\s*)*\)))"
	operacion1=r"\(*(?:" + clave + r"|" + entero + r")\)*" 
	operacion=operacion1 + operador + operacion1 +r"\)*"
	ebnf= operacion +r"(?:" + operador + operacion1 +r")*\s*"
	match=re.match(ebnf,sentencia)
	if match or sentencia=="":
		match2=re.findall(r'\W\(\d+\)', sentencia)   # el unico problema de la expresiones regulares es que detectan (\d) entonces aqui lo elimino
		if len(match2)>=1:
			return False
		else:
			return True
	else:
		return False
#Funcion filtro.
#Esta funcion verifica si el patron cumple con los requisitos pedidos en el ebnf, devuelve true en caso de que cumpla y false en caso contrario

def evaluar(sentencia):
	while "(" in sentencia:
		inicio_par=sentencia.rfind("(")
		fin_par= sentencia.find(")",inicio_par)
		if fin_par==-1:
			break
		expr=sentencia[inicio_par + 1:fin_par]
		resultado=evaluar(expr)
		sentencia = sentencia[:inicio_par] + str(resultado) + sentencia[fin_par + 1:]
	while re.search(r"\*|\/\/",sentencia):
		mul=re.search(r"\d+\s*\*\s*\-*\d+",sentencia)
		div=re.search(r"\d+\s*(\/\/)\s*\-*\d+",sentencia)
		if mul and (not div or mul.start() < div.start()): #aqui se verifica de izquerda a derecha
			match=mul
			numeros=re.findall(r"\-*\d+",mul[0])
			numero1=int(numeros[0])
			numero2=int(numeros[1])
			resultado=numero1*numero2
		elif div:
			match=div
			numeros=re.findall(r"\-*\d+",div[0])
			numero1=int(numeros[0])
			numero2=int(numeros[1])
			if numero2==0:
				return ("ERROR")
				break
			resultado=numero1//numero2
		else:
			break
		sentencia=sentencia[:match.start()] + str(resultado) + sentencia[match.end():]
	while re.search(r"\+|\-",sentencia):
		suma=re.search(r"\d+\s*\+\s*\-*\d+",sentencia)
		resta=re.search(r"\d+\s*\-\s*\-*\d+",sentencia)
		if suma and (not resta or suma.start() < resta.start()): #aqui se verifica de izquerda a derecha
			match=suma
			numeros=re.findall(r"\-*\d+",suma[0])
			numero1=int(numeros[0])
			numero2=int(numeros[1])
			resultado=numero1+numero2
		elif resta:
			match=resta
			numeros=re.findall(r"\-*\d+",resta[0])
			numero1=int(numeros[0])
			numero2=int(numeros[1])
			resultado=numero1-numero2
		else:
			break
		sentencia=sentencia[:match.start()] + str(resultado) + sentencia[match.end():]
	if sentencia=="":
		return
	elif int(sentencia)<0:
		return 0
	else:
		return sentencia
#Funcion evaluar
"""la funcion se basa en evaluar las sentencias ya separadas, evalua linea por linea 
siguiendo el orden, primero parentesis luego multiplicacion y division y finalmente suma y resta, tambien respeta el orden de izquierda a derecha
""" 
def aplicar_cupon(sentencia):
    patron = r"CUPON\(\s*(\d+)\s*(?:,\s*(\d+)\s*)?\)"
    match = re.search(patron, sentencia)
    
    if match:
        x = int(match.group(1))
        y = int(match.group(2)) if match.group(2) else 20
        return str((x * y) // 100)
    
    return sentencia
#Funcion aplicar cupon
#esta funcion se encarga de dar un valor numerico a la expresion cupon()
ANS=0
desarollos=open("desarollos.txt","w")
for x in sentencias:
	desarollos.write(x)
	if filtro(x)==True:
		cupon=aplicar_cupon(x)
		x=re.sub(r"CUPON\(\s*(\d+)\s*(?:,\s*(\d+)\s*)?\)",cupon,x)
		x=x.replace('ANS', str(ANS))
		resultado=evaluar(x)
		if x=="":
			ANS=0
			desarollos.write("\n")
		else:
			ANS=resultado
		if x!="":
			desarollos.write(" = ",)
			desarollos.write(str(resultado))
			desarollos.write("\n")
	else:
		desarollos.write(" = ",)
		desarollos.write("ERROR")
		desarollos.write("\n")
#Aqui es donde se aplican todas las funciones creadas, comenzando por un for en sentencias, para verificar una por una las expresiones
#primero la escribe en el txt, luego verifica si la sentencia pertenece al ebnf dado, si es false escribe "ERROR", en caso que sea verdadero aplicara las demas funciones