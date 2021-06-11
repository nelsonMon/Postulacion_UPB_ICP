#### código de la postulacion UPB-ICP

##### paquetes utilizados para la GUI
import tkinter #### PAQUETE NECESARIO PARA CREAR LOS OBJETOS QUE SE COLOCARAN 
               #### DENTRO DE LA GUI 
import random  #### PAQUETE PARA GENERAR NUMEROS ALEATORIOS
#from wn32api import GetSystemMetrics ### PAQUETE PARA OBTENER EL 
from PIL import Image, ImageTk
####


# def seguro_image():
#     imge = PhotoImage(file = r"triangulo.png")
#     return imge

### configuro la ventana y en ancho para colocar todos los elementos propuestos.
window =tkinter.Tk()
window.geometry('900x900')

def COLOCAR_TRIANGULO():
    ### funcion para colocar un triangulo(cuadrado rojo) con las respectivas entradas y salidas
    ### como se observa en el documento de word    
    global cajas_datos ### se declara la variabla de cajas_datos como variable global. Esto con el fin de que sea de utilidad para mover 
    ### las cajas de datos  tanto de entrada como de saliad.
    # global coordenatex_caja_datos_I1
    # global coordenatey_caja_datos_I1
    
    # global coordenatex_caja_datos_I2
    # global coordenatey_caja_datos_I2
    
    # global coordenatex_caja_datos_O1
    # global coordenatey_caja_datos_O1
       
    ### con las lineas 4 lineas de código de abajo creo y posiciono un cuadrado rojo que representaria el triangulo con dos entradas, una salida.
    Labels.append(tkinter.Label(window,bg="red",width=10,height=5)) #configuración de la figura que se va a poner en una sección de la ventana
    coordenatex=int(random.gauss(450, 150)) ### coordenadas en x de la figura que se colocará en una sección de la ventana
    coordenatey=int(random.gauss(800, 15)) ### coordenadas en y de la figura que se colocará en una sección de la ventana
    Labels[-1].place(x=coordenatex, y=coordenatey) ##  la figura se posiciona en la ventana con las cordenadas especificadas.
    
    ### con las lineas 4 lineas de código de abajo creo y posiciono un cuadro de entrada de datos.
    cajas_datos.append(tkinter.Entry(window,width=10)) ## creo el objeto de tipo caja de datos (NO ES LABEL O ETIQUETA)
    coordenatex_caja_datos_I1=coordenatex+100 ## configuro la entrada de datos a la derecha de la figura(triangulo rojo) en cuanto a su cordenanda en x
    coordenatey_caja_datos_I1=coordenatey ## configuro la entrada de datos a la misma ubicación de y de la figura (triangulo rojo)
    cajas_datos[-1].place(x=coordenatex_caja_datos_I1, y=coordenatey_caja_datos_I1) ## posiciono la entrada de datos en la ventana
    
    ### con las lineas 4 lineas de código de abajo creo y posiciono un cuadro de entrada de datos.
    cajas_datos.append(tkinter.Entry(window,width=10)) ## creo el objeto de tipo caja de datos (NO ES LABEL O ETIQUETA)
    coordenatex_caja_datos_I2=coordenatex-80 ## configuro la entrada de datos a la izquierda de la figura(triangulo rojo) en cuanto a su cordenanda en x
    coordenatey_caja_datos_I2=coordenatey ## configuro la entrada de datos a la misma ubicación de y de la figura (triangulo rojo)
    cajas_datos[-1].place(x=coordenatex_caja_datos_I2, y=coordenatey_caja_datos_I2)  ## posiciono la entrada de datos en la ventana
    
    ### con las lineas 4 lineas de código de abajo creo y posiciono un cuadro de salida de datos.
    cajas_datos.append(tkinter.Entry(window,width=10)) ## creo el objeto de tipo caja de datos (NO ES LABEL O ETIQUETA)
    coordenatex_caja_datos_O1=coordenatex ## configuro la salida de datos a la misma ubicación de x de la figura (triangulo rojo)
    coordenatey_caja_datos_O1=coordenatey+100 ## configuro la entrada de datos más abajo de la figura(cuadro azul ) en cuanto a su cordenanda en y
    cajas_datos[-1].place(x=coordenatex_caja_datos_O1, y=coordenatey_caja_datos_O1) ## posiciono la salida de datos en la ventana
    
    ## este código me sirve para activar el drop y el drap de cada figura hecha y posicionada en la ventana.
    for i in range(0,len(Labels)):
        Labels[i].bind("<Button-1>",drag_start_triangulo)
        Labels[i].bind("<B1-Motion>",drag_motion_triangulo)
        
def COLOCAR_CUADRADO():
    
    ### con las lineas 4 lineas de código de abajo creo y posiciono un cuadrado azul que representaria el cuadrado con dos entradas y dos  salidas.
    Labels.append(tkinter.Label(window,bg="blue",width=10,height=5))
    coordenatex=int(random.gauss(450, 150))#configuración de la figura que se va a poner en una sección de la ventana
    coordenatey=int(random.gauss(800, 15))#configuración de la figura que se va a poner en una sección de la ventana
    Labels[-1].place(x=coordenatex, y=coordenatey) ##  la figura se posiciona en la ventana con las cordenadas especificadas.
    
    ### con las lineas 4 lineas de código de abajo creo y posiciono un cuadro de entrada de datos.
    cajas_datos.append(tkinter.Entry(window,width=10)) ## creo el objeto de tipo caja de datos (NO ES LABEL O ETIQUETA)
    coordenatex_caja_datos_I1=coordenatex+100 ## configuro la entrada de datos a la derecha de la figura(cuadro azul ) en cuanto a su cordenanda en x
    coordenatey_caja_datos_I1=coordenatey ## configuro la entrada de datos a la misma ubicación de y de la figura (triangulo rojo)
    cajas_datos[-1].place(x=coordenatex_caja_datos_I1, y=coordenatey_caja_datos_I1) ## posiciono la entrada de datos en la ventana
    
    ### con las lineas 4 lineas de código de abajo creo y posiciono un cuadro de entrada de datos.
    cajas_datos.append(tkinter.Entry(window,width=10))## creo el objeto de tipo caja de datos (NO ES LABEL O ETIQUETA)
    coordenatex_caja_datos_I2=coordenatex-80 ## configuro la entrada de datos a la izquierda de la figura(cuadro azul ) en cuanto a su cordenanda en x
    coordenatey_caja_datos_I2=coordenatey ## configuro la entrada de datos a la misma ubicación de y de la figura (triangulo rojo)
    cajas_datos[-1].place(x=coordenatex_caja_datos_I2, y=coordenatey_caja_datos_I2) ## posiciono la entrada de datos en la ventana
    
    ### con las lineas 4 lineas de código de abajo creo y posiciono un cuadro de salida de datos.
    cajas_datos.append(tkinter.Entry(window,width=10)) ## creo el objeto de tipo caja de datos (NO ES LABEL O ETIQUETA)
    coordenatex_caja_datos_O1=coordenatex+100 ## configuro la salida de datos a la derecha de la figura(cuadro azul ) en cuanto a su cordenanda en x
    coordenatey_caja_datos_O1=coordenatey+100 ## configuro la salida de datos más abajo de la figura(cuadro azul ) en cuanto a su cordenanda en y
    cajas_datos[-1].place(x=coordenatex_caja_datos_O1, y=coordenatey_caja_datos_O1) ## posiciono la entrada de datos en la ventana

    ### con las lineas 4 lineas de código de abajo creo y posiciono un cuadro de salida de datos.
    cajas_datos.append(tkinter.Entry(window,width=10)) ## creo el objeto de tipo caja de datos (NO ES LABEL O ETIQUETA)
    coordenatex_caja_datos_O2=coordenatex-80 ## configuro la salida de datos a la izquierda de la figura(cuadro azul ) en cuanto a su cordenanda en x
    coordenatey_caja_datos_O2=coordenatey+100 ## configuro la salida de datos más abajo de la figura(cuadro azul ) en cuanto a su cordenanda en y
    cajas_datos[-1].place(x=coordenatex_caja_datos_O2, y=coordenatey_caja_datos_O2) ## posiciono la entrada de datos en la ventana

    ## este código me sirve para activar el drop y el drap de cada figura hecha y posicionada en la ventana.
    for i in range(0,len(Labels)):
        Labels[i].bind("<Button-1>",drag_start_cuadrado)
        Labels[i].bind("<B1-Motion>",drag_motion_cuadrado)
    

def COLOCAR_CIRCULO():
    ### el código para colocar el cuadro verde que representa el circulo con su respectiva entrada y salida tienen la misma estructura o secuencia que las observadas previamente.
    ### primero se configura los parámetros de la figura y se posiciona, posteriormente se configura y se posiciona la entrada y salida.  
    Labels.append(tkinter.Label(window,bg="green",width=10,height=5))
    coordenatex=int(random.gauss(450, 150))
    coordenatey=int(random.gauss(800, 15))
    Labels[-1].place(x=coordenatex, y=coordenatey)
    
    cajas_datos.append(tkinter.Entry(window,width=10))
    coordenatex_caja_datos_I1=coordenatex+100
    coordenatey_caja_datos_I1=coordenatey
    cajas_datos[-1].place(x=coordenatex_caja_datos_I1, y=coordenatey_caja_datos_I1)
    
    cajas_datos.append(tkinter.Entry(window,width=10))
    coordenatex_caja_datos_O1=coordenatex+100
    coordenatey_caja_datos_O1=coordenatey+100
    cajas_datos[-1].place(x=coordenatex_caja_datos_O1, y=coordenatey_caja_datos_O1)
    
    for i in range(0,len(Labels)):
        Labels[i].bind("<Button-1>",drag_start_circulo)
        Labels[i].bind("<B1-Motion>",drag_motion_circulo)        
        
 
    #### con esta funcion se realiza los calculos con los datos escritos en el cuadro azul, mostrando las dos salidas correspondientes. NOTA: se debe colocar primero y unicamente esta figura 
def CALCULAR():
    datoI1=int(cajas_datos[-1].get())
    datoI2=int(cajas_datos[-2].get())
    cajas_datos[-3].insert(0,str(3*datoI1))
    cajas_datos[-4].insert(0,str(2*datoI2))
    #print(dato1,dato2)
    # dato_O1=
    # dato_O2=        
    
    ### con esta funcion se obtiene las coordenadas actuales de la figura del triangulo que posteriormente se podrá mover con el mouse y posicionar en otro lugar.
def drag_start_triangulo(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    # print(event.x)
    # print(event.x)
    
    ### con esta funcion se actualiza las coordenadas del triangulo y las cajas de datos tanto de entrada como de salida.
def drag_motion_triangulo(event):
    global cajas_datos
       
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
    cajas_datos[-1].place(x=x+100, y=y)

    cajas_datos[-1-1].place(x=x-80, y=y)
    
    # coordenatex_caja_datos_I2=x
    # coordenatey_caja_datos_I2=y
    
    cajas_datos[-1-2].place(x=x, y=y+100)
    # coordenatex_caja_datos_O1=x
    # coordenatey_caja_datos_O1=y
    
    # print(x,y)
    ### con esta funcion se obtiene las coordenadas actuales de la figura del cuadrado que posteriormente se podrá mover con el mouse y posicionar en otro lugar.
def drag_start_cuadrado(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    # print(event.x)
    # print(event.x)
### con esta funcion se actualiza las coordenadas del cuadrado y las cajas de datos tanto de entrada como de salida.   
def drag_motion_cuadrado(event):
    global cajas_datos
       
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
    cajas_datos[-1].place(x=x+100, y=y)

    cajas_datos[-1-1].place(x=x-80, y=y)
    
    # coordenatex_caja_datos_I2=x
    # coordenatey_caja_datos_I2=y
    
    cajas_datos[-1-2].place(x=x+100, y=y+100)
    cajas_datos[-1-3].place(x=x-80, y=y+100)
    # coordenatex_caja_datos_O1=x
    # coordenatey_caja_datos_O1=y
    # print(x,y)

### con esta funcion se obtiene las coordenadas actuales de la figura del cuadrado que posteriormente se podrá mover con el mouse y posicionar en otro lugar.
def drag_start_circulo(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    # print(event.x)
    # print(event.x)

### con esta funcion se obtiene las coordenadas actuales de la figura del circulo que posteriormente se podrá mover con el mouse y posicionar en otro lugar.
def drag_motion_circulo(event):
    global cajas_datos
       
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
    cajas_datos[-1].place(x=x+100, y=y)
    
    # coordenatex_caja_datos_I2=x
    # coordenatey_caja_datos_I2=y   
    cajas_datos[-1-1].place(x=x+100, y=y+100)
    # coordenatex_caja_datos_O1=x
    # coordenatey_caja_datos_O1=y
    # print(x,y)

#### variables de listas en donde se guardaran cada objeto creado
cajas_datos=[]
Labels=[]
botones=[]

#### Segmento que crea una etiqueta que separa la ventana en secciones, una para colocar las figuras y otra para colocar los botones que se usan para crear las figuras.
#### creación de una etiqueta de color azul muy claro en la pate superior
Labels_botones=tkinter.Label(window,bg="LightBlue3",width='2',height='2')
#Labels_botones.place(x=0, y=800)
Labels_botones.pack(fill='x')

#### creación de una etiqueta de color azul muy claro en la pate inferior
Labels_figuras=tkinter.Label(window,bg="LightBlue3",height='10')
#Labels_botones.place(x=0, y=800)
Labels_figuras.pack(fill='x',side='bottom')


### botones que me sirven para colocar cada figura dependiendo la demanda del usuario. Es decir, no existe un limite de figuras para agregar.
boton1 =tkinter.Button(window,text= 'triangulo', command = COLOCAR_TRIANGULO)
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

### Inicializó toda la ventana con sus respectivos botones y funcionalidades.
window.mainloop()

