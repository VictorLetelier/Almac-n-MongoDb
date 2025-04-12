import pymongo
from pymongo import MongoClient
from tkinter import Tk, Frame, ttk, messagebox, IntVar, Toplevel

def conectar(coleccion):
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client['almacen']
    collection = db[coleccion]
    return collection

def borrar_documento():
    nombre_buscar = input("Ingrese el nombre del documento a borrar: ")

    collection = conectar()
    resultado = collection.delete_one({'nombre': nombre_buscar})

    if resultado.deleted_count == 1:
        print("Documento borrado exitosamente")
    else:
        print("No se encontró el documento especificado")


def modificar_documento():
    nombre_buscar = input("Ingrese el nombre del documento a modificar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")

    collection = conectar()
    resultado = collection.update_many({'nombre': nombre_buscar}, {'$set': {'nombre': nuevo_nombre}})
    print("Número de documentos modificados:", resultado.modified_count)

colecciones = ['empleado', 'producto', 'factura', 'envio']
root = Tk()
root.geometry("990x500")
root.wm_title('Almacen')
root.minsize(width=950, height=325)
frame = Frame(root)
frame.grid(column=0, row=0, sticky='nsew')
label = ttk.Label(frame, text='Seleccione una acción a realizar:')
label.grid(column=1, row=0, columnspan=4, padx=5, pady=5)
colecl = ttk.Label(frame, text='Colección')
colecl.grid(column=0, row=0, padx=5, pady=5)
colecb = ttk.Combobox(frame, values=colecciones)
colecb.set(colecciones[0])
colecb.grid(column=0, row=1, padx=5, pady=5)
def Mostrar():
    ventana = Toplevel(root)
    ventana.geometry("990x500")
    if colecb.get() == 'empleado':
        empleadol = ttk.Label(ventana, text='Ingrese los datos necesarios para su consulta (no es necesario ingresar todos):')
        empleadol.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        rutl = ttk.Label(ventana, text='Rut:')
        rutl.grid(column=0, row=1, padx=5, pady=5)
        rutt = ttk.Entry(ventana)
        rutt.grid(column=1, row=1, padx=5, pady=5)
        nombrel = ttk.Label(ventana, text='Nombre:')
        nombrel.grid(column=0, row=2, padx=5, pady=5)
        nombret = ttk.Entry(ventana)
        nombret.grid(column=1, row=2, padx=5, pady=5)
        apellidol = ttk.Label(ventana, text='Apellido:')
        apellidol.grid(column=0, row=3, padx=5, pady=5)
        apellidot = ttk.Entry(ventana)
        apellidot.grid(column=1, row=3, padx=5, pady=5)
        edadl = ttk.Label(ventana, text='Edad:')
        edadl.grid(column=0, row=4, padx=5, pady=5)
        edadt = ttk.Entry(ventana)
        edadt.grid(column=1, row=4, padx=5, pady=5)
        salariol = ttk.Label(ventana, text='Salario:')
        salariol.grid(column=0, row=5, padx=5, pady=5)
        salariot = ttk.Entry(ventana)
        salariot.grid(column=1, row=5, padx=5, pady=5)
        teléfonol = ttk.Label(ventana, text='Teléfono:')
        teléfonol.grid(column=0, row=6, padx=5, pady=5)
        teléfonot = ttk.Entry(ventana)
        teléfonot.grid(column=1, row=6, padx=5, pady=5)
        fechal = ttk.Label(ventana, text='Fecha Ingreso:')
        fechal.grid(column=0, row=7, padx=5, pady=5)
        fechat = ttk.Entry(ventana)
        fechat.grid(column=1, row=7, padx=5, pady=5)
        filtrol = ttk.Label(ventana, text='Seleccione los datos que quiere recuperar:')
        filtrol.grid(column=2, row=0, padx=5, pady=5)
        var1 = IntVar()
        idc = ttk.Checkbutton(ventana, text='Id', variable=var1)
        idc.grid(column=2, row=1, padx=5, pady=5)
        var2 = IntVar()
        rutc = ttk.Checkbutton(ventana, text='Rut', variable=var2)
        rutc.grid(column=2, row=2, padx=5, pady=5)
        var3 = IntVar()
        nombrec = ttk.Checkbutton(ventana, text='Nombre', variable=var3)
        nombrec.grid(column=2, row=3, padx=5, pady=5)
        var4 = IntVar()
        apellidoc = ttk.Checkbutton(ventana, text='Apellido', variable=var4)
        apellidoc.grid(column=2, row=4, padx=5, pady=5)
        var5 = IntVar()
        edadc = ttk.Checkbutton(ventana, text='Edad', variable=var5)
        edadc.grid(column=2, row=5, padx=5, pady=5)
        var6 = IntVar()
        salarioc = ttk.Checkbutton(ventana, text='Salario', variable=var6)
        salarioc.grid(column=2, row=6, padx=5, pady=5)
        var7 = IntVar()
        teléfonoc = ttk.Checkbutton(ventana, text='Teléfono', variable=var7)
        teléfonoc.grid(column=2, row=7, padx=5, pady=5)
        var8 = IntVar()
        fechac = ttk.Checkbutton(ventana, text='Fecha', variable=var8)
        fechac.grid(column=2, row=8, padx=5, pady=5)
        def MostrarEmpleados():
            filtro = {}
            filtro2 = {}
            if rutt.get() != '':
                filtro.update({'rut': rutt.get()})
            if nombret.get() != '':
                filtro.update({'nombre': nombret.get()})
            if apellidot.get() != '':
                filtro.update({'apellido': apellidot.get()})
            if edadt.get() != '':
                filtro.update({'edad': int(edadt.get())})
            if salariot.get() != '':
                filtro.update({'salario': int(salariot.get())})
            if teléfonot.get() != '':
                filtro.update({'teléfono': int(teléfonot.get())})
            if fechat.get() != '':
                filtro.update({'fecha': fechat.get()})
            if var1.get() == 0:
                filtro2.update({'_id':0})
            if var2.get() == 1:
                filtro2.update({'rut':1})
            if var3.get() == 1:
                filtro2.update({'nombre':1})
            if var4.get() == 1:
                filtro2.update({'apellido':1})
            if var5.get() == 1:
                filtro2.update({'edad':1})
            if var6.get() == 1:
                filtro2.update({'salario':1})
            if var7.get() == 1:
                filtro2.update({'teléfono':1})
            if var8.get() == 1:
                filtro2.update({'fecha':1})
            collection = conectar('empleado')
            resultados = collection.find(filtro, filtro2)
            objetos = []
            for resultado in resultados:
                objetos.append(resultado)
            messagebox.showinfo('Datos Recuperados:', objetos)
        def MostrarTodoEm():
            collection = conectar('empleado')
            resultados = collection.find({})
            objetos = []
            for resultado in resultados:
                objetos.append(resultado)
            messagebox.showinfo('Datos Recuperados:', objetos)
        boton = ttk.Button(ventana, text='Mostrar', command=MostrarEmpleados)
        boton.grid(column=1, row=8, padx=5, pady=5)
        boton2 = ttk.Button(ventana, text='Mostrar Todos los Datos', command=MostrarTodoEm)
        boton2.grid(column=1, row=9, columnspan=2, padx=5, pady=5)
    
    if colecb.get() == 'producto':
        productol = ttk.Label(ventana, text='Ingrese los datos necesarios para su consulta (no es necesario ingresar todos):')
        productol.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        nombrel = ttk.Label(ventana, text='Nombre:')
        nombrel.grid(column=0, row=1, padx=5, pady=5)
        nombret = ttk.Entry(ventana)
        nombret.grid(column=1, row=1, padx=5, pady=5)
        marcal = ttk.Label(ventana, text='Marca:')
        marcal.grid(column=0, row=2, padx=5, pady=5)
        marcat = ttk.Entry(ventana)
        marcat.grid(column=1, row=2, padx=5, pady=5)
        stockl = ttk.Label(ventana, text='Stock:')
        stockl.grid(column=0, row=3, padx=5, pady=5)
        stockt = ttk.Entry(ventana)
        stockt.grid(column=1, row=3, padx=5, pady=5)
        preciol = ttk.Label(ventana, text='Precio:')
        preciol.grid(column=0, row=4, padx=5, pady=5)
        preciot = ttk.Entry(ventana)
        preciot.grid(column=1, row=4, padx=5, pady=5)
        filtrol = ttk.Label(ventana, text='Seleccione los datos que quiere recuperar:')
        filtrol.grid(column=2, row=0, padx=5, pady=5)
        var1 = IntVar()
        idc = ttk.Checkbutton(ventana, text='Id', variable=var1)
        idc.grid(column=2, row=1, padx=5, pady=5)
        var2 = IntVar()
        nombrec = ttk.Checkbutton(ventana, text='Nombre', variable=var2)
        nombrec.grid(column=2, row=2, padx=5, pady=5)
        var3 = IntVar()
        marcac = ttk.Checkbutton(ventana, text='Marca', variable=var3)
        marcac.grid(column=2, row=3, padx=5, pady=5)
        var4 = IntVar()
        stockc = ttk.Checkbutton(ventana, text='Stock', variable=var4)
        stockc.grid(column=2, row=4, padx=5, pady=5)
        var5 = IntVar()
        precioc = ttk.Checkbutton(ventana, text='Precio', variable=var5)
        precioc.grid(column=2, row=5, padx=5, pady=5)
        def MostrarProductos():
            filtro = {}
            filtro2 = {}
            if nombret.get() != '':
                filtro.update({'nombre': nombret.get()})
            if marcat.get() != '':
                filtro.update({'marca': marcat.get()})
            if stockt.get() != '':
                filtro.update({'stock': int(stockt.get())})
            if preciot.get() != '':
                filtro.update({'precio': int(preciot.get())})
            if var1.get() == 0:
                filtro2.update({'_id':0})
            if var2.get() == 1:
                filtro2.update({'nombre':1})
            if var3.get() == 1:
                filtro2.update({'marca':1})
            if var4.get() == 1:
                filtro2.update({'stock':1})
            if var5.get() == 1:
                filtro2.update({'precio':1})
            collection = conectar('producto')
            resultados = collection.find(filtro, filtro2)
            objetos = []
            for resultado in resultados:
                objetos.append(resultado)
            messagebox.showinfo('Datos Recuperados:', objetos)
        def MostrarTodoPr():
            collection = conectar('producto')
            resultados = collection.find({})
            objetos = []
            for resultado in resultados:
                objetos.append(resultado)
            messagebox.showinfo('Datos Recuperados:', objetos)
        boton = ttk.Button(ventana, text='Mostrar', command=MostrarProductos)
        boton.grid(column=1, row=8, padx=5, pady=5)
        boton2 = ttk.Button(ventana, text='Mostrar Todos los Datos', command=MostrarTodoPr)
        boton2.grid(column=1, row=9, columnspan=2, padx=5, pady=5)

    if colecb.get() == 'factura':
        factural = ttk.Label(ventana, text='Ingrese los datos necesarios para su consulta (no es necesario ingresar todos):')
        factural.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        preciotl = ttk.Label(ventana, text='Precio Total:')
        preciotl.grid(column=0, row=1, padx=5, pady=5)
        preciott = ttk.Entry(ventana)
        preciott.grid(column=1, row=1, padx=5, pady=5)
        fechal = ttk.Label(ventana, text='Fecha Factura:')
        fechal.grid(column=0, row=2, padx=5, pady=5)
        fechat = ttk.Entry(ventana)
        fechat.grid(column=1, row=2, padx=5, pady=5)
        empleadol = ttk.Label(ventana, text='Empleado:')
        empleadol.grid(column=0, row=3, padx=5, pady=5)
        empleadot = ttk.Entry(ventana)
        empleadot.grid(column=1, row=3, padx=5, pady=5)
        detallel = ttk.Label(ventana, text='Detalles:')
        detallel.grid(column=1, row=4, padx=5, pady=5)
        nombreprodl = ttk.Label(ventana, text='Producto:')
        nombreprodl.grid(column=0, row=5, padx=5, pady=5)
        nombreprodt = ttk.Entry(ventana)
        nombreprodt.grid(column=1, row=5, padx=5, pady=5)
        cantidadl = ttk.Label(ventana, text='Cantidad:')
        cantidadl.grid(column=0, row=6, padx=5, pady=5)
        cantidadt = ttk.Entry(ventana)
        cantidadt.grid(column=1, row=6, padx=5, pady=5)
        preciol = ttk.Label(ventana, text='Precio:')
        preciol.grid(column=0, row=7, padx=5, pady=5)
        preciot = ttk.Entry(ventana)
        preciot.grid(column=1, row=7, padx=5, pady=5)
        filtrol = ttk.Label(ventana, text='Seleccione los datos que quiere recuperar:')
        filtrol.grid(column=2, row=0, padx=5, pady=5)
        var1 = IntVar()
        idc = ttk.Checkbutton(ventana, text='Id', variable=var1)
        idc.grid(column=2, row=1, padx=5, pady=5)
        var2 = IntVar()
        preciotc = ttk.Checkbutton(ventana, text='Precio Total', variable=var2)
        preciotc.grid(column=2, row=2, padx=5, pady=5)
        var3 = IntVar()
        fechac = ttk.Checkbutton(ventana, text='Fecha Factura', variable=var3)
        fechac.grid(column=2, row=3, padx=5, pady=5)
        var4 = IntVar()
        empleadoc = ttk.Checkbutton(ventana, text='Empleado', variable=var4)
        empleadoc.grid(column=2, row=4, padx=5, pady=5)
        var5 = IntVar()
        detallec = ttk.Checkbutton(ventana, text='Detalle', variable=var5)
        detallec.grid(column=2, row=5, padx=5, pady=5)
        var6 = IntVar()
        productoc = ttk.Checkbutton(ventana, text='Producto', variable=var6)
        productoc.grid(column=2, row=6, padx=5, pady=5)
        var7 = IntVar()
        cantidadc = ttk.Checkbutton(ventana, text='Cantidad', variable=var7)
        cantidadc.grid(column=2, row=7, padx=5, pady=5)
        var8 = IntVar()
        precioc = ttk.Checkbutton(ventana, text='Precio', variable=var8)
        precioc.grid(column=2, row=8, padx=5, pady=5)
        def MostrarFacturas():
            filtro = {}
            filtro2 = {}
            if preciott.get() != '':
                filtro.update({'Precio Total': preciot.get()})
            if fechat.get() != '':
                filtro.update({'Fecha Factura': fechat.get()})
            if empleadot.get() != '':
                filtro.update({'Nombre Empleado': empleadot.get()})
            if nombreprodt.get() != '':
                filtro.update({'Detalle.Nombre Producto': nombreprodt.get()})
            if cantidadt.get() != '':
                filtro.update({'Detalle.Cantidad': int(cantidadt.get())})
            if preciot.get() != '':
                filtro.update({'Detalle.Precio': int(preciot.get())})
            if var1.get() == 0:
                filtro2.update({'_id':0})
            if var2.get() == 1:
                filtro2.update({'Precio Total':1})
            if var3.get() == 1:
                filtro2.update({'Fecha Factura':1})
            if var4.get() == 1:
                filtro2.update({'Nombre Empleado':1})
            if var5.get() == 1:
                    filtro2.update({'Detalle':1})
            if var5.get() == 0:
                if var6.get() == 1:
                    filtro2.update({'Detalle.Nombre Producto':1})
                if var7.get() == 1:
                    filtro2.update({'Detalle.Cantidad':1})
                if var8.get() == 1:
                    filtro2.update({'Detalle.Precio':1})
            collection = conectar('factura')
            resultados = collection.find(filtro, filtro2)
            objetos = []
            for resultado in resultados:
                objetos.append(resultado)
            messagebox.showinfo('Datos Recuperados:', objetos)
        def MostrarTodoFc():
            collection = conectar('factura')
            resultados = collection.find({})
            objetos = []
            for resultado in resultados:
                objetos.append(resultado)
            messagebox.showinfo('Datos Recuperados:', objetos)
        boton = ttk.Button(ventana, text='Mostrar', command=MostrarFacturas)
        boton.grid(column=1, row=8, padx=5, pady=5)
        boton2 = ttk.Button(ventana, text='Mostrar Todos los Datos', command=MostrarTodoFc)
        boton2.grid(column=1, row=9, columnspan=2, padx=5, pady=5)

    if colecb.get() == 'envio':
        enviol = ttk.Label(ventana, text='Ingrese los datos necesarios para su consulta (no es necesario ingresar todos):')
        enviol.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        fechaenvl = ttk.Label(ventana, text='Fecha Envio:')
        fechaenvl.grid(column=0, row=1, padx=5, pady=5)
        fechaenvt = ttk.Entry(ventana)
        fechaenvt.grid(column=1, row=1, padx=5, pady=5)
        fechaentl = ttk.Label(ventana, text='Fecha Entrega:')
        fechaentl.grid(column=0, row=2, padx=5, pady=5)
        fechaentt = ttk.Entry(ventana)
        fechaentt.grid(column=1, row=2, padx=5, pady=5)
        proveedorl = ttk.Label(ventana, text='Proveedor:')
        proveedorl.grid(column=1, row=3, padx=5, pady=5)
        nombrel = ttk.Label(ventana, text='Nombre:')
        nombrel.grid(column=0, row=4, padx=5, pady=5)
        nombret = ttk.Entry(ventana)
        nombret.grid(column=1, row=4, padx=5, pady=5)
        apellidol = ttk.Label(ventana, text='Apellido:')
        apellidol.grid(column=0, row=5, padx=5, pady=5)
        apellidot = ttk.Entry(ventana)
        apellidot.grid(column=1, row=5, padx=5, pady=5)
        correol = ttk.Label(ventana, text='Correo:')
        correol.grid(column=0, row=6, padx=5, pady=5)
        correot = ttk.Entry(ventana)
        correot.grid(column=1, row=6, padx=5, pady=5)
        teléfonol = ttk.Label(ventana, text='Teléfono:')
        teléfonol.grid(column=0, row=7, padx=5, pady=5)
        teléfonot = ttk.Entry(ventana)
        teléfonot.grid(column=1, row=7, padx=5, pady=5)
        stockenvl = ttk.Label(ventana, text='Stock Enviado:')
        stockenvl.grid(column=1, row=8, padx=5, pady=5)
        nombreprodl = ttk.Label(ventana, text='Nombre Producto:')
        nombreprodl.grid(column=0, row=9, padx=5, pady=5)
        nombrepordt = ttk.Entry(ventana)
        nombrepordt.grid(column=1, row=9, padx=5, pady=5)
        cantidadl = ttk.Label(ventana, text='Cantidad Enviada:')
        cantidadl.grid(column=0, row=10, padx=5, pady=5)
        cantidadt = ttk.Entry(ventana)
        cantidadt.grid(column=1, row=10, padx=5, pady=5)
        filtrol = ttk.Label(ventana, text='Seleccione los datos que quiere recuperar:')
        filtrol.grid(column=2, row=0, padx=5, pady=5)
        var1 = IntVar()
        idc = ttk.Checkbutton(ventana, text='Id', variable=var1)
        idc.grid(column=2, row=1, padx=5, pady=5)
        var2 = IntVar()
        fechaenvc = ttk.Checkbutton(ventana, text='Fecha Envio', variable=var2)
        fechaenvc.grid(column=2, row=2, padx=5, pady=5)
        var3 = IntVar()
        fechaentc = ttk.Checkbutton(ventana, text='Fecha Entrega', variable=var3)
        fechaentc.grid(column=2, row=3, padx=5, pady=5)
        var4 = IntVar()
        proveedorc = ttk.Checkbutton(ventana, text='Proveedor', variable=var4)
        proveedorc.grid(column=2, row=4, padx=5, pady=5)
        var5 = IntVar()
        nombrec = ttk.Checkbutton(ventana, text='Nombre Proveedor', variable=var5)
        nombrec.grid(column=2, row=5, padx=5, pady=5)
        var6 = IntVar()
        apellidoc = ttk.Checkbutton(ventana, text='Apellido Proveedor', variable=var6)
        apellidoc.grid(column=2, row=6, padx=5, pady=5)
        var7 = IntVar()
        correoc = ttk.Checkbutton(ventana, text='Correo Proveedor', variable=var7)
        correoc.grid(column=2, row=7, padx=5, pady=5)
        var8 = IntVar()
        teléfonoc = ttk.Checkbutton(ventana, text='Teléfono Proveedor', variable=var8)
        teléfonoc.grid(column=2, row=8, padx=5, pady=5)
        var9 = IntVar()
        stockenvc = ttk.Checkbutton(ventana, text='Stock Enviado', variable=var9)
        stockenvc.grid(column=2, row=9, padx=5, pady=5)
        var10 = IntVar()
        productoc = ttk.Checkbutton(ventana, text='Nombre Producto', variable=var10)
        productoc.grid(column=2, row=10, padx=5, pady=5)
        var11 = IntVar()
        cantidadc = ttk.Checkbutton(ventana, text='Cantidad Enviada', variable=var11)
        cantidadc.grid(column=2, row=11, padx=5, pady=5)
        def MostrarEnvios():
            filtro = {}
            filtro2 = {}
            if fechaenvt.get() != '':
                filtro.update({'Fecha Envio': fechaenvt.get()})
            if fechaentt.get() != '':
                filtro.update({'Fecha Entrega': fechaentt.get()})
            if nombret.get() != '':
                filtro.update({'Proveedor.Nombre': nombret.get()})
            if apellidot.get() != '':
                filtro.update({'Proveedor.Apellido': apellidot.get()})
            if correot.get() != '':
                filtro.update({'Proveedor.Correo': correot.get()})
            if teléfonot.get() != '':
                filtro.update({'Proveedor.Teléfono': int(teléfonot.get())})
            if nombreprodt.get() != '':
                filtro.update({'Stock Enviado.Nombre Producto': nombeprodt.get()})
            if cantidadt.get() != '':
                filtro.update({'Stock Enviado.Cantidad Enviada': int(cantidadt.get())})
            if var1.get() == 0:
                filtro2.update({'_id':0})
            if var2.get() == 1:
                filtro2.update({'Fecha Envio':1})
            if var3.get() == 1:
                filtro2.update({'Fecha Entrega':1})
            if var4.get() == 1:
                filtro2.update({'Proveedor':1})
            if var4.get() == 0:
                if var5.get() == 1:
                    filtro2.update({'Proveedor.Nombre':1})
                if var6.get() == 1:
                    filtro2.update({'Proveedor.Apellido':1})
                if var7.get() == 1:
                    filtro2.update({'Proveedor.Correo':1})
                if var8.get() == 1:
                    filtro2.update({'Proveedor.Teléfono':1})
            if var9.get() == 1:
                filtro2.update({'Stock Enviado':1})
            if var9.get() == 0:
                if var10.get() == 1:
                    filtro2.update({'Stock Enviado.Nombre Producto':1})
                if var11.get() == 1:
                    filtro2.update({'Stock Enviado.Cantidad Enviada':1})
            collection = conectar('envio')
            resultados = collection.find(filtro, filtro2)
            objetos = []
            for resultado in resultados:
                objetos.append(resultado)
            messagebox.showinfo('Datos Recuperados:', objetos)
        def MostrarTodoEn():
            collection = conectar('envio')
            resultados = collection.find({})
            objetos = []
            for resultado in resultados:
                objetos.append(resultado)
            messagebox.showinfo('Datos Recuperados:', objetos)
        boton = ttk.Button(ventana, text='Mostrar', command=MostrarEnvios)
        boton.grid(column=1, row=11, padx=5, pady=5)
        boton2 = ttk.Button(ventana, text='Mostrar Todos los Datos', command=MostrarTodoEn)
        boton2.grid(column=1, row=12, columnspan=2, padx=5, pady=5)

def Ingresar():
    ventana = Toplevel(root)
    ventana.geometry("990x500")
    if colecb.get() == 'empleado':
        rutl = ttk.Label(ventana, text='Rut:')
        rutl.grid(column=0, row=0, padx=5, pady=5)
        rutt = ttk.Entry(ventana)
        rutt.grid(column=1, row=0, padx=5, pady=5)
        nombrel = ttk.Label(ventana, text='Nombre:')
        nombrel.grid(column=0, row=1, padx=5, pady=5)
        nombret = ttk.Entry(ventana)
        nombret.grid(column=1, row=1, padx=5, pady=5)
        apellidol = ttk.Label(ventana, text='Apellido:')
        apellidol.grid(column=0, row=2, padx=5, pady=5)
        apellidot = ttk.Entry(ventana)
        apellidot.grid(column=1, row=2, padx=5, pady=5)
        edadl = ttk.Label(ventana, text='Edad:')
        edadl.grid(column=0, row=3, padx=5, pady=5)
        edadt = ttk.Entry(ventana)
        edadt.grid(column=1, row=3, padx=5, pady=5)
        salariol = ttk.Label(ventana, text='Salario:')
        salariol.grid(column=0, row=4, padx=5, pady=5)
        salariot = ttk.Entry(ventana)
        salariot.grid(column=1, row=4, padx=5, pady=5)
        teléfonol = ttk.Label(ventana, text='Teléfono:')
        teléfonol.grid(column=0, row=5, padx=5, pady=5)
        teléfonot = ttk.Entry(ventana)
        teléfonot.grid(column=1, row=5, padx=5, pady=5)
        fechal = ttk.Label(ventana, text='Fecha Ingreso:')
        fechal.grid(column=0, row=6, padx=5, pady=5)
        fechat = ttk.Entry(ventana)
        fechat.grid(column=1, row=6, padx=5, pady=5)
        def IngresarEmpleado():
            documento = {
                'rut': rutt.get(),
                'nombre': nombret.get(),
                'apellido': apellidot.get(),
                'edad': int(edadt.get()),
                'salario': int(salariot.get()),
                'teléfono': int(teléfonot.get()),
                'fecha': fechat.get()
            }

            collection = conectar('empleado')
            resultado = collection.insert_one(documento)
            try:
                messagebox.showinfo('Datos Ingresados', 'Los datos se han ingresado correctamente con id: '+ str(resultado.inserted_id))
            except:
                messagebox.showerror('Erro', 'Los datos no se han ingresado correctamente')
        ingresar = ttk.Button(ventana, text='Ingresar', command=IngresarEmpleado)
        ingresar.grid(column=0, row=7, columnspan=2)
        root.mainloop()

    elif colecb.get() == 'producto':
        nombrel = ttk.Label(ventana, text='Nombre:')
        nombrel.grid(column=0, row=0, padx=5, pady=5)
        nombret = ttk.Entry(ventana)
        nombret.grid(column=1, row=0, padx=5, pady=5)
        marcal = ttk.Label(ventana, text='Marca:')
        marcal.grid(column=0, row=1, padx=5, pady=5)
        marcat = ttk.Entry(ventana)
        marcat.grid(column=1, row=1, padx=5, pady=5)
        stockl = ttk.Label(ventana, text='Stock:')
        stockl.grid(column=0, row=2, padx=5, pady=5)
        stockt = ttk.Entry(ventana)
        stockt.grid(column=1, row=2, padx=5, pady=5)
        preciol = ttk.Label(ventana, text='Precio:')
        preciol.grid(column=0, row=3, padx=5, pady=5)
        preciot = ttk.Entry(ventana)
        preciot.grid(column=1, row=3, padx=5, pady=5)
        def IngresarProducto():
            documento = {
                'nombre': nombret.get(),
                'marca': marcat.get(),
                'stock': int(stockt.get()),
                'precio': int(preciot.get())
            }

            collection = conectar('producto')
            resultado = collection.insert_one(documento)
            try:
                messagebox.showinfo('Datos Ingresados', 'Los datos se han ingresado correctamente con id: '+ str(resultado.inserted_id))
            except:
                messagebox.showerror('Erro', 'Los datos no se han ingresado correctamente')
        ingresar = ttk.Button(ventana, text='Ingresar', command=IngresarProducto)
        ingresar.grid(column=0, row=7, columnspan=2)
        root.mainloop()

    elif colecb.get() == 'envio':
        envl = ttk.Label(ventana, text='Envio:')
        envl.grid(column=1, row=0, padx=5, pady=5)
        fechaenvl = ttk.Label(ventana, text='Fecha Envio:')
        fechaenvl.grid(column=0, row=1, padx=5, pady=5)
        fechaenvt = ttk.Entry(ventana)
        fechaenvt.grid(column=1, row=1, padx=5, pady=5)
        fechaentl = ttk.Label(ventana, text='Fecha Entrega:')
        fechaentl.grid(column=0, row=2, padx=5, pady=5)
        fechaentt = ttk.Entry(ventana)
        fechaentt.grid(column=1, row=2, padx=5, pady=5)
        proveedorl = ttk.Label(ventana, text='Proveedor:')
        proveedorl.grid(column=1, row=3, padx=5, pady=5)
        nombrel = ttk.Label(ventana, text='Nombre:')
        nombrel.grid(column=0, row=4, padx=5, pady=5)
        nombret = ttk.Entry(ventana)
        nombret.grid(column=1, row=4, padx=5, pady=5)
        apellidol = ttk.Label(ventana, text='Apellido:')
        apellidol.grid(column=0, row=5, padx=5, pady=5)
        apellidot = ttk.Entry(ventana)
        apellidot.grid(column=1, row=5, padx=5, pady=5)
        correol = ttk.Label(ventana, text='Correo:')
        correol.grid(column=0, row=6, padx=5, pady=5)
        correot = ttk.Entry(ventana)
        correot.grid(column=1, row=6, padx=5, pady=5)
        teléfonol = ttk.Label(ventana, text='Teléfono:')
        teléfonol.grid(column=0, row=7, padx=5, pady=5)
        teléfonot = ttk.Entry(ventana)
        teléfonot.grid(column=1, row=7, padx=5, pady=5)
        stockl = ttk.Label(ventana, text='Stock Enviado (separando por comas cada uno):')
        stockl.grid(column=0, row=8, padx=5, pady=5)
        prodl = ttk.Label(ventana, text='Nombres Productos:')
        prodl.grid(column=0, row=9, padx=5, pady=5)
        prodt = ttk.Entry(ventana)
        prodt.grid(column=1, row=9, columnspan=2, padx=10, pady=10)
        cantl = ttk.Label(ventana, text='Cantidades Enviadas:')
        cantl.grid(column=0, row=10, padx=5, pady=5)
        cantt = ttk.Entry(ventana)
        cantt.grid(column=1, row=10, padx=10, pady=10)
        def IngresarEnvio():
            stockenv = []
            x = prodt.get().split(', ')
            y = cantt.get().split(', ')
            for n in range(len(x)):
                for m in range(len(y)):
                    if n==m:
                        stock = {
                            'Nombre Producto': x[n],
                            'Cantidad Enviada': int(y[m])
                            }
                        stockenv.append(stock)
            documento = {
                'Fecha Envio': fechaenvt.get(),
                'Fecha Entrega': fechaentt.get(),
                'Proveedor': {
                    'Nombre': nombret.get(),
                    'Apellido': apellidot.get(),
                    'Correo': correot.get(),
                    'Teléfono': int(teléfonot.get())
                },
                'Stock Enviado': stockenv
            }

            collection = conectar('envio')
            resultado = collection.insert_one(documento)
            try:
                messagebox.showinfo('Datos Ingresados', 'Los datos se han ingresado correctamente con id: '+ str(resultado.inserted_id))
            except:
                messagebox.showerror('Erro', 'Los datos no se han ingresado correctamente')
        ingresar = ttk.Button(ventana, text='Ingresar', command=IngresarEnvio)
        ingresar.grid(column=0, row=11, columnspan=2)
        root.mainloop()

    elif colecb.get() == 'factura':
        factural = ttk.Label(ventana, text='Factura:')
        factural.grid(column=1, row=0, padx=5, pady=5)
        preciototl = ttk.Label(ventana, text='Precio Total:')
        preciototl.grid(column=0, row=1, padx=5, pady=5)
        preciotott = ttk.Entry(ventana)
        preciotott.grid(column=1, row=1, padx=5, pady=5)
        fechal = ttk.Label(ventana, text='Fecha Factura:')
        fechal.grid(column=0, row=2, padx=5, pady=5)
        fechat = ttk.Entry(ventana)
        fechat.grid(column=1, row=2, padx=5, pady=5)
        empleadol = ttk.Label(ventana, text='Nombre Empleado:')
        empleadol.grid(column=0, row=3, padx=5, pady=5)
        empleadot = ttk.Entry(ventana)
        empleadot.grid(column=1, row=3, padx=5, pady=5)
        detallel = ttk.Label(ventana, text='Detalle (separar por comas cada uno):')
        detallel.grid(column=0, row=4, columnspan=2, padx=5, pady=5)
        productol = ttk.Label(ventana, text='Nombres Productos:')
        productol.grid(column=0, row=5, padx=5, pady=5)
        productot = ttk.Entry(ventana)
        productot.grid(column=1, row=5, padx=5, pady=5)
        cantidadl = ttk.Label(ventana, text='Cantidades Productos:')
        cantidadl.grid(column=0, row=6, padx=5, pady=5)
        cantidadt = ttk.Entry(ventana)
        cantidadt.grid(column=1, row=6, padx=5, pady=5)
        preciol = ttk.Label(ventana, text='Precios:')
        preciol.grid(column=0, row=7, padx=5, pady=5)
        preciot = ttk.Entry(ventana)
        preciot.grid(column=1, row=7, padx=5, pady=5)
        def IngresarFactura():
            producto = []
            x = productot.get().split(', ')
            y = cantidadt.get().split(', ')
            z = preciot.get().split(', ')
            for n in range(len(x)):
                for m in range(len(y)):
                    for o in range(len(z)):
                        if n==m:
                            if n==o:
                                prod = {
                                    'Nombre Producto': x[n],
                                    'Cantidad': int(y[m]),
                                    'Precio': int(z[o])
                                    }
                                producto.append(prod)
            documento = {
                'Precio Total': int(preciotott.get()),
                'Fecha Factura': fechat.get(),
                'Nombre Empleado': empleadot.get(),
                'Detalle': producto
            }

            collection = conectar('factura')
            resultado = collection.insert_one(documento)
            try:
                messagebox.showinfo('Datos Ingresados', 'Los datos se han ingresado correctamente con id: '+ str(resultado.inserted_id))
            except:
                messagebox.showerror('Erro', 'Los datos no se han ingresado correctamente')
        ingresar = ttk.Button(ventana, text='Ingresar', command=IngresarFactura)
        ingresar.grid(column=0, row=8, columnspan=2)
        root.mainloop()

def Actualizar():
    ventana = Toplevel(root)
    ventana.geometry("990x500")
    if colecb.get() == 'empleado':
        empleadol = ttk.Label(ventana, text='Ingrese el/los datos que quiere actualizar:')
        empleadol.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        rutl = ttk.Label(ventana, text='Rut:')
        rutl.grid(column=0, row=1, padx=5, pady=5)
        rutt = ttk.Entry(ventana)
        rutt.grid(column=1, row=1, padx=5, pady=5)
        nombrel = ttk.Label(ventana, text='Nombre:')
        nombrel.grid(column=0, row=2, padx=5, pady=5)
        nombret = ttk.Entry(ventana)
        nombret.grid(column=1, row=2, padx=5, pady=5)
        apellidol = ttk.Label(ventana, text='Apellido:')
        apellidol.grid(column=0, row=3, padx=5, pady=5)
        apellidot = ttk.Entry(ventana)
        apellidot.grid(column=1, row=3, padx=5, pady=5)
        edadl = ttk.Label(ventana, text='Edad:')
        edadl.grid(column=0, row=4, padx=5, pady=5)
        edadt = ttk.Entry(ventana)
        edadt.grid(column=1, row=4, padx=5, pady=5)
        salariol = ttk.Label(ventana, text='Salario:')
        salariol.grid(column=0, row=5, padx=5, pady=5)
        salariot = ttk.Entry(ventana)
        salariot.grid(column=1, row=5, padx=5, pady=5)
        teléfonol = ttk.Label(ventana, text='Teléfono:')
        teléfonol.grid(column=0, row=6, padx=5, pady=5)
        teléfonot = ttk.Entry(ventana)
        teléfonot.grid(column=1, row=6, padx=5, pady=5)
        fechal = ttk.Label(ventana, text='Fecha Ingreso:')
        fechal.grid(column=0, row=7, padx=5, pady=5)
        fechat = ttk.Entry(ventana)
        fechat.grid(column=1, row=7, padx=5, pady=5)
        empleado2l = ttk.Label(ventana, text='Ingrese el/los nuevos valores de los datos:')
        empleado2l.grid(column=2, row=0, columnspan=2, padx=5, pady=5)
        rut2l = ttk.Label(ventana, text='Rut:')
        rut2l.grid(column=2, row=1, padx=5, pady=5)
        rut2t = ttk.Entry(ventana)
        rut2t.grid(column=3, row=1, padx=5, pady=5)
        nombre2l = ttk.Label(ventana, text='Nombre:')
        nombre2l.grid(column=2, row=2, padx=5, pady=5)
        nombre2t = ttk.Entry(ventana)
        nombre2t.grid(column=3, row=2, padx=5, pady=5)
        apellido2l = ttk.Label(ventana, text='Apellido:')
        apellido2l.grid(column=2, row=3, padx=5, pady=5)
        apellido2t = ttk.Entry(ventana)
        apellido2t.grid(column=3, row=3, padx=5, pady=5)
        edad2l = ttk.Label(ventana, text='Edad:')
        edad2l.grid(column=2, row=4, padx=5, pady=5)
        edad2t = ttk.Entry(ventana)
        edad2t.grid(column=3, row=4, padx=5, pady=5)
        salario2l = ttk.Label(ventana, text='Salario:')
        salario2l.grid(column=2, row=5, padx=5, pady=5)
        salario2t = ttk.Entry(ventana)
        salario2t.grid(column=3, row=5, padx=5, pady=5)
        teléfono2l = ttk.Label(ventana, text='Teléfono:')
        teléfono2l.grid(column=2, row=6, padx=5, pady=5)
        teléfono2t = ttk.Entry(ventana)
        teléfono2t.grid(column=3, row=6, padx=5, pady=5)
        fecha2l = ttk.Label(ventana, text='Fecha Ingreso:')
        fecha2l.grid(column=2, row=7, padx=5, pady=5)
        fecha2t = ttk.Entry(ventana)
        fecha2t.grid(column=3, row=7, padx=5, pady=5)
        def ActualizarEmpleados():
            filtro = {}
            filtro2 = {}
            if rutt.get() != '':
                filtro.update({'rut': rutt.get()})
            if nombret.get() != '':
                filtro.update({'nombre': nombret.get()})
            if apellidot.get() != '':
                filtro.update({'apellido': apellidot.get()})
            if edadt.get() != '':
                filtro.update({'edad': int(edadt.get())})
            if salariot.get() != '':
                filtro.update({'salario': int(salariot.get())})
            if teléfonot.get() != '':
                filtro.update({'teléfono': int(teléfonot.get())})
            if fechat.get() != '':
                filtro.update({'fecha': fechat.get()})
            if rut2t.get() != '':
                filtro2.update({'rut': rut2t.get()})
            if nombre2t.get() !=  '':
                filtro2.update({'nombre': nombre2t.get()})
            if apellido2t.get() != '':
                filtro2.update({'apellido': apellido2t.get()})
            if edad2t.get() != '':
                filtro2.update({'edad': int(edad2t.get())})
            if salario2t.get() != '':
                filtro2.update({'salario': int(salario2t.get())})
            if teléfono2t.get() != '':
                filtro2.update({'teléfono': teléfono2t.get()})
            if fecha2t.get() != '':
                filtro2.update({'fecha': fecha2t.get()})
            collection = conectar('empleado')
            resultados = collection.update_many(filtro, {'$set':filtro2})
            if resultados.modified_count == 1:
                messagebox.showinfo('Datos Actualizados', 'Se ha modificado '+ str(resultados.modified_count)+ " dato")
            elif resultados.modified_count > 1:
                messagebox.showinfo('Datos Actualizados', 'Se han modificado '+ str(resultados.modified_count)+ " datos")
            else:
                messagebox.showerror('Error', 'No se ha actualizado ningún dato')
        actualizar = ttk.Button(ventana, text='Actualizar', command=ActualizarEmpleados)
        actualizar.grid(column=1, row=8, columnspan=2)
        root.mainloop()

    elif colecb.get() == 'producto':
        productol = ttk.Label(ventana, text='Ingrese el/los datos que quiere actualizar:')
        productol.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        nombrel = ttk.Label(ventana, text='Nombre:')
        nombrel.grid(column=0, row=1, padx=5, pady=5)
        nombret = ttk.Entry(ventana)
        nombret.grid(column=1, row=1, padx=5, pady=5)
        marcal = ttk.Label(ventana, text='Marca:')
        marcal.grid(column=0, row=2, padx=5, pady=5)
        marcat = ttk.Entry(ventana)
        marcat.grid(column=1, row=2, padx=5, pady=5)
        stockl = ttk.Label(ventana, text='Stock:')
        stockl.grid(column=0, row=3, padx=5, pady=5)
        stockt = ttk.Entry(ventana)
        stockt.grid(column=1, row=3, padx=5, pady=5)
        preciol = ttk.Label(ventana, text='Precio:')
        preciol.grid(column=0, row=4, padx=5, pady=5)
        preciot = ttk.Entry(ventana)
        preciot.grid(column=1, row=4, padx=5, pady=5)
        productol2 = ttk.Label(ventana, text='Ingrese el/los nuevos valores de los datos:')
        productol2.grid(column=2, row=0, columnspan=2, padx=5, pady=5)
        nombrel2 = ttk.Label(ventana, text='Nombre:')
        nombrel2.grid(column=2, row=1, padx=5, pady=5)
        nombret2 = ttk.Entry(ventana)
        nombret2.grid(column=3, row=1, padx=5, pady=5)
        marcal2 = ttk.Label(ventana, text='Marca:')
        marcal2.grid(column=2, row=2, padx=5, pady=5)
        marcat2 = ttk.Entry(ventana)
        marcat2.grid(column=3, row=2, padx=5, pady=5)
        stockl2 = ttk.Label(ventana, text='Stock:')
        stockl2.grid(column=2, row=3, padx=5, pady=5)
        stockt2 = ttk.Entry(ventana)
        stockt2.grid(column=3, row=3, padx=5, pady=5)
        preciol2 = ttk.Label(ventana, text='Precio:')
        preciol2.grid(column=2, row=4, padx=5, pady=5)
        preciot2 = ttk.Entry(ventana)
        preciot2.grid(column=3, row=4, padx=5, pady=5)
        def ActualizarProductos():
            filtro = {}
            filtro2 = {}
            if nombret.get() != '':
                filtro.update({'nombre': nombret.get()})
            if marcat.get() != '':
                filtro.update({'marca': marcat.get()})
            if stockt.get() != '':
                filtro.update({'stock': int(stockt.get())})
            if preciot.get() != '':
                filtro.update({'precio': int(preciot.get())})
            if nombret2.get() != '':
                filtro2.update({'nombre': nombret2.get()})
            if marcat2.get() != '':
                filtro2.update({'marca': marcat2.get()})
            if stockt2.get() != '':
                filtro2.update({'stock': int(stockt2.get())})
            if preciot2.get() != '':
                filtro2.update({'precio': int(preciot2.get())})
            collection = conectar('producto')
            resultados = collection.update_many(filtro, {'$set':filtro2})
            if resultados.modified_count == 1:
                messagebox.showinfo('Datos Actualizados', 'Se ha modificado '+ str(resultados.modified_count)+ " dato")
            elif resultados.modified_count > 1:
                messagebox.showinfo('Datos Actualizados', 'Se han modificado '+ str(resultados.modified_count)+ " datos")
            else:
                messagebox.showerror('Error', 'No se ha actualizado ningún dato')
        actualizar = ttk.Button(ventana, text='Actualizar', command=ActualizarProductos)
        actualizar.grid(column=1, row=5, columnspan=2)
        root.mainloop()

    elif colecb.get() == 'envio':
        modl = ttk.Label(ventana, text='Ingrese el/los datos que quiere actualizar:')
        modl.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        envl = ttk.Label(ventana, text='Envio:')
        envl.grid(column=1, row=1, padx=5, pady=5)
        fechaenvl = ttk.Label(ventana, text='Fecha Envio:')
        fechaenvl.grid(column=0, row=2, padx=5, pady=5)
        fechaenvt = ttk.Entry(ventana)
        fechaenvt.grid(column=1, row=2, padx=5, pady=5)
        fechaentl = ttk.Label(ventana, text='Fecha Entrega:')
        fechaentl.grid(column=0, row=3, padx=5, pady=5)
        fechaentt = ttk.Entry(ventana)
        fechaentt.grid(column=1, row=3, padx=5, pady=5)
        proveedorl = ttk.Label(ventana, text='Proveedor:')
        proveedorl.grid(column=1, row=4, padx=5, pady=5)
        nombrel = ttk.Label(ventana, text='Nombre:')
        nombrel.grid(column=0, row=5, padx=5, pady=5)
        nombret = ttk.Entry(ventana)
        nombret.grid(column=1, row=5, padx=5, pady=5)
        apellidol = ttk.Label(ventana, text='Apellido:')
        apellidol.grid(column=0, row=6, padx=5, pady=5)
        apellidot = ttk.Entry(ventana)
        apellidot.grid(column=1, row=6, padx=5, pady=5)
        correol = ttk.Label(ventana, text='Correo:')
        correol.grid(column=0, row=7, padx=5, pady=5)
        correot = ttk.Entry(ventana)
        correot.grid(column=1, row=7, padx=5, pady=5)
        teléfonol = ttk.Label(ventana, text='Teléfono:')
        teléfonol.grid(column=0, row=8, padx=5, pady=5)
        teléfonot = ttk.Entry(ventana)
        teléfonot.grid(column=1, row=8, padx=5, pady=5)
        stockl = ttk.Label(ventana, text='Stock Enviado:')
        stockl.grid(column=0, row=9, columnspan=2, padx=5, pady=5)
        prodl = ttk.Label(ventana, text='Nombres Productos:')
        prodl.grid(column=0, row=10, padx=5, pady=5)
        prodt = ttk.Entry(ventana)
        prodt.grid(column=1, row=10, padx=10, pady=10)
        cantl = ttk.Label(ventana, text='Cantidades Enviadas:')
        cantl.grid(column=0, row=11, padx=5, pady=5)
        cantt = ttk.Entry(ventana)
        cantt.grid(column=1, row=11, padx=10, pady=10)
        modl2 = ttk.Label(ventana, text='Ingrese el/los nuevos valores de los datos:')
        modl2.grid(column=2, row=0, columnspan=2, padx=5, pady=5)
        envl2 = ttk.Label(ventana, text='Envio:')
        envl2.grid(column=3, row=1, padx=5, pady=5)
        fechaenvl2 = ttk.Label(ventana, text='Fecha Envio:')
        fechaenvl2.grid(column=2, row=2, padx=5, pady=5)
        fechaenvt2 = ttk.Entry(ventana)
        fechaenvt2.grid(column=3, row=2, padx=5, pady=5)
        fechaentl2 = ttk.Label(ventana, text='Fecha Entrega:')
        fechaentl2.grid(column=2, row=3, padx=5, pady=5)
        fechaentt2 = ttk.Entry(ventana)
        fechaentt2.grid(column=3, row=3, padx=5, pady=5)
        proveedorl2 = ttk.Label(ventana, text='Proveedor:')
        proveedorl2.grid(column=3, row=4, padx=5, pady=5)
        nombrel2 = ttk.Label(ventana, text='Nombre:')
        nombrel2.grid(column=2, row=5, padx=5, pady=5)
        nombret2 = ttk.Entry(ventana)
        nombret2.grid(column=3, row=5, padx=5, pady=5)
        apellidol2 = ttk.Label(ventana, text='Apellido:')
        apellidol2.grid(column=2, row=6, padx=5, pady=5)
        apellidot2 = ttk.Entry(ventana)
        apellidot2.grid(column=3, row=6, padx=5, pady=5)
        correol2 = ttk.Label(ventana, text='Correo:')
        correol2.grid(column=2, row=7, padx=5, pady=5)
        correot2 = ttk.Entry(ventana)
        correot2.grid(column=3, row=7, padx=5, pady=5)
        teléfonol2 = ttk.Label(ventana, text='Teléfono:')
        teléfonol2.grid(column=2, row=8, padx=5, pady=5)
        teléfonot2 = ttk.Entry(ventana)
        teléfonot2.grid(column=3, row=8, padx=5, pady=5)
        stockl2 = ttk.Label(ventana, text='Stock Enviado (Separado por comas cada uno):')
        stockl2.grid(column=3, row=9, padx=5, pady=5)
        prodl2 = ttk.Label(ventana, text='Nombres Productos:')
        prodl2.grid(column=2, row=10, padx=5, pady=5)
        prodt2 = ttk.Entry(ventana)
        prodt2.grid(column=3, row=10, columnspan=2, padx=10, pady=10)
        cantl2 = ttk.Label(ventana, text='Cantidades Enviadas:')
        cantl2.grid(column=2, row=11, padx=5, pady=5)
        cantt2 = ttk.Entry(ventana)
        cantt2.grid(column=3, row=11, padx=10, pady=10)
        def ActualizarEnvios():
            filtro = {}
            filtro2 = {}
            stockenviado = []
            if fechaenvt.get() != '':
                filtro.update({'Fecha Envio': fechaenvt.get()})
            if fechaentt.get() != '':
                filtro.update({'Fecha Entrega': fechaentt.get()})
            if nombret.get() != '':
                filtro.update({'Proveedor.Nombre': nombret.get()})
            if apellidot.get() != '':
                filtro.update({'Proveedor.Apellido': apellidot.get()})
            if correot.get() != '':
                filtro.update({'Proveedor.Correo': correot.get()})
            if teléfonot.get() != '':
                filtro.update({'Proveedor.Teléfono': int(teléfonot.get())})
            if prodt.get() != '':
                filtro.update({'Stock Enviado.Nombre Producto': prodt.get()})
            if cantt.get() != '':
                filtro.update({'Stock Enviado.Cantidad Enviada': int(cantt.get())})
            if fechaenvt2.get() != '':
                filtro2.update({'Fecha Envio': fechaenvt2.get()})
            if fechaentt2.get() != '':
                filtro2.update({'Fecha Entrega': fechaentt2.get()})
            if nombret2.get() != '':
                filtro2.update({'Proveedor.Nombre': nombret2.get()})
            if apellidot2.get() != '':
                filtro2.update({'Proveedor.Apellido': apellidot2.get()})
            if correot2.get() != '':
                filtro2.update({'Proveedor.Correo': correot2.get()})
            if teléfonot2.get() != '':
                filtro2.update({'Proveedor.Teléfono': int(teléfonot2.get())})
            if prodt2.get() != '':
                if cantt2.get() != '':
                    x = prodt2.get().split(', ')
                    y = cantt2.get().split(', ')
                    for n in range(len(x)):
                        for m in range(len(y)):
                            if n==m:
                                stock = {
                                    'Nombre Producto': x[n],
                                    'Cantidad Enviada': int(y[m])
                                    }
                                stockenviado.append(stock)
                    filtro2.update({'Stock Enviado': stockenviado})
            collection = conectar('envio')
            resultados = collection.update_many(filtro, {'$set':filtro2})
            if resultados.modified_count == 1:
                messagebox.showinfo('Datos Actualizados', 'Se ha modificado '+ str(resultados.modified_count)+ " dato")
            elif resultados.modified_count > 1:
                messagebox.showinfo('Datos Actualizados', 'Se han modificado '+ str(resultados.modified_count)+ " datos")
            else:
                messagebox.showerror('Error', 'No se ha actualizado ningún dato')

        actualizar = ttk.Button(ventana, text='Actualizar', command=ActualizarEnvios)
        actualizar.grid(column=1, row=12, columnspan=2)
        root.mainloop()

    elif colecb.get() == 'factura':
        modl = ttk.Label(ventana, text='Ingrese el/los datos que quiere actualizar:')
        modl.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        factural = ttk.Label(ventana, text='Factura:')
        factural.grid(column=1, row=1, padx=5, pady=5)
        preciototl = ttk.Label(ventana, text='Precio Total:')
        preciototl.grid(column=0, row=2, padx=5, pady=5)
        preciotott = ttk.Entry(ventana)
        preciotott.grid(column=1, row=2, padx=5, pady=5)
        fechal = ttk.Label(ventana, text='Fecha Factura:')
        fechal.grid(column=0, row=3, padx=5, pady=5)
        fechat = ttk.Entry(ventana)
        fechat.grid(column=1, row=3, padx=5, pady=5)
        empleadol = ttk.Label(ventana, text='Nombre Empleado:')
        empleadol.grid(column=0, row=4, padx=5, pady=5)
        empleadot = ttk.Entry(ventana)
        empleadot.grid(column=1, row=4, padx=5, pady=5)
        detallel = ttk.Label(ventana, text='Detalle:')
        detallel.grid(column=0, row=5, columnspan=2, padx=5, pady=5)
        productol = ttk.Label(ventana, text='Nombres Productos:')
        productol.grid(column=0, row=6, padx=5, pady=5)
        productot = ttk.Entry(ventana)
        productot.grid(column=1, row=6, padx=5, pady=5)
        cantidadl = ttk.Label(ventana, text='Cantidades Productos:')
        cantidadl.grid(column=0, row=7, padx=5, pady=5)
        cantidadt = ttk.Entry(ventana)
        cantidadt.grid(column=1, row=7, padx=5, pady=5)
        preciol = ttk.Label(ventana, text='Precios:')
        preciol.grid(column=0, row=8, padx=5, pady=5)
        preciot = ttk.Entry(ventana)
        preciot.grid(column=1, row=8, padx=5, pady=5)
        modl2 = ttk.Label(ventana, text='Ingrese el/los nuevos valores de los datos:')
        modl2.grid(column=2, row=0, columnspan=2, padx=5, pady=5)
        factural2 = ttk.Label(ventana, text='Factura:')
        factural2.grid(column=3, row=1, padx=5, pady=5)
        preciototl2 = ttk.Label(ventana, text='Precio Total:')
        preciototl2.grid(column=2, row=2, padx=5, pady=5)
        preciotott2 = ttk.Entry(ventana)
        preciotott2.grid(column=3, row=2, padx=5, pady=5)
        fechal2 = ttk.Label(ventana, text='Fecha Factura:')
        fechal2.grid(column=2, row=3, padx=5, pady=5)
        fechat2 = ttk.Entry(ventana)
        fechat2.grid(column=3, row=3, padx=5, pady=5)
        empleadol2 = ttk.Label(ventana, text='Nombre Empleado:')
        empleadol2.grid(column=2, row=4, padx=5, pady=5)
        empleadot2 = ttk.Entry(ventana)
        empleadot2.grid(column=3, row=4, padx=5, pady=5)
        detallel2 = ttk.Label(ventana, text='Detalle (separar por comas cada uno):')
        detallel2.grid(column=2, row=5, columnspan=2, padx=5, pady=5)
        productol2 = ttk.Label(ventana, text='Nombres Productos:')
        productol2.grid(column=2, row=6, padx=5, pady=5)
        productot2 = ttk.Entry(ventana)
        productot2.grid(column=3, row=6, padx=5, pady=5)
        cantidadl2 = ttk.Label(ventana, text='Cantidades Productos:')
        cantidadl2.grid(column=2, row=7, padx=5, pady=5)
        cantidadt2 = ttk.Entry(ventana)
        cantidadt2.grid(column=3, row=7, padx=5, pady=5)
        preciol2 = ttk.Label(ventana, text='Precios:')
        preciol2.grid(column=2, row=8, padx=5, pady=5)
        preciot2 = ttk.Entry(ventana)
        preciot2.grid(column=3, row=8, padx=5, pady=5)
        def MostrarFactura():
            filtro = {}
            filtro2 = {}
            if preciotott.get() != '':
                filtro.update({'Precio Total': int(preciotott.get())})
            if fechat.get() != '':
                filtro.update({'Fecha Factura': fechat.get()})
            if empleadot.get() != '':
                filtro.update({'Nombre Empleado': empleadot.get()})
            if productot.get() != '':
                filtro.update({'Detalle.Nombre Producto': productot.get()})
            if cantidadt.get() != '':
                filtro.update({'Detalle.Cantidad': int(cantidadt.get())})
            if preciot.get() != '':
                filtro.update({'Detalle.Precio': int(preciot.get())})
            if preciotott2.get() != '':
                filtro.update({'Precio Total': int(preciotott2.get())})
            if fechat2.get() != '':
                filtro2.update({'Fecha Factura': fechat2.get()})
            if empleadot2.get() != '':
                filtro2.update({'Nombre Empleado': empleadot2.get()})
            if productot2.get() != '':
                if cantidadt2.get() != '':
                    if preciot2.get() != '':
                        producto = []
                        x = productot2.get().split(', ')
                        y = cantidadt2.get().split(', ')
                        z = preciot2.get().split(', ')
                        for n in range(len(x)):
                            for m in range(len(y)):
                                for o in range(len(z)):
                                    if n==m:
                                        if n==o:
                                            prod = {
                                                'Nombre Producto': x[n],
                                                'Cantidad': int(y[m]),
                                                'Precio': int(z[o])
                                                }
                                            producto.append(prod)
                        filtro2.update({'Detalle': producto})
            collection = conectar('factura')
            resultados = collection.update_many(filtro, {'$set':filtro2})
            if resultados.modified_count == 1:
                messagebox.showinfo('Datos Actualizados', 'Se ha modificado '+ str(resultados.modified_count)+ " dato")
            elif resultados.modified_count > 1:
                messagebox.showinfo('Datos Actualizados', 'Se han modificado '+ str(resultados.modified_count)+ " datos")
            else:
                messagebox.showerror('Error', 'No se ha actualizado ningún dato')
        actualizar = ttk.Button(ventana, text='Actualizar', command=MostrarFactura)
        actualizar.grid(column=1, row=9, columnspan=2)
        root.mainloop()

Mostrar = ttk.Button(frame, text='Mostrar datos', command=Mostrar)
Mostrar.grid(column=1, row=1, padx=5, pady=5)
Insertar = ttk.Button(frame, text='Insertar datos', command=Ingresar)
Insertar.grid(column=2, row=1, padx=5, pady=5)
Actualizar = ttk.Button(frame, text='Actualizar datos', command=Actualizar)
Actualizar.grid(column=3, row=1, padx=5, pady=5)
def EliminarDatos():
    root2 = Tk()
    root2.geometry("990x500")
    root2.wm_title('Ingresar')
    root2.minsize(width=950, height=325)
    frame2 = Frame(root2)
    frame2.grid(column=0, row=0, sticky='nsew')
    if colecb.get() == 'empleado':
        rutl = ttk.Label(frame2, text='Rut:')
        rutl.grid(column=0, row=0, padx=5, pady=5)
        rutt = ttk.Entry(frame2)
        rutt.grid(column=1, row=0, padx=5, pady=5)
        
        def Eliminar():
            documento = {
                'rut': rutt.get()
            }

            collection = conectar('empleado')
            resultado = collection.delete_one(documento)

            if resultado.deleted_count == 1:
                messagebox.showinfo("Eliminación exitosa", "El documento se eliminó exitosamente.")
            else:
                messagebox.showerror("Error", "No se encontró el empleado especificado.")
        
        elim = ttk.Button(frame2, text='Eliminar', command=Eliminar)
        elim.grid(column=2, row=3, padx=5, pady=5)

    if colecb.get() == 'producto': 
        nombrel = ttk.Label(frame2, text='Nombre:')
        nombrel.grid(column=0, row=0, padx=5, pady=5)
        nombret = ttk.Entry(frame2)
        nombret.grid(column=1, row=0, padx=5, pady=5)

        marcal = ttk.Label(frame2, text='Marca:')
        marcal.grid(column=0, row=1, padx=5, pady=5)
        marcat = ttk.Entry(frame2)
        marcat.grid(column=1, row=1, padx=5, pady=5)

        preciol = ttk.Label(frame2, text='Precio:')
        preciol.grid(column=0, row=2, padx=5, pady=5)
        preciot = ttk.Entry(frame2)
        preciot.grid(column=1, row=2, padx=5, pady=5)


        def Eliminar():
            documento = {
                'nombre': nombret.get(),
                'marca' : marcat.get(),
                'precio' : int(preciot.get())
            }

            collection = conectar('producto')
            resultado = collection.delete_one(documento)

            if resultado.deleted_count == 1:
                messagebox.showinfo("Eliminación exitosa", "El producto se eliminó exitosamente.")
            else:
                messagebox.showerror("Error", "No se encontró el producto especificado.")
        
        elim = ttk.Button(frame2, text='Eliminar', command=Eliminar)
        elim.grid(column=2, row=0, padx=5, pady=5)

    if colecb.get() == 'envio': 
        fechaenviol = ttk.Label(frame2, text='Fecha Envio:')
        fechaenviol.grid(column=0, row=0, padx=5, pady=5)
        fechaenviot = ttk.Entry(frame2)
        fechaenviot.grid(column=1, row=0, padx=5, pady=5)

        nombrel = ttk.Label(frame2, text='Nombre Proveedor:')
        nombrel.grid(column=0, row=1, padx=5, pady=5)
        nombret = ttk.Entry(frame2)
        nombret.grid(column=1, row=1, padx=5, pady=5)

        apellidol = ttk.Label(frame2, text='Apellido Proveedor:')
        apellidol.grid(column=0, row=2, padx=5, pady=5)
        apellidot = ttk.Entry(frame2)
        apellidot.grid(column=1, row=2, padx=5, pady=5)

        telefonol = ttk.Label(frame2, text='Telefono:')
        telefonol.grid(column=0, row=3, padx=5, pady=5)
        telefonot = ttk.Entry(frame2)
        telefonot.grid(column=1, row=3, padx=5, pady=5)



        def Eliminar():
            documento = {
                'Fecha Envio': fechaenviot.get(),
                'Proveedor.Nombre' : nombret.get(),
                'Proveedor.Apellido' : apellidot.get(),
                'Proveedor.Teléfono' : int(telefonot.get())
            }

            collection = conectar('envio')
            resultado = collection.delete_one(documento)

            if resultado.deleted_count == 1:
                messagebox.showinfo("Eliminación exitosa", "El proveedor se eliminó exitosamente.")
                root2.destroy()
            else:
                messagebox.showerror("Error", "No se encontró el proveedor especificado.")
        
        elim = ttk.Button(frame2, text='Eliminar', command=Eliminar)
        elim.grid(column=1, row=4, padx=5, pady=5)
    
Eliminar = ttk. Button(frame, text='Eliminar datos', command=EliminarDatos)
Eliminar.grid(column=4, row=1)
root.mainloop()