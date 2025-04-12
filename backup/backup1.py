import pymongo
from pymongo import MongoClient
from tkinter import Tk, Frame, ttk, messagebox, IntVar

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
    root2 = Tk()
    root2.geometry("990x500")
    root2.wm_title('Ingresar')
    root2.minsize(width=950, height=325)
    frame2 = Frame(root2)
    frame2.grid(column=0, row=0, sticky='nsew')
    if colecb.get() == 'empleado':
        empleadol = ttk.Label(frame2, text='Ingrese los datos necesarios para su consulta (no es necesario ingresar todos):')
        empleadol.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        rutl = ttk.Label(frame2, text='Rut:')
        rutl.grid(column=0, row=1, padx=5, pady=5)
        rutt = ttk.Entry(frame2)
        rutt.grid(column=1, row=1, padx=5, pady=5)
        nombrel = ttk.Label(frame2, text='Nombre:')
        nombrel.grid(column=0, row=2, padx=5, pady=5)
        nombret = ttk.Entry(frame2)
        nombret.grid(column=1, row=2, padx=5, pady=5)
        apellidol = ttk.Label(frame2, text='Apellido:')
        apellidol.grid(column=0, row=3, padx=5, pady=5)
        apellidot = ttk.Entry(frame2)
        apellidot.grid(column=1, row=3, padx=5, pady=5)
        edadl = ttk.Label(frame2, text='Edad:')
        edadl.grid(column=0, row=4, padx=5, pady=5)
        edadt = ttk.Entry(frame2)
        edadt.grid(column=1, row=4, padx=5, pady=5)
        salariol = ttk.Label(frame2, text='Salario:')
        salariol.grid(column=0, row=5, padx=5, pady=5)
        salariot = ttk.Entry(frame2)
        salariot.grid(column=1, row=5, padx=5, pady=5)
        teléfonol = ttk.Label(frame2, text='Teléfono:')
        teléfonol.grid(column=0, row=6, padx=5, pady=5)
        teléfonot = ttk.Entry(frame2)
        teléfonot.grid(column=1, row=6, padx=5, pady=5)
        fechal = ttk.Label(frame2, text='Fecha Ingreso:')
        fechal.grid(column=0, row=7, padx=5, pady=5)
        fechat = ttk.Entry(frame2)
        fechat.grid(column=1, row=7, padx=5, pady=5)
        filtrol = ttk.Label(frame2, text='Seleccione los datos que quiere recuperar:')
        filtrol.grid(column=2, row=0, padx=5, pady=5)
        var1 = IntVar()
        idc = ttk.Checkbutton(frame2, text='Id', variable=var1)
        idc.grid(column=2, row=1, padx=5, pady=5)
        var2 = IntVar()
        rutc = ttk.Checkbutton(frame2, text='Rut', variable=var2)
        rutc.grid(column=2, row=2, padx=5, pady=5)
        var3 = IntVar()
        nombrec = ttk.Checkbutton(frame2, text='Nombre', variable=var3)
        nombrec.grid(column=2, row=3, padx=5, pady=5)
        var4 = IntVar()
        apellidoc = ttk.Checkbutton(frame2, text='Apellido', variable=var4)
        apellidoc.grid(column=2, row=4, padx=5, pady=5)
        var5 = IntVar()
        edadc = ttk.Checkbutton(frame2, text='Edad', variable=var5)
        edadc.grid(column=2, row=5, padx=5, pady=5)
        var6 = IntVar()
        salarioc = ttk.Checkbutton(frame2, text='Salario', variable=var6)
        salarioc.grid(column=2, row=6, padx=5, pady=5)
        var7 = IntVar()
        teléfonoc = ttk.Checkbutton(frame2, text='Teléfono', variable=var7)
        teléfonoc.grid(column=2, row=7, padx=5, pady=5)
        var8 = IntVar()
        fechac = ttk.Checkbutton(frame2, text='Fecha', variable=var8)
        fechac.grid(column=2, row=8, padx=5, pady=5)
        def MostrarEmpleados():
            filtro = {}
            if rutt.get() != '':
                filtro.update({'rut': rutt.get()})
            elif nombret.get() != '':
                filtro.update({'nombre': nombret.get()})
            elif apellidot.get() != '':
                filtro.update({'apellido': apellidot.get()})
            elif edadt.get() != '':
                filtro.update({'edad': int(edadt.get())})
            elif salariot.get() != '':
                filtro.update({'salario': int(salariot.get())})
            elif teléfonot.get() != '':
                filtro.update({'teléfono': int(teléfonot.get())})
            elif fechat.get() != '':
                filtro.update({'fecha': fechat.get()})
            collection = conectar('empleado')
            resultados = collection.find(filtro)
            objetos = []
            for resultado in resultados:
                objetos.append(resultado)
            messagebox.showinfo('Datos Recuperados:', objetos)
        def MostrarTodo():
            print(var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get())
            collection = conectar('empleado')
            resultados = collection.find({})
            objetos = []
            for resultado in resultados:
                objetos.append(resultado['nombre'])
            messagebox.showinfo('Datos Recuperados:', objetos)
        boton = ttk.Button(frame2, text='Mostrar', command=MostrarEmpleados)
        boton.grid(column=1, row=8, padx=5, pady=5)
        boton2 = ttk.Button(frame2, text='Mostrar Todos los Datos', command=MostrarTodo)
        boton2.grid(column=0, row=9, columnspan=2, padx=5, pady=5)

def Ingresar():
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
        nombrel = ttk.Label(frame2, text='Nombre:')
        nombrel.grid(column=0, row=1, padx=5, pady=5)
        nombret = ttk.Entry(frame2)
        nombret.grid(column=1, row=1, padx=5, pady=5)
        apellidol = ttk.Label(frame2, text='Apellido:')
        apellidol.grid(column=0, row=2, padx=5, pady=5)
        apellidot = ttk.Entry(frame2)
        apellidot.grid(column=1, row=2, padx=5, pady=5)
        edadl = ttk.Label(frame2, text='Edad:')
        edadl.grid(column=0, row=3, padx=5, pady=5)
        edadt = ttk.Entry(frame2)
        edadt.grid(column=1, row=3, padx=5, pady=5)
        salariol = ttk.Label(frame2, text='Salario:')
        salariol.grid(column=0, row=4, padx=5, pady=5)
        salariot = ttk.Entry(frame2)
        salariot.grid(column=1, row=4, padx=5, pady=5)
        teléfonol = ttk.Label(frame2, text='Teléfono:')
        teléfonol.grid(column=0, row=5, padx=5, pady=5)
        teléfonot = ttk.Entry(frame2)
        teléfonot.grid(column=1, row=5, padx=5, pady=5)
        fechal = ttk.Label(frame2, text='Fecha Ingreso:')
        fechal.grid(column=0, row=6, padx=5, pady=5)
        fechat = ttk.Entry(frame2)
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
        ingresar = ttk.Button(frame2, text='Ingresar', command=IngresarEmpleado)
        ingresar.grid(column=0, row=7, columnspan=2)
        root2.mainloop()

    elif colecb.get() == 'producto':
        nombrel = ttk.Label(frame2, text='Nombre:')
        nombrel.grid(column=0, row=0, padx=5, pady=5)
        nombret = ttk.Entry(frame2)
        nombret.grid(column=1, row=0, padx=5, pady=5)
        marcal = ttk.Label(frame2, text='Marca:')
        marcal.grid(column=0, row=1, padx=5, pady=5)
        marcat = ttk.Entry(frame2)
        marcat.grid(column=1, row=1, padx=5, pady=5)
        stockl = ttk.Label(frame2, text='Stock:')
        stockl.grid(column=0, row=2, padx=5, pady=5)
        stockt = ttk.Entry(frame2)
        stockt.grid(column=1, row=2, padx=5, pady=5)
        preciol = ttk.Label(frame2, text='Precio:')
        preciol.grid(column=0, row=3, padx=5, pady=5)
        preciot = ttk.Entry(frame2)
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
        ingresar = ttk.Button(frame2, text='Ingresar', command=IngresarProducto)
        ingresar.grid(column=0, row=7, columnspan=2)
        root2.mainloop()

    elif colecb.get() == 'envio':
        envl = ttk.Label(frame2, text='Envio:')
        envl.grid(column=1, row=0, padx=5, pady=5)
        fechaenvl = ttk.Label(frame2, text='Fecha Envio:')
        fechaenvl.grid(column=0, row=1, padx=5, pady=5)
        fechaenvt = ttk.Entry(frame2)
        fechaenvt.grid(column=1, row=1, padx=5, pady=5)
        fechaentl = ttk.Label(frame2, text='Fecha Entrega:')
        fechaentl.grid(column=0, row=2, padx=5, pady=5)
        fechaentt = ttk.Entry(frame2)
        fechaentt.grid(column=1, row=2, padx=5, pady=5)
        proveedorl = ttk.Label(frame2, text='Proveedor:')
        proveedorl.grid(column=1, row=3, padx=5, pady=5)
        nombrel = ttk.Label(frame2, text='Nombre:')
        nombrel.grid(column=0, row=4, padx=5, pady=5)
        nombret = ttk.Entry(frame2)
        nombret.grid(column=1, row=4, padx=5, pady=5)
        apellidol = ttk.Label(frame2, text='Apellido:')
        apellidol.grid(column=0, row=5, padx=5, pady=5)
        apellidot = ttk.Entry(frame2)
        apellidot.grid(column=1, row=5, padx=5, pady=5)
        correol = ttk.Label(frame2, text='Correo:')
        correol.grid(column=0, row=6, padx=5, pady=5)
        correot = ttk.Entry(frame2)
        correot.grid(column=1, row=6, padx=5, pady=5)
        teléfonol = ttk.Label(frame2, text='Teléfono:')
        teléfonol.grid(column=0, row=7, padx=5, pady=5)
        teléfonot = ttk.Entry(frame2)
        teléfonot.grid(column=1, row=7, padx=5, pady=5)
        stockl = ttk.Label(frame2, text='Stock Enviado (separando por comas cada uno):')
        stockl.grid(column=0, row=8, padx=5, pady=5)
        prodl = ttk.Label(frame2, text='Nombres Productos:')
        prodl.grid(column=0, row=9, padx=5, pady=5)
        prodt = ttk.Entry(frame2)
        prodt.grid(column=1, row=9, columnspan=2, padx=10, pady=10)
        cantl = ttk.Label(frame2, text='Cantidades Enviadas:')
        cantl.grid(column=0, row=10, padx=5, pady=5)
        cantt = ttk.Entry(frame2)
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
        ingresar = ttk.Button(frame2, text='Ingresar', command=IngresarEnvio)
        ingresar.grid(column=0, row=11, columnspan=2)
        root2.mainloop()

    elif colecb.get() == 'factura':
        factural = ttk.Label(frame2, text='Factura:')
        factural.grid(column=1, row=0, padx=5, pady=5)
        preciototl = ttk.Label(frame2, text='Precio Total:')
        preciototl.grid(column=0, row=1, padx=5, pady=5)
        preciotott = ttk.Entry(frame2)
        preciotott.grid(column=1, row=1, padx=5, pady=5)
        fechal = ttk.Label(frame2, text='Fecha Factura:')
        fechal.grid(column=0, row=2, padx=5, pady=5)
        fechat = ttk.Entry(frame2)
        fechat.grid(column=1, row=2, padx=5, pady=5)
        empleadol = ttk.Label(frame2, text='Nombre Empleado:')
        empleadol.grid(column=0, row=3, padx=5, pady=5)
        empleadot = ttk.Entry(frame2)
        empleadot.grid(column=1, row=3, padx=5, pady=5)
        detallel = ttk.Label(frame2, text='Detalle (separar por comas cada uno):')
        detallel.grid(column=0, row=4, columnspan=2, padx=5, pady=5)
        productol = ttk.Label(frame2, text='Nombres Productos:')
        productol.grid(column=0, row=5, padx=5, pady=5)
        productot = ttk.Entry(frame2)
        productot.grid(column=1, row=5, padx=5, pady=5)
        cantidadl = ttk.Label(frame2, text='Cantidades Productos:')
        cantidadl.grid(column=0, row=6, padx=5, pady=5)
        cantidadt = ttk.Entry(frame2)
        cantidadt.grid(column=1, row=6, padx=5, pady=5)
        preciol = ttk.Label(frame2, text='Precios:')
        preciol.grid(column=0, row=7, padx=5, pady=5)
        preciot = ttk.Entry(frame2)
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
        ingresar = ttk.Button(frame2, text='Ingresar', command=IngresarFactura)
        ingresar.grid(column=0, row=8, columnspan=2)
        root2.mainloop()

Mostrar = ttk.Button(frame, text='Mostrar datos', command=Mostrar)
Mostrar.grid(column=1, row=1, padx=5, pady=5)
Insertar = ttk.Button(frame, text='Insertar datos', command=Ingresar)
Insertar.grid(column=2, row=1, padx=5, pady=5)
Actualizar = ttk.Button(frame, text='Actualizar datos')#, command=ActualizarDatos)
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

Eliminar = ttk. Button(frame, text='Eliminar datos', command=EliminarDatos)
Eliminar.grid(column=4, row=1)
root.mainloop()

root.mainloop()

def mostrar_menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Ingresar un documento")
        print("2. Ingresar varios documentos")
        print("3. Borrar documentos enteros")
        print("4. Modificar documentos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_documento()
        elif opcion == "2":
            ingresar_varios_documentos()
        elif opcion == "3":
            borrar_documentos()
        elif opcion == "4":
            modificar_documento()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")