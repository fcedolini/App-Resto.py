import tkinter as tk
import random
import datetime
from tkinter import filedialog, messagebox

operadores = ''
operador = ''

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postre = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


# Func BOTONES
def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, 'end')
    visor_calculadora.insert('end', operador)


# Tecla borrar
def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, 'end')


# Tecla Resultado
def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, 'end')
    visor_calculadora.insert(0, resultado)
    operador = ''


# Calcular total
def total():
    subtotal_comida = 0
    i = 0
    for cantidad in texto_comida:
        subtotal_comida = subtotal_comida + \
            (float(cantidad.get()) * precios_comida[i])
        i += 1

    subtotal_bebida = 0
    i = 0
    for cantidad in texto_bebida:
        subtotal_bebida = subtotal_bebida + \
            (float(cantidad.get()) * precios_bebida[i])
        i += 1

    subtotal_postre = 0
    i = 0
    for cantidad in texto_postre:
        subtotal_postre = subtotal_postre + \
            (float(cantidad.get()) * precios_postre[i])
        i += 1

    sub_total = subtotal_comida + subtotal_bebida + subtotal_postre
    impuesto = sub_total * 0.21
    total = sub_total + impuesto

    var_costo_comida.set(f'$ {round(subtotal_comida, 2)}')
    var_costo_bebida.set(f'$ {round(subtotal_bebida, 2)}')
    var_costo_postre.set(f'$ {round(subtotal_postre, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuesto.set(f'$ {round(impuesto, 2)}')
    var_total.set(f'$ {round(total, 2)}')


# func recibo
def recibo():
    texto_recibo.delete(1.0, 'end')
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{
        fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert('end', f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert('end', '*' * 57 + '\n')
    texto_recibo.insert('end', 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert('end', '-' * 68 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(
                'end', f'{lista_comidas[x]}\t\t{comida.get()}\t$ {int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(
                'end', f'{lista_bebidas[x]}\t\t{bebida.get()}\t$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(
                'end', f'{lista_postres[x]}\t\t{postre.get()}\t$ {int(postre.get()) * precios_postre[x]}\n')
        x += 1

    texto_recibo.insert('end', '-' * 68 + '\n')
    texto_recibo.insert(
        'end', f'Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(
        'end', f'Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(
        'end', f'Costo de los Postres: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert('end', '-' * 68 + '\n')
    texto_recibo.insert(
        'end', f'Sub Total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(
        'end', f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(
        'end', f'Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert('end', '*' * 57 + '\n')


# Func GUARDAR
def guardar():
    info_recibo = texto_recibo.get(1.0, 'end')
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'Su Recibo ha sido guardado')


# RESETEAR
def reset():
    texto_recibo.delete(0.1, 'end')

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state='disabled')
    for cuadro in cuadros_bebida:
        cuadro.config(state='disabled')
    for cuadro in cuadros_postre:
        cuadro.config(state='disabled')

    for v in variables_comida:
        v.set('0')
    for v in variables_bebida:
        v.set('0')
    for v in variables_postre:
        v.set('0')

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


# Resivar Check Button
def revisar_chack():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state='normal')
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, 'end')
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state='disabled')
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state='normal')
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, 'end')
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state='disabled')
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state='normal')
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, 'end')
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state='disabled')
            texto_postre[x].set('0')
        x += 1


# iniciar TKinter en variable
aplicacion = tk.Tk()

# Tamaño ventana
aplicacion.geometry('1020x630+0+0')

# Evitar maximizar para no modificar diseño
aplicacion.resizable(0, 0)

# Titulo ventana
aplicacion.title('Mi Resto - Sistema de Facturación')

# Color de fondo ventana
aplicacion.config(bg='burlywood')


# Panel superior
panel_sup = tk.Frame(aplicacion, bd=1, relief='flat')
panel_sup.pack(side='top')


# Panel Iz
panel_iz = tk.Frame(aplicacion, bd=1, relief='flat')
panel_iz.pack(side='left')

# Panel costo (dentro de Panel Iz)
panel_costos = tk.Frame(panel_iz,  bd=1, relief='flat', bg='azure4')
panel_costos.pack(side='bottom')

# Panel Comidas (dentro de Panel Iz)
panel_comidas = tk.LabelFrame(panel_iz, text='Comida', font=(
    'Dosis', 15, 'bold'), fg='azure4', bd=1, relief='flat')
panel_comidas.pack(side='left')

# Panel Bebidas (dentro de Panel Iz)
panel_bebidas = tk.LabelFrame(panel_iz, text='Bebidas', font=(
    'Dosis', 15, 'bold'), fg='azure4', bd=1, relief='flat')
panel_bebidas.pack(side='left')

# Panel Postres (dentro de Panel Iz)
panel_postres = tk.LabelFrame(panel_iz, text='Postres', font=(
    'Dosis', 15, 'bold'), fg='azure4', bd=1, relief='flat')
panel_postres.pack(side='left')


# Panel Der
panel_der = tk.Frame(aplicacion, bd=1, relief='flat')
panel_der.pack(side='right')

# Panel Calc (Der)
panel_calc = tk.LabelFrame(panel_der, bg='burlywood', bd=1, relief='flat')
panel_calc.pack()

# Panel recibo (Der)
panel_recibo = tk.LabelFrame(panel_der, bg='burlywood', bd=1, relief='flat')
panel_recibo.pack()

# Panel botones (Der)
panel_botones = tk.LabelFrame(panel_der, bg='burlywood', bd=1, relief='flat')
panel_botones.pack()


# Etiqueta Título
etiqueta_titulo = tk.Label(panel_sup, text='Sistema de Facturación',
                           fg='azure4', font=('Dosis', 58), bg='burlywood', width=20)
etiqueta_titulo.grid(row=0, column=0)


# Lista de productos
lista_comidas = ['pollo', 'salmón', 'pizza',
                 'cordero', 'merluza', 'musa', 'papa', 'lomito']
lista_bebidas = ['agua', 'gaseosa', 'lima',
                 'limonada', 'jugo', 'te', 'soda', 'vino']
lista_postres = ['torta', 'tarta', 'helado',
                 'flan', 'budin', 'crama', 'frutas', 'dulce']


# Check button items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # Check button
    variables_comida.append('')
    variables_comida[contador] = tk.IntVar()
    comida = tk.Checkbutton(panel_comidas, text=comida.title(), font=(
        'Dosis', 15, 'bold'), onvalue=1, offvalue=0, variable=variables_comida[contador], command=revisar_chack)
    comida.grid(row=contador, column=0, sticky='W')
    # Crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = tk.StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = tk.Entry(panel_comidas, font=(
        'Dosis', 15, 'bold'), bd=1, width=6, state='disabled', textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1


# Check button items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    # Check button
    variables_bebida.append('')
    variables_bebida[contador] = tk.IntVar()
    bebida = tk.Checkbutton(panel_bebidas, text=bebida.title(), font=(
        'Dosis', 15, 'bold'), onvalue=1, offvalue=0, variable=variables_bebida[contador], command=revisar_chack)
    bebida.grid(row=contador, column=0, sticky='W')
    # Crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = tk.StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = tk.Entry(panel_bebidas, font=(
        'Dosis', 15, 'bold'), bd=1, width=6, state='disabled', textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)

    contador += 1


# Check button items postre
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    # Check button
    variables_postre.append('')
    variables_postre[contador] = tk.IntVar()
    postre = tk.Checkbutton(panel_postres, text=postre.title(), font=(
        'Dosis', 15, 'bold'), onvalue=1, offvalue=0, variable=variables_postre[contador], command=revisar_chack)
    postre.grid(row=contador, column=0, sticky='W')
    # Crear cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = tk.StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = tk.Entry(panel_postres, font=(
        'Dosis', 15, 'bold'), bd=1, width=6, state='disabled', textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=1)

    contador += 1


# Variables
var_costo_comida = tk.StringVar()
var_costo_bebida = tk.StringVar()
var_costo_postre = tk.StringVar()
var_subtotal = tk.StringVar()
var_impuesto = tk.StringVar()
var_total = tk.StringVar()

# Etiquetas de COSTOS y campos de entrada Comida
etiqueta_costo_comida = tk.Label(panel_costos, text='Costo Comida', font=(
    'Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = tk.Entry(panel_costos, bd=1, width=10, state='readonly', font=(
    'Dosis', 12, 'bold'), textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)


# Etiquetas de COSTOS y campos de entrada BEBIDA
etiqueta_costo_bebida = tk.Label(panel_costos, text='Costo Bebida', font=(
    'Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = tk.Entry(panel_costos, bd=1, width=10, state='readonly', font=(
    'Dosis', 12, 'bold'), textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)


# Etiquetas de COSTOS y campos de entrada POSTRE
etiqueta_costo_postre = tk.Label(panel_costos, text='Costo Postre', font=(
    'Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = tk.Entry(panel_costos, bd=1, width=10, state='readonly', font=(
    'Dosis', 12, 'bold'), textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)


# Etiquetas de COSTOS y campos de entrada SUBTOTAL
etiqueta_subtotal = tk.Label(panel_costos, text='Sub Total', font=(
    'Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = tk.Entry(panel_costos, bd=1, width=10, state='readonly', font=(
    'Dosis', 12, 'bold'), textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# Etiquetas de COSTOS y campos de entrada IMPUESTO
etiqueta_impuesto = tk.Label(panel_costos, text='Impuesto', font=(
    'Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = tk.Entry(panel_costos, bd=1, width=10, state='readonly', font=(
    'Dosis', 12, 'bold'), textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

# Etiquetas de COSTOS y campos de entrada TOTAL
etiqueta_total = tk.Label(panel_costos, text='Total', font=(
    'Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = tk.Entry(panel_costos, bd=1, width=10, state='readonly', font=(
    'Dosis', 12, 'bold'), textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)


# Botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = tk.Button(panel_botones, text=boton.title(), font=(
        'Dosis', 14, 'bold'), fg='white', bg='azure4', bd=1, width=9)
    botones_creados.append(boton)
    boton.grid(row=0, column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=reset)


# Área de Recibo
texto_recibo = tk.Text(panel_recibo, font=(
    'Dosis', 12, 'bold'), bd=1, width=51, height=10)
texto_recibo.grid(row=0, column=0)


# CALCULADORA
visor_calculadora = tk.Entry(panel_calc, font=(
    'Dosis', 16, 'bold'), width=32, bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5',
                       '6', '-', '1', '2', '3', 'x', 'Res', 'C', '0', '/']
botones_guardados = []

# Loop crear botones
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = tk.Button(panel_calc, text=boton.title(), font=(
        'Dosis', 16, 'bold'), fg='white', bg='azure4', bd=1, width=8)
    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna)
    if columna == 3:
        fila += 1
    columna += 1
    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))


# Evitar q pantalle se cierre
aplicacion.mainloop()
