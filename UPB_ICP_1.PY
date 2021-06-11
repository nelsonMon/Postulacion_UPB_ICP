#### codigo de la postulacion UPB-ICP

##### paquetes utilizados para la GUI
import tkinter #### PAQUETE NECESARIO PARA CREAR LOS OBJETOS QUE SE COLOCARAN 
               #### DENTRO DE LA GUI 
import random  #### PAQUETE PARA GENERAR NUMEROS ALEATORIOS
from win32api import GetSystemMetrics ### PAQUETE PARA OBTENER EL 
####



def COLOCAR_TRIANGULO():
    
    label.append(tkinter.Label(window,bg="red",width=10,height=5))
    coordenatex=int(random.gauss(450, 150))
    coordenatey=int(random.gauss(800, 15))
    label[-1].place(x=coordenatex, y=coordenatey)
    for i in range(0,len(label)):
        label[i].bind("<Button-1>",drag_start)
        label[i].bind("<B1-Motion>",drag_motion)

def COLOCAR_CUADRADO():
    
    label.append(tkinter.Label(window,bg="blue",width=10,height=5))
    coordenatex=int(random.gauss(450, 150))
    coordenatey=int(random.gauss(800, 15))
    label[-1].place(x=coordenatex, y=coordenatey)
    for i in range(0,len(label)):
        label[i].bind("<Button-1>",drag_start)
        label[i].bind("<B1-Motion>",drag_motion)
        

def COLOCAR_CIRCULO():
    
    label.append(tkinter.Label(window,bg="green",width=10,height=5))
    coordenatex=int(random.gauss(450, 150))
    coordenatey=int(random.gauss(800, 15))
    label[-1].place(x=coordenatex, y=coordenatey)
    for i in range(0,len(label)):
        label[i].bind("<Button-1>",drag_start)
        label[i].bind("<B1-Motion>",drag_motion)        
        
 
def CALCULAR():
    print('mmmm')
    
       
def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    # print(event.x)
    # print(event.x)
    
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
    print(x,y)

    

window =tkinter.Tk()
window.geometry('900x900')




label=[]

label_botones=tkinter.Label(window,bg="LightBlue3",width='2',height='2')
#label_botones.place(x=0, y=800)
label_botones.pack(fill='x')

label_figuras=tkinter.Label(window,bg="LightBlue3",height='10')
#label_botones.place(x=0, y=800)
label_figuras.pack(fill='x',side='bottom')



boton1 =tkinter.Button(window,text= 'triangulo',command=COLOCAR_TRIANGULO)
boton1.pack()
boton1.place(x=50,y=0)

boton2 =tkinter.Button(window,text= 'cuadrado',command=COLOCAR_CUADRADO)
boton2.pack()
boton2.place(x=250,y=0)

boton3 =tkinter.Button(window,text= 'circulo',command=COLOCAR_CIRCULO)
boton3.pack()
boton3.place(x=450,y=0)

boton4 =tkinter.Button(window,text= 'calcular',command=CALCULAR)
boton4.pack()
boton4.place(x=650,y=0)


window.mainloop()

