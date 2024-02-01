## Aplicacion desarrollada en Python con el IDE VSCode.

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### Este proyecto es una agenda de contactos sencilla la cual guarda el nombre y el numero de la persona.

### Dentro de las funciones que realiza la aplicacion son:

- Carga el archivo de texto (donde se guardaran los datos).
- Guarda el contacto.
- Edita el contacto.
- Busca el contacto.
- Elimina el contacto

### Diseño

1. Importacion de modulos.
   
   ![1](https://github.com/edSoto02/Agenda-Contactos/assets/106222946/1e295251-4b89-4f04-843c-1e15b8ee53a1)

   - Se importa el módulo os para realizar operaciones relaciondas con el sistema operativo, en este caso, se utiliza para verificar la existencia de n archivo.
2. Definicion de funciones.
   - cargar_agenda(). Lee el archivo y carga los contactos almacenado en un diccioario. Si el archivo no existe, devuelve un diccionario vacio.
    
     ![2](https://github.com/edSoto02/Agenda-Contactos/assets/106222946/56316bf5-b67d-4ff8-bf4a-66537c484abc)

   - guardar_contacto(agenda): Permite al usuario agregar un nuevo contacto al dicciionario.
  
     ![3](https://github.com/edSoto02/Agenda-Contactos/assets/106222946/4da8b9ac-a993-477c-8c6a-37702ab4edbb)


   - editar_contacto(agenda): Permite al usuario editar el numero de telefono de in contaxto existente en el diccionario.
  
     ![4](https://github.com/edSoto02/Agenda-Contactos/assets/106222946/aab1a0ae-3a30-4ed3-86e1-c319f8c56219)


   - buscar_contacto(agenda): Permite al usuairo buscar un contacto por su nombre en el diccionario y muestra su informacion si existe.

     ![5](https://github.com/edSoto02/Agenda-Contactos/assets/106222946/7c77beb5-5f47-450a-b1a2-7906d3e9861c)


   - eliminar_contacto(agenda): Permite al usuario eliminar un contacto existente en el diccionario.
  
     ![6](https://github.com/edSoto02/Agenda-Contactos/assets/106222946/a7c0c702-38f7-4e65-a3e8-d21234426036)


   - mostrar menu: Imprime en la consila las opciones disponibles en el menu.

     ![7](https://github.com/edSoto02/Agenda-Contactos/assets/106222946/a5696398-5872-4445-8688-1dd0031323ff)

3. Carga la agenda desde el archivo:
   - Se carga la agenda al inicio del programa.
4. Bucle principal:
   - Inicia un bucle infinito par mantener el programa en ejecucion hasta que el usuario decida salir.
5. Mostrar el menu y obtener la opcion del usuario:
   
      ![8](https://github.com/edSoto02/Agenda-Contactos/assets/106222946/eeb9158a-aa70-40c2-90b7-05d2c6f90bc5)

    
   - Imprime el menu en la consola y solicita al usuario que ingrese el numero de la opcion que desea realizar.
6. Manejar la opcion seleccionada:

      ![9](https://github.com/edSoto02/Agenda-Contactos/assets/106222946/e637b747-e330-4c36-a016-b2067310836e)


   - Se realiza la accion correspondiente segun la opcion ingresada por el usuario.
7. Mostrar la agenda:

    ![10](https://github.com/edSoto02/Agenda-Contactos/assets/106222946/58a5ef86-a6b9-4b56-ae6b-65a29193912a)

   - Imprime en la consola la lista de contactos alacenados en la agenda.
8. Salir de programa:

    ![11](https://github.com/edSoto02/Agenda-Contactos/assets/106222946/da533217-1eab-4a7e-8008-9d7906efae05)


   - Guarda la agenda en el archivo agenda.txt, impirme un mensaje de despedida y sale del bucle, finalizando el programa.
9. Manejar opciones no validas:

    ![12](https://github.com/edSoto02/Agenda-Contactos/assets/106222946/346a8de3-d14a-4033-bc25-abafba699bb3)

   - Si el usuario ingresa una opción que no está en el rango de opciones validas, se muestra un mensaje indicando que la opción no es válida.
  

## Ejecucion y compilacion:

![14](https://github.com/edSoto02/Agenda-Contactos/assets/106222946/a8bfad5e-437e-421c-86da-c2023db3e217)
![13](https://github.com/edSoto02/Agenda-Contactos/assets/106222946/a8c51785-d14d-4f3e-81ab-d0394b1fab8a)

