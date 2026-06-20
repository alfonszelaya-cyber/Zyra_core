# ============================================================
# MODULO 2 — INSCRIPCIONES (CLIENTES & EMPRESAS)
# ============================================================

import os

# ============================================================
# FUNCIONES DE APOYO
# ============================================================

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def header():
    print("============================================================")
    print("                ZYRA / NEXO CORE SYSTEM                     ")
    print("============================================================")


def pausa(titulo=""):
    if titulo:
        print(f"\n{titulo}")

    input("\n[ENTER] para continuar...")


def menu_simple(titulo, opciones):

    while True:

        clear()
        header()

        print(f"{titulo}\n")

        for i, op in enumerate(opciones, 1):
            print(f"{i}. {op}")

        print("0. Volver")

        o = input("> ")

        if o == "0":
            break

        try:

            idx = int(o) - 1

            if 0 <= idx < len(opciones):
                pausa(f"Accediendo a: {opciones[idx]}")

            else:
                pausa("Opción no válida.")

        except:
            pausa("Entrada no válida.")


# ============================================================
# CLIENTES
# ============================================================

def clientes():

    while True:

        clear()
        header()

        print("""

CLIENTES

1. Alta Cliente
2. Editar Cliente
3. Cambiar Estado
4. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Alta Cliente")

        elif op == "2":
            pausa("Editar Cliente")

        elif op == "3":
            pausa("Cambiar Estado")

        elif op == "4":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES CLIENTES

1. Validación KYC
2. Documentos
3. Historial
4. Riesgo
5. Auditoría
6. Perfil Completo
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Información disponible.")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


# ============================================================
# EMPRESAS
# ============================================================

def empresas():

    while True:

        clear()
        header()

        print("""

EMPRESAS

1. Alta Empresa
2. Editar Empresa
3. Cambiar Estado
4. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Alta Empresa")

        elif op == "2":
            pausa("Editar Empresa")

        elif op == "3":
            pausa("Cambiar Estado")

        elif op == "4":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES EMPRESAS

1. Representantes
2. Accionistas
3. Documentación
4. Riesgo Empresarial
5. Auditoría
6. Perfil Completo
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Información disponible.")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")

# ============================================================
# PERFILES
# ============================================================

def perfiles():

    while True:

        clear()
        header()

        print("""

PERFILES

1. Asignar Rol
2. Cambiar Rol
3. Permisos
4. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Asignar Rol")

        elif op == "2":
            pausa("Cambiar Rol")

        elif op == "3":
            pausa("Permisos")

        elif op == "4":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES DE PERFILES

1. Historial de Roles
2. Roles Especiales
3. Roles Temporales
4. Jerarquías
5. Accesos
6. Auditoría de Perfil
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Información disponible.")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


# ============================================================
# ESTADO Y RIESGO
# ============================================================

def estado_riesgo():

    while True:

        clear()
        header()

        print("""

ESTADO Y RIESGO

1. Activo
2. Pendiente
3. Bloqueado
4. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Activo")

        elif op == "2":
            pausa("Pendiente")

        elif op == "3":
            pausa("Bloqueado")

        elif op == "4":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES DE RIESGO

1. Riesgo Bajo
2. Riesgo Medio
3. Riesgo Alto
4. Lista de Observación
5. Alertas
6. Score ZYRA
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Información disponible.")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")

# ============================================================
# HISTORIAL
# ============================================================

def historial_inscripciones():

    while True:

        clear()
        header()

        print("""

HISTORIAL

1. Operaciones
2. Alertas
3. Auditoría
4. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Operaciones")

        elif op == "2":
            pausa("Alertas")

        elif op == "3":
            pausa("Auditoría")

        elif op == "4":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES DE HISTORIAL

1. Cambios de Estado
2. Cambios de Perfil
3. Riesgos Detectados
4. Eventos
5. Bitácora
6. Trazabilidad Completa
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Información disponible.")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


# ============================================================
# MÓDULO 2 — INSCRIPCIONES (MENÚ PRINCIPAL)
# ============================================================

def modulo_2_inscripciones():

    while True:

        clear()
        header()

        print("""

ZYRA / NEXO CORE — INSCRIPCIONES

1. Clientes
2. Empresas
3. Perfiles
4. Estado / Riesgo
5. Historial
0. Volver a ROOT

""")

        op = input("> ")

        if op == "1":

            clientes()

        elif op == "2":

            empresas()

        elif op == "3":

            perfiles()

        elif op == "4":

            estado_riesgo()

        elif op == "5":

            historial_inscripciones()

        elif op == "0":

            break

        else:

            pausa("Opción inválida")


# ============================================================
# FIN MÓDULO 2
# ============================================================
