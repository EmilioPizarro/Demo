from tkinter import *
#Modulo de mensajes de alerta
from tkinter import messagebox as mb


#Activo la caja, cargo el valor, y la descativo
def CargarValorRetro(resultado):
    totalRetro.config(state=NORMAL)
    totalRetro.insert(0,str(resultado))
    totalRetro.config(state=DISABLED)

def CargarValorMayo(resultado):
    totalMayo.config(state=NORMAL)
    totalMayo.insert(0,str(resultado))
    totalMayo.config(state=DISABLED)

def CargarValorSueldo(resultado):
    totalSueldo.config(state=NORMAL)
    totalSueldo.insert(0,str(resultado))
    totalSueldo.config(state=DISABLED)




def borrar_resultado_anterior():
    totalRetro.config(state=NORMAL)
    totalRetro.delete(0, 'end')
    totalRetro.config(state=DISABLED)    
    
    totalMayo.config(state=NORMAL)
    totalMayo.delete(0, 'end')
    totalMayo.config(state=DISABLED)   
    
    totalSueldo.config(state=NORMAL)
    totalSueldo.delete(0, 'end')
    totalSueldo.config(state=DISABLED)   
    

#Devuelvo true o false si algun campo de carga esta vacio.
def verificarInputVacio():
    
    return febrero.get()=='' or marzo.get() == '' or abril.get() == ''  or mayo.get() == '' or valorDia.get() == '' or aumento.get() == ''

def totRetro():
    #Si se encuentra vacio un campo de carga, aviso para que se carguen ambos
    if verificarInputVacio():
            mb.showwarning(title='!Atencion¡',message='Complete Todos los campos')
    else:
        #Con la excepcion controlo que no se manden strings
        try:
            #defino el resultado como uha operacion entre los entry
            resultadoRetro = ((float(valorDia.get()) * float(aumento.get()))/100)*((float(febrero.get()) + float(marzo.get()) + float(abril.get())))
            borrar_resultado_anterior()
            #muestro el valor
            CargarValorRetro(resultadoRetro)
            

            #Sueldo Mayo            
            resultadoMayo = ((float(valorDia.get()) * float(aumento.get()))/100)+(
                
                float(valorDia.get()) * float(mayo.get())
                )
            #muestro el valor
            CargarValorMayo(resultadoMayo)
            
            
            #Sueldo final
            resultadoSueldo = (float(totalMayo.get())+float(totalRetro.get()))
            #muestro el valor
            CargarValorSueldo(resultadoSueldo)
            
            

        except ValueError:
            mb.showwarning(title='!Atencion¡',message='Ingrese solo Numeros')
            febrero.delete(0,'end')
            marzo.delete(0,'end')
            borrar_resultado_anterior()  

            

        
#Las variables de control no tienen Delete
        
def limpiar():
    febrero.delete(0,'end')
    marzo.delete(0,'end')
    abril.delete(0,'end')
    mayo.delete(0,'end')
    valorDia.delete(0,'end')
    aumento.delete(0,'end')
    totalRetro.delete(0,'end')
    totalMayo.delete(0,'end')
    borrar_resultado_anterior()
    






#ventana
root = Tk()


#Titulo de la ventana
root.title("Demo")

#Definir la dimension de la ventana
root.geometry("600x600")

#Frame dentro de la raiz
cuadro = Frame(root,width=500,height=400)
#Fijar el frame dentro del root
cuadro.pack()



#-------------- 1 ---------------
febrero = Entry(cuadro)
#Uso grid como grilla para ordenar las columnas y las entradas
#la columna uno es para los inputs y la 0 para las etiquetas
#padx e y son paddings, relleno entre contenido
febrero.grid(row=0,column=1,padx=10,pady=10)



etiqueta1 = Label(cuadro,text="Dias trabajados en Febrero: ",font=20)
etiqueta1.grid(row=0,column=0,padx=10,pady=10)


#-------------- 1 ---------------



#-------------- 2 ---------------
marzo=Entry(cuadro)
marzo.grid(row=1,column=1,padx=10,pady=10)

etiqueta2 = Label(cuadro,text="Dias trabajados en Marzo: ",font=20)
etiqueta2.grid(row=1,column=0,padx=10,pady=10)

#-------------- 2 ---------------

#-------------- 3 ---------------
abril=Entry(cuadro)
abril.grid(row=2,column=1,padx=10,pady=10)


etiqueta3 = Label(cuadro,text="Dias trabajados en Abril: ",font=20)
etiqueta3.grid(row=2,column=0,padx=10,pady=10)

#-------------- 3 ---------------

#-------------- 4 ---------------
mayo=Entry(cuadro)
mayo.grid(row=3,column=1,padx=10,pady=10)

etiqueta4 = Label(cuadro,text="Dias trabajados en Mayo: ",font=20)
etiqueta4.grid(row=3,column=0,padx=10,pady=10)

#-------------- 4 ---------------

#-------------- 5 ---------------
valorDia=Entry(cuadro)
valorDia.grid(row=4,column=1,padx=10,pady=10)

etiquetaDia = Label(cuadro,text="Valor del dia en $: ",font=20)
etiquetaDia.grid(row=4,column=0,padx=10,pady=10)

#-------------- 5 ---------------

#-------------- 6 ---------------
aumento=Entry(cuadro)
aumento.grid(row=5,column=1,padx=10,pady=10)

etiquetaAumento = Label(cuadro,text="Porcentaje de aumento: ",font=20)
etiquetaAumento.grid(row=5,column=0,padx=10,pady=10)

#-------------- 6 ---------------



#------ Salidas ------

totalRetro=Entry(cuadro)
totalRetro.grid(row=6,column=1,padx=10,pady=10)
#Desactivo esta caja para que no se puedan cargar valores, solo los calculados
totalRetro.config(state=DISABLED)

totalRetrolbl = Label(cuadro,text="Total Retroactivos en $: ",font=20)
totalRetrolbl.grid(row=6,column=0,padx=10,pady=10)


totalMayo=Entry(cuadro)
totalMayo.grid(row=7,column=1,padx=10,pady=10)
totalMayo.config(state=DISABLED)

totalMayolbl = Label(cuadro,text="Total Mayo en $: ",font=20)
totalMayolbl.grid(row=7,column=0,padx=10,pady=10)


totalSueldo=Entry(cuadro)
totalSueldo.grid(row=8,column=1,padx=10,pady=10)
totalSueldo.config(state=DISABLED)

totalSueldolbl = Label(cuadro,text="Total Sueldo en $: ",font=20)
totalSueldolbl.grid(row=8,column=0,padx=10,pady=10)



# ------------- Botones ---------------
#Botones
btnTotalRetro = Button(cuadro,text='Calcular Total Retro y Mayo')
#Empaquetar dentro del cuadro
btnTotalRetro.grid(row=9,column=0,padx=3,pady=3)
#Le defino la configuracion al boton, con la funcion de comportamiento en command
btnTotalRetro.config(font='Curier,10',command=totRetro)


#btnTotalMayo = Button(cuadro,text='Calcular Total Mayo')
#btnTotalMayo.grid(row=9,column=1,padx=3,pady=3)
#btnTotalMayo.config(font='Curier,10',command=totMayo)

btnLimpiarCampos = Button(cuadro,text='Limpiar')
btnLimpiarCampos.grid(row=9,column=1,padx=3,pady=3)
btnLimpiarCampos.config(font='Curier,10',command=limpiar)







#Cerrar el loop de la ventana
root.mainloop()