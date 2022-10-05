import pandas as pd
import matplotlib.pyplot as plt

# LIMPIAMOS el dataframe

try:
    df= pd.read_csv('finanzas2020[1].csv', sep='[;  ,:\s*\t\r]', engine='python')
    print("\n*****Fichero encontrado.*****\n")

    # Comprobación de columnas
    n_column=df.columns
    if len(n_column)!=12:
        raise NameError("El número de columnas no es el correcto.")
    
    # Comprobación de contenido en columnas y tratamiento
    df.fillna(0,inplace=True)

    # Comprobación de datos y tratamiento de errores.
    errors_count=0
    for i in df.columns:
        if type(i) != int:
            df.replace('[A-Za-z]', 0, regex=True, inplace=True)
            df.replace('\'', '', regex=True, inplace=True)
            df= df.astype(int)
            errors_count+=1  
    print("----------------")
    print(f"El número total de conversiones realizadas, {errors_count}, se han realizado con éxito.")    
    print("----------------")

    print("\n*****Fichero abierto una vez tratado.*****\n")
    print(df)
    print("----------------")


    # Suma de todas las columnas
    total_addition= df.sum()
    print("Totales mensuales:\n")
    print(total_addition)
    total_dict=total_addition.to_dict()
    print("----------------")


    # MES QUE MÁS SE HA GASTADO

    expenditure_month= min(total_dict, key=total_dict.get)
    print(f"El mes de más gasto ha sido {expenditure_month}.")
    print("----------------")

    # MES QUE MÁS SE HA AHORRADO

    savings_month= max(total_dict, key = total_dict.get)
    print(f"El mes de más ahorro ha sido {savings_month}.")
    print("----------------")

    # MEDIA DE GASTO DEL AÑO

    counter=0
    for value in total_dict.values():
        counter+=value
    print(f"La media de gastos anual ha sido {counter/len(total_dict):0.2f}€. ")
    print("----------------")

    # GASTOS e INGRESOS TOTALES DEL AÑO

    expenditures=0
    deposits=0
    for value in total_dict.values():
        if value < 0:    
            expenditures+=value
        else:
            deposits+=value
        
    print(f"Los gastos anuales tienen un total de {expenditures}€. ")
    print("----------------")
    print(f"Los ingresos anuales tienen un total de {deposits}€. ")
    print("----------------")

    # GRAFICA EVOLUTIVA DE INGRESOS ANUALES

    my_List=total_dict.items()
    x, y = zip(*my_List)
    plt.plot(x, y)
    plt.xlabel('Mes')
    plt.ylabel('Euros')
    plt.title('Finanzas Anuales')
    plt.show()

except FileNotFoundError:
    print ("\n*****Fichero N0 encontrado.*****\n")
    

