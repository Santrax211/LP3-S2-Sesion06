noticia = open("noticia.txt","rt")
datos_noticia = noticia.read()
print(datos_noticia)

noticia = open("noticia.txt","rt",encoding='utf8')
datos_noticia = noticia.read()
print(datos_noticia)
