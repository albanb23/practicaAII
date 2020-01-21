#encoding: UTF-8
from os import path

from main.models import Album


def deleteTable():
    Album.objects.all().delete()

def populateDB():
    print('Loading albums...')
    
    fileobj = open("trabajoAII/data/album.txt", "r", encoding="utf8")
    line = fileobj.readline()
    while line:
        rip = line.split('|')
        if len(rip)>1:
            idA = rip[0]
            tit = rip[1]
            im = rip[2]
            po = rip[3]
            pd = rip[4]
            fe = rip[5]
            ve = rip[6][:-1]
            
            
            Album.objects.create(albumId=idA, titulo=tit, imagen=im, precioOriginal=po, precioDescuento=pd, fecha=fe, ventas=ve)       
        line= fileobj.readline()
    fileobj.close()
    
    print("Albums inserted: " + str(Album.objects.count()))