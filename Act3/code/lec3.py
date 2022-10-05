import re
from tkinter import *
from tkinter import messagebox as Msg
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

"""
En esta aplicación vamos a realizar la predicción de la especie de Iris, a través 
de los datos introducidos por nuestra aplicación TKinter.

"""

"""Definimos apariencia de nuestra aplicación."""
raiz = Tk()

raiz.title("Iris dataset with Tkinter")
raiz.iconphoto(False, PhotoImage(file='icono.png'))
raiz.config(bg="#BCB60A")
raiz.geometry('800x500')
raiz.resizable(0,0)

miframe=Frame(raiz)
miframe.config(bg="#BCB60A")
img = PhotoImage(file="iris.png")
label = Label(miframe, image=img, width=500, height=281)
label.grid(row=1, column=3, rowspan=2, padx=15, pady=15, sticky="s")
miframe.pack()

sl=StringVar()
sw=StringVar()
pl=StringVar()
pw=StringVar()

#ENTRY:
cuadro_texo_sepal_length=Entry(miframe, textvariable=sl)
cuadro_texo_sepal_length.grid(row=0, column=1, padx=15, pady=15)
cuadro_texo_sepal_length.config(fg="green")

cuadro_texo_sepal_width=Entry(miframe, textvariable=sw)
cuadro_texo_sepal_width.grid(row=1, column=1, padx=15, pady=15)
cuadro_texo_sepal_width.config(fg="green")

cuadro_texo_petal_length=Entry(miframe, textvariable=pl)
cuadro_texo_petal_length.grid(row=2, column=1, padx=15, pady=15)
cuadro_texo_petal_length.config(fg="green")

cuadro_texo_petal_width=Entry(miframe, textvariable=pw)
cuadro_texo_petal_width.grid(row=3, column=1, padx=15, pady=15)
cuadro_texo_petal_width.config(fg="green")


#LABEL:
nombre_Label_sepal_length=Label(miframe, text="Sepal length: ", bg="#BCB60A", fg="#AC0BAC")
nombre_Label_sepal_length.grid(row=0, column=0, sticky="e")

nombre_Label_sepal_width=Label(miframe, text="Sepal width: ", bg="#BCB60A", fg="#AC0BAC")
nombre_Label_sepal_width.grid(row=1, column=0, sticky="e")

nombre_Label_petal_length=Label(miframe, text="Petal lenght: ", bg="#BCB60A", fg="#AC0BAC")
nombre_Label_petal_length.grid(row=2, column=0, sticky="e")

nombre_Label_petal_width=Label(miframe, text="Petal width: ", bg="#BCB60A", fg="#AC0BAC")
nombre_Label_petal_width.grid(row=3, column=0, sticky="e")

"""
Definimos ahora nuestras funciones para el funcionamiento de la aplicación.
FUNCIONES:
"""

def prediccion(s_length, s_width, p_length, p_width):
    """
    Esta función llamada prediccion nos realiza el calculo con respecto a los datos que ya tenemos 
    y los datos introducidos por el usuario.
    La función recibre los datos:
    - sepal length
    - sepal width
    - petal length
    - petal width
    con los cuales nos devolverá la specie de iris al que corresponde según nuestros cálculos. 

    """
    df=pd.read_csv("iris.csv")
    X= df.drop(["species"], axis=1)
    y=df["species"]
    X = X.values
    y = y.values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.80, random_state=0)
    clf =DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    Xnew_a= []
    Xnew_a.append(round(s_length, 1))
    Xnew_a.append(round(s_width, 1))
    Xnew_a.append(round(p_length, 1))
    Xnew_a.append(round(p_width, 1))
    Xnew=[]
    Xnew.append(Xnew_a)
    y_new=clf.predict(Xnew)
    return (y_new[0])
"""Retorno solo el valor """

"""Para reestablecer los campos a vacíos"""
def setTextInput(text):
    """
    Esta función nos pone la aplicación sin datos para una nueva comprobación por parte del usuiario.
    """
    sl.set(text)
    sw.set(text)
    pl.set(text)
    pw.set(text)

"""Reviso si el dato introducido es un número con coma y lo cambio por punto"""
def procesando_datos(text):
    """
    Esta función nos cambia la coma de los números introducidos por el usuario para hacerlos válidos 
    con el punto (float)
    """
    text=re.sub(',', '.', text)
    return text

"""Validar y dar resultado"""
def validar_datos():
    """
    En esta función validamos datos y realizamos la distintas comprobaciones 
    de los datos introducidos por el usuario, además de mostrar el resultado.
    """
    try:
        """Transformo texto en float """
        sl=float(procesando_datos(cuadro_texo_sepal_length.get()))
        sw=float(procesando_datos(cuadro_texo_sepal_width.get()))
        pl=float(procesando_datos(cuadro_texo_petal_length.get()))
        pw=float(procesando_datos(cuadro_texo_petal_width.get()))
        resolucion = prediccion(sl, sw, pl, pw)
        """Muestro resultado a través de un messagebox"""
        message= "With the data provided, the IRIS species is:\n ***" + resolucion + "***"
        Msg.showinfo("Result", message)
        setTextInput("")
        
    except Exception:
        message= "The data entered is not valid."
        Msg.showinfo("ERROR", message)
        setTextInput("")

"""Definimos el botón que nos validará datos en la aplicación."""

boton_enviar=Button(raiz, text="Give Species", command=validar_datos, bg="#64E5FF", fg="#AC0BAC")
boton_enviar.pack()

raiz.mainloop()