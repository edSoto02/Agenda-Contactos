import os

def cargar_agenda():
    agenda = {}
    if os.path.exists("agenda.txt"):
        with open("agenda.txt", "r") as file:
            for line in file:
                nombre, telefono = line.strip().split(",")
                agenda[nombre] = telefono
    return agenda

def guardar_agenda(agenda):
    with open("agenda.txt", "w") as file:
        for nombre, telefono in agenda.items():
            file.write(f"{nombre},{telefono}\n")

def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado correctamente.")

def editar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea editar: ")
    if nombre in agenda:
        nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
        agenda[nombre] = nuevo_telefono
        print(f"Contacto {nombre} editado correctamente.")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado correctamente.")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")

def mostrar_menu():
    print("1. Agregar contacto")
    print("2. Editar contacto")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar agenda")
    print("0. Salir")

agenda = cargar_agenda()

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción que desea realizar: ")

    if opcion == "1":
        agregar_contacto(agenda)
    elif opcion == "2":
        editar_contacto(agenda)
    elif opcion == "3":
        buscar_contacto(agenda)
    elif opcion == "4":
        eliminar_contacto(agenda)
    elif opcion == "5":
        print("Agenda:")
        for nombre, telefono in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    elif opcion == "0":
        guardar_agenda(agenda)
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")
