texto, letras = input ('Ingresa tu texto aqui: ').lower(), list (input ('Ingresa 3 letras: ').lower()) #INGRESAR TEXTO Y 3 LETRAS
palabras = len(texto.split()) #CORTA LAS PALABRAS Y CUENTA CADA 1 DE ELLAS PARA LUEGO ALMACENARLAS EN LA VARIABLE "palabras"
l1,  l2 , l3 = texto.count(letras [0]),texto.count(letras [1]),texto.count(letras [2]) # LE ASIGNA A CADA VARIABLE EL NUMERO DE VECES QUE APARECE CADA LETRA EN EL TEXTO
primera_letra, ultima_letra = texto[0], texto[-1] #ALMACENAMOS PRIMERA Y ULTIMA LETRA
texto_invertido = texto[::-1] #INVERTIMOS TEXTO
python =  'Si' if 'python' in texto  else 'No' #UN IF ALTENARIO BASICO PARA SABER SI "python" esta en el texto o no
print (f"Tu primera letra \"{letras[0]}\" aparece {l1} veces, tu segunda letra \"{letras[1]}\" aparece {l2} veces y tu ultima letra \"{letras[2]}\" aparece {l3} veces) \n hay {palabras} palabras  \n la primera letra del texto es  \"{primera_letra}\" y la ultima es \"{ultima_letra}\" \n tu texto invertido es \"{texto_invertido}\" \n ¿La palabra python aparece en el texto? {python}")
#imprimimos el resultado con un formato adecuado y saltos de linea