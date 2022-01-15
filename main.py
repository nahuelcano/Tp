from concurso import Concurso
from disparo import Disparo
from participante import Participante

        

def dibujar_menu():
    print(
            f"""
                                 __
                               .'  '.
                          _.-'/  |   )
              ,        _.-"  ,|  /  0 `-.
              |\    .-"       `--""-.__.'========================-,
              \ '-'`        .___.--._)============================|
               \            .'      |          MENU               |
                |     /,_.-'        |  0  Agregar participante    |
              _/   _.'(             |  1  Mostrar registros       |
             /  ,-' \  \            |  2  Mostrar podio           |
             \  \    `-'            |  3  Mostrar ultimo          |
              `-'                   |  4  Cantidad participantes  |                                                                 
                                    |  5  Ordenar por edad        |   
                                    |  6  Promedio disparos       |
                                    |  7  Mejores disparos        |
                                    |  8  Guardar CSV             |
                                    |  9  Borrar CSV              |
                                    |  10 Guardar en DB           |
                                    |  11 Mostrar registros en DB |
                                    |  12 Mostrar ganador         |
                                    |  13 Salir                   |                                                                        
                                    '-----------------------------' 
        """
        )
    opcion = input("Ingrese una opcion: ")
    return opcion


def seleccionar_opciones(Concurso, opcion):
    """
    Recibe un objeto de concurso y una opcion
    Permite seleccionar distintas opciones con sus funcionalidades0
    """
    opciones = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","10", "11", "12"]
    while opcion != "13":
        try:
            if opcion == "0":
                nombre = input("Ingrese nombre del participante: ")
                apellido = input("Ingrese apellido del participante: ")
                edad = input("Ingrese la edad del participante: ")
                sexo = input("Ingrese sexo del participante [F/M]: ").upper()
                participante = Disparo(nombre, apellido, edad, sexo)
                participante.hacer_disparos() 
                Concurso.set_disparos(participante.armar_datos())
            elif opcion == "1":
                if len(Concurso.get_disparos()) == 0:
                    print(
                        f"""
                        ==============================================
                        ==        No se encontraron registros       ==
                        ==============================================
                        """
                    )
                else:
                    Concurso.mostrar_registros()
            elif opcion == "2":
                if len(Concurso.get_disparos()) < 3:
                    print(
                        f"""
                        ==============================================
                        ==   Se necesita al menos 3 participantes   ==
                        ==============================================
                        """
                    )
                else:
                    Concurso.mostrar_podio()
            elif opcion == "3":
                if len(Concurso.get_disparos()) < 3:
                    print(
                        f"""
                        ==============================================
                        ==   Se necesita al menos 2 participantes   ==
                        ==============================================
                        """
                    )
                else:
                    Concurso.mostrar_ultimo()
            elif opcion == "4":
                Concurso.cantidad_participantes()
            elif opcion == "5":
                if len(Concurso.get_disparos()) < 2:
                    print(
                        f"""
                        ==============================================
                        ==   Se necesita al menos 2 participantes   ==
                        ==============================================
                        """
                    )
                else:
                    Concurso.mostrar_ordenado_por_edad()
            elif opcion == "6":
                if len(Concurso.get_disparos()) < 1:
                    print(
                        f"""
                        ==============================================
                        ==   Se necesita al menos 1 participante    ==
                        ==============================================
                        """
                    )
                else:
                    Concurso.mostrar_promedio_disparo()
            elif opcion == "7":
                if len(Concurso.get_disparos()) < 1:
                    print(
                        f"""
                        ==============================================
                        ==   Se necesita al menos 1 participante    ==
                        ==============================================
                        """
                    )
                else:
                    Concurso.mostrar_mejores_disparos()
            elif opcion == "8":
                Concurso.guardar_CSV()
            elif opcion == "9":
                Concurso.borrar_CSV()
            elif opcion == "10":
                if len(Concurso.get_disparos()) < 1:
                    print(
                        f"""
                        ==============================================
                        ==   Se necesita al menos 1 participante    ==
                        ==============================================
                        """
                    )
                else:
                    Concurso.guardar_DB()
            elif opcion == "11":
                Concurso.consultar_todos_DB()
            elif opcion == "12":
                if len(Concurso.get_disparos()) < 3:
                        print(
                        f"""
                        ==============================================
                        ==   Se necesita al menos 3 participantes   ==
                        ==============================================
                        """
                    )
                else:
                    Concurso.mostrar_ganador()
            elif opcion not in opciones:
                print(
                        f"""
                        ===================================================
                        ==   Por favor seleccione una opcion correcta    ==
                        ===================================================
                        """
                    )
            
            
        except FileNotFoundError:
            print(
                f"""
                ==============================================
                ==       ERROR: Archivo no encontrado       ==
                ==============================================
                """
            )
        
        finally:
            opcion = dibujar_menu()
    else:
        print(
            """
            Hasta Luego.......
            """
        )   
    

def iniciar():
    """
    Inicia el programa
    Dibuja y contiene la lógica del menú
    """
    concurso_disparos = Concurso()
    opcion = dibujar_menu()
    seleccionar_opciones(concurso_disparos, opcion)
    
                

iniciar()