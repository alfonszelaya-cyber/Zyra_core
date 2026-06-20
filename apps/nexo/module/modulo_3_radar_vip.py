# ============================================================
# MODULO 3 : RADAR VIP
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


# ============================================================
# IMPORTACIONES
# ============================================================

def radar_importaciones():

    while True:

        clear()
        header()

        print("""

IMPORTACIONES

1. Fuentes
2. Análisis
3. Costos
4. Rentabilidad
5. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Fuentes")

        elif op == "2":
            pausa("Análisis")

        elif op == "3":
            pausa("Costos")

        elif op == "4":
            pausa("Rentabilidad")

        elif op == "5":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES IMPORTACIONES

1. Proveedores
2. Aduanas
3. Aranceles
4. Riesgo País
5. Logística
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
# EXPORTACIONES
# ============================================================

def radar_exportaciones():

    while True:

        clear()
        header()

        print("""

EXPORTACIONES

1. Mercados
2. Costos
3. Logística
4. Rentabilidad
5. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Mercados")

        elif op == "2":
            pausa("Costos")

        elif op == "3":
            pausa("Logística")

        elif op == "4":
            pausa("Rentabilidad")

        elif op == "5":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES EXPORTACIONES

1. Destinos
2. Regulaciones
3. Riesgo Comercial
4. Competencia
5. Supply Chain
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
# COMERCIO
# ============================================================

def radar_comercio():

    while True:

        clear()
        header()

        print("""

COMERCIO

1. Compras
2. Ventas
3. Margen
4. Riesgo
5. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Compras")

        elif op == "2":
            pausa("Ventas")

        elif op == "3":
            pausa("Margen")

        elif op == "4":
            pausa("Riesgo")

        elif op == "5":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES COMERCIO

1. Tendencias
2. Competencia
3. Proveedores
4. Clientes
5. Oportunidades
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
# BIENES RAÍCES
# ============================================================

def radar_bienes_raices():

    while True:

        clear()
        header()

        print("""

BIENES RAÍCES

1. Adquisición
2. Costos
3. Retorno
4. Riesgos
5. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Adquisición")

        elif op == "2":
            pausa("Costos")

        elif op == "3":
            pausa("Retorno")

        elif op == "4":
            pausa("Riesgos")

        elif op == "5":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES BIENES RAÍCES

1. Avalúos
2. Mercado
3. Financiamiento
4. Rentabilidad
5. Riesgo Jurídico
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
# PANEL RADAR
# ============================================================

def panel_radar():

    while True:

        clear()
        header()

        print("""

PANEL RADAR

1. Alertas
2. Recomendaciones ZYRA
3. Historial
4. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Alertas")

        elif op == "2":
            pausa("Recomendaciones ZYRA")

        elif op == "3":
            pausa("Historial")

        elif op == "4":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES PANEL RADAR

1. Oportunidades Detectadas
2. Riesgos Detectados
3. Ranking de Negocios
4. Alertas VIP
5. Seguimiento
6. Score General ZYRA
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
# MODULO 3 : RADAR VIP (MENÚ PRINCIPAL)
# ============================================================

def modulo_3_radar_vip():

    while True:

        clear()
        header()

        print("""

ZYRA / NEXO CORE — RADAR VIP

1. Importaciones
2. Exportaciones
3. Comercio
4. Bienes Raíces
5. Panel Radar
0. Volver a ROOT

""")

        op = input("> ")

        if op == "1":

            radar_importaciones()

        elif op == "2":

            radar_exportaciones()

        elif op == "3":

            radar_comercio()

        elif op == "4":

            radar_bienes_raices()

        elif op == "5":

            panel_radar()

        elif op == "0":

            break

        else:

            pausa("Opción inválida")


# ============================================================
# FIN MÓDULO 3
# ============================================================
