# ============================================================
# MODULO 1 : PANEL EJECUTIVO (CALLABLE DESDE MAIN)
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
# MODULO 1 : AUDITORIA EJECUTIVA
# ============================================================

def auditoria_ejecutiva():

    while True:

        clear()
        header()

        print("""

AUDITORIA EJECUTIVA

1. Auditoría Financiera
2. Auditoría Fiscal
3. Auditoría Operativa
4. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            auditoria_financiera()

        elif op == "2":
            auditoria_fiscal()

        elif op == "3":
            auditoria_operativa()

        elif op == "4":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES DE AUDITORÍA

1. Auditoría de Riesgos
2. Auditoría Logística
3. Auditoría Reputacional
4. Auditoría de Seguridad
5. Auditoría de Cumplimiento
6. Auditoría Integral ZYRA
0. Volver

""")

                sub = input("> ")

                if sub == "1":
                    auditoria_riesgos()

                elif sub == "2":
                    auditoria_logistica()

                elif sub == "3":
                    auditoria_reputacional()

                elif sub == "4":
                    auditoria_seguridad()

                elif sub == "5":
                    auditoria_cumplimiento()

                elif sub == "6":
                    auditoria_integral_zyra()

                elif sub == "0":
                    break

                else:
                    pausa("Opción inválida")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")

# ============================================================
# MODULO 1 : PANEL EJECUTIVO (ACTUALIZACIÓN MENÚ PRINCIPAL)
# ============================================================

def modulo_1_panel_ejecutivo():

    while True:

        clear()
        header()

        print("""

ZYRA / NEXO CORE — PANEL EJECUTIVO

1. Resumen General
2. Estado Financiero
3. Estado Fiscal
4. Alertas Globales
5. KPIs Ejecutivos
6. Decisiones Estratégicas
7. Auditoría Ejecutiva
0. Volver a ROOT

""")

        op = input("> ")

        if op == "1":

            menu_simple(
                "Resumen General",
                [
                    "Ingresos",
                    "Egresos",
                    "Utilidad",
                    "Operaciones Activas"
                ]
            )

        elif op == "2":

            menu_simple(
                "Estado Financiero",
                [
                    "Balance General",
                    "Resultados",
                    "Flujo de Caja"
                ]
            )

        elif op == "3":

            menu_simple(
                "Estado Fiscal",
                [
                    "Impuestos Pendientes",
                    "Declaraciones",
                    "Riesgos Fiscales"
                ]
            )

        elif op == "4":

            menu_simple(
                "Alertas Globales",
                [
                    "Riesgo Alto",
                    "Bloqueos",
                    "Incidentes Críticos"
                ]
            )

        elif op == "5":

            menu_simple(
                "KPIs Ejecutivos",
                [
                    "Rentabilidad",
                    "Liquidez",
                    "Rotación",
                    "Crecimiento"
                ]
            )

        elif op == "6":

            menu_simple(
                "Decisiones Estratégicas",
                [
                    "Aprobar",
                    "Revisar",
                    "Bloquear"
                ]
            )

        elif op == "7":

            auditoria_ejecutiva()

        elif op == "0":

            break

        else:

            pausa("Opción inválida")

# ============================================================
# MODULO 1 : AUDITORÍA EJECUTIVA (EXPANSIÓN NIVEL 2)
# ============================================================

def auditoria_financiera():

    while True:

        clear()
        header()

        print("""

AUDITORÍA FINANCIERA

1. Balance General
2. Estado de Resultados
3. Flujo de Caja
4. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Balance General")

        elif op == "2":
            pausa("Estado de Resultados")

        elif op == "3":
            pausa("Flujo de Caja")

        elif op == "4":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES FINANCIERAS

1. Liquidez
2. Endeudamiento
3. Rentabilidad
4. Tesorería
5. Presupuestos
6. Auditoría Integral
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


def auditoria_fiscal():

    while True:

        clear()
        header()

        print("""

AUDITORÍA FISCAL

1. Declaraciones
2. IVA
3. Renta
4. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Declaraciones")

        elif op == "2":
            pausa("IVA")

        elif op == "3":
            pausa("Renta")

        elif op == "4":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES FISCALES

1. Retenciones
2. DTE
3. Créditos Fiscales
4. Auditoría Tributaria
5. Fiscalizaciones
6. Riesgos Fiscales
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


def auditoria_operativa():

    while True:

        clear()
        header()

        print("""

AUDITORÍA OPERATIVA

1. Procesos
2. Producción
3. Calidad
4. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Procesos")

        elif op == "2":
            pausa("Producción")

        elif op == "3":
            pausa("Calidad")

        elif op == "4":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES OPERATIVAS

1. Eficiencia
2. Productividad
3. Trazabilidad
4. Inventarios
5. Control Interno
6. Auditoría Integral
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
# MODULO 1 : AUDITORÍAS AVANZADAS
# ============================================================

def auditoria_riesgos():

    while True:

        clear()
        header()

        print("""

AUDITORÍA DE RIESGOS

1. Riesgo Financiero
2. Riesgo Operativo
3. Riesgo Legal
4. Riesgo Reputacional
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Riesgo Financiero")

        elif op == "2":
            pausa("Riesgo Operativo")

        elif op == "3":
            pausa("Riesgo Legal")

        elif op == "4":
            pausa("Riesgo Reputacional")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


def auditoria_logistica():

    while True:

        clear()
        header()

        print("""

AUDITORÍA LOGÍSTICA

1. Transporte
2. Aduanas
3. Supply Chain
4. Inventarios
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Transporte")

        elif op == "2":
            pausa("Aduanas")

        elif op == "3":
            pausa("Supply Chain")

        elif op == "4":
            pausa("Inventarios")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


def auditoria_reputacional():

    while True:

        clear()
        header()

        print("""

AUDITORÍA REPUTACIONAL

1. Imagen Corporativa
2. Medios
3. Redes Sociales
4. Marca
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Imagen Corporativa")

        elif op == "2":
            pausa("Medios")

        elif op == "3":
            pausa("Redes Sociales")

        elif op == "4":
            pausa("Marca")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


def auditoria_seguridad():

    while True:

        clear()
        header()

        print("""

AUDITORÍA DE SEGURIDAD

1. Usuarios
2. Roles
3. Permisos
4. Eventos de Seguridad
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Usuarios")

        elif op == "2":
            pausa("Roles")

        elif op == "3":
            pausa("Permisos")

        elif op == "4":
            pausa("Eventos de Seguridad")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


def auditoria_cumplimiento():

    while True:

        clear()
        header()

        print("""

AUDITORÍA DE CUMPLIMIENTO

1. Políticas
2. Normativas
3. Regulaciones
4. Controles
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Políticas")

        elif op == "2":
            pausa("Normativas")

        elif op == "3":
            pausa("Regulaciones")

        elif op == "4":
            pausa("Controles")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


def auditoria_integral_zyra():

    while True:

        clear()
        header()

        print("""

AUDITORÍA INTEGRAL ZYRA

1. Finanzas
2. Fiscal
3. Operaciones
4. Riesgos
5. Seguridad
6. Cumplimiento
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Finanzas")

        elif op == "2":
            pausa("Fiscal")

        elif op == "3":
            pausa("Operaciones")

        elif op == "4":
            pausa("Riesgos")

        elif op == "5":
            pausa("Seguridad")

        elif op == "6":
            pausa("Cumplimiento")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")
