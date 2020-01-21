#encoding:utf-8
import datetime
import os.path
import sqlite3
from time import strptime
from tkinter import messagebox
import urllib.request

from bs4 import BeautifulSoup
from django.utils.html import strip_tags



def abrir_url(url, file):
    try:
        f = urllib.request.urlretrieve(url,file)
    except:
        print  ("Error al conectarse a la pagina")
        return None
    
def extraer_datos(f):
    f = open(f, "r", encoding="utf-8")
    s = f.read()
    soup = BeautifulSoup(s, 'html.parser')
    
    bloque = soup.find_all("div", class_="product-list-type01")
    for b in range(0, len(bloque)):
        items = bloque[b].find_all("div", class_="item")
        for i in range(0, len(items)):
            imagen = "https://www.ktown4u.com/" + items[i].find("span", class_="img").find("img").get("src")
            titulo = items[i].find("span", class_="btxt").getText().replace("(Out Of Stock)","").strip()
            
            if items[i].find("span", class_="ctxt").find("i") is None:
                precioSin=''
            else:
                precioSin = items[i].find("span", class_="ctxt").find("i").string
                
            precioCon = items[i].find("span", class_="ctxt").getText().strip()[-9:].strip()
            
            stxt = items[i].find_all("span", class_="stxt")
            
            if stxt[0].getText()[6:] is '':
                ventas = int(0)
            else:
                ventas = int(stxt[0].getText()[6:].replace(",",""))
            
            fecha = stxt[1].string[1:-1]
            
            lista = []
            lista.append(titulo)
            lista.append(imagen)
            lista.append(precioSin)
            lista.append(precioCon)
            lista.append(fecha)
            lista.append(ventas)
            
            listaListas.append(lista)
    f.close()
    return listaListas
            
#def formatear_fecha(s):
#    partes = s.split("-")
#    fe = "/".join(reversed(partes))
#    return fe

def almacenar_bd():
    conn = sqlite3.connect('album.db')
    conn.text_factory = str
    conn.execute("DROP TABLE IF EXISTS ALBUM")   
    conn.execute('''CREATE TABLE ALBUM
       (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
       TITULO           TEXT    NOT NULL,
       IMAGEN           TEXT    NOT NULL,
       PRECIOSIN           TEXT    NOT NULL,
       PRECIOCON        TEXT     NOT NULL,
       FECHA           DATE    NOT NULL,
       VENTAS           INTEGER    NOT NULL
       );''')
    l = extraer_datos(f)
    for i in l:
        conn.execute("""INSERT INTO ALBUM (TITULO, IMAGEN, PRECIOSIN, PRECIOCON, FECHA, VENTAS) VALUES (?,?,?,?,?,?)""",(i[0],i[1],i[2],i[3],i[4],i[5]))
    conn.commit()
    cursor = conn.execute("SELECT * FROM ALBUM")
    
    if os.path.exists("album.txt"):
        print("HTML was extracted in the past")
    else: 
        archivo = open("album.txt","a",encoding='utf-8')
        
        for row in cursor:
            s = str(row[0]) +'|'+ str(row[1]) +'|'+ str(row[2]) +'|'+ str(row[3])+'|'+ str(row[4])+'|'+ str(row[5])+'|'+ str(row[6])+"\n" 
            print(s)
            archivo.write(str(s))
    
        archivo.close()    
    conn.close()    
    

if __name__ == '__main__':
    f='albums'
    listaListas=[]
    
    for i in range(1,10):
        abrir_url('https://www.ktown4u.com/cat_2nd?grp_no=231307&currentPage=' + str(i),f)
        extraer_datos(f)
    print(listaListas)
    
    almacenar_bd()
