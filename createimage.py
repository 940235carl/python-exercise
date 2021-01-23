import random, math
import PIL.Image as Image
import colorsys
import numpy as np


def MSE(np,op,bs):
    imageSize1 = 768
    imageSize2 = 512
    totales = 0
    for x in range(0,imageSize1):
        for y in range(0,imageSize2):
            r = np[x,y][0]-op[x,y][0]
            g = np[x,y][1]-op[x,y][1]
            b = np[x,y][2]-op[x,y][2]
            #print(r,g,b)
            totales = totales + (r*r+g*g+b*b)
            
    totales = totales/bs
    mse = totales/(imageSize1*imageSize2)
    
    return mse
    
    
if __name__ == "__main__":
    imageSize1 = 768
    imageSize2 = 512
    # 以下為嵌入信息
    image = Image.open("kodim03.png").convert('RGB')
    
    pixel = image.load()
    
    random.seed(1)
    
    g = [random.randint(0,2) for _ in range(3)]
    #print(g[0],g[1],g[2])
    
    b = 3;
    for x in range(0,imageSize1):
        for y in range(0,imageSize2):
            for z in range(3):
                P = pixel[x,y][z]
                P1 = (P-(P%b))+g[z]
                P2 = P1+b
                P3 = P1-b
                if P2> 255: 
                    if abs(P1-P) < abs(P3-P):
                        PP = P1
                    else:
                        PP = P3
                elif P3< 0:
                    if abs(P1-P) < abs(P2-P):
                        PP = P1
                    else:
                        PP = P2
                else:
                    ch = min(abs(P1-P),abs(P2-P),abs(P3-P))
                    if ch == abs(P1-P):
                        PP = P1
                    elif ch == abs(P2-P):
                        PP = P2
                    else:
                        PP = P3
                if z == 0 :
                    image.putpixel((x,y),(PP,pixel[x,y][1],pixel[x,y][2]))
                if z == 1 :
                    image.putpixel((x,y),(pixel[x,y][0],PP,pixel[x,y][2]))
                if z == 2 :
                    image.putpixel((x,y),(pixel[x,y][0],pixel[x,y][1],PP))
     
        
    image.save("resff.png")
    
    
    #以下為讀取信息，算取信息mse
    
    images = Image.open("resff.png").convert('RGB')
    image = Image.open("kodim03.png").convert('RGB')
    
    pixels = images.load()
    pix = image.load()
     
    ans = MSE(pixels,pix,3)
    
    print(ans)
    
    
    
    