# ============================================================
# MÓDULO 002 — FAMILY OFFICE
# NEXO / ZYRA CORE
# Estructura Oficial Congelada
# ============================================================

import os

# ============================================================
# UTILIDADES
# ============================================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def header():
    print("=" * 70)
    print("                 NEXO / ZYRA CORE")
    print("                 MÓDULO 002")
    print("                  FAMILY OFFICE")
    print("=" * 70)

def pausa(msg=""):
    if msg:
        print(f"\n{msg}")
    input("\n[ENTER] para continuar...")

def submenu(titulo, opciones):

    while True:

        clear()
        header()

        print(f"\n{titulo}\n")

        for i, item in enumerate(opciones, start=1):
            print(f"{i}. {item}")

        print("\n0. Volver")

        op = input("\n> ")

        if op == "0":
            break

        try:
            idx = int(op) - 1

            if 0 <= idx < len(opciones):
                pausa(f"Accediendo a: {opciones[idx]}")
            else:
                pausa("Opción inválida")

        except:
            pausa("Entrada inválida")

# ============================================================
# MÓDULO 002
# ============================================================

def modulo_002_family_office():

    while True:

        clear()
        header()

        print("""

1. Dashboard Patrimonial

2. Patrimonio Mundial

3. Bienes Raíces

4. Empresas

5. Tierras Agrícolas

6. Arte

7. Metales

8. Coleccionables

9. Vehículos

10. Trusts

11. Herencias

12. Gobierno Familiar

0. Volver a ROOT

""")

        op = input("> ")

        # ====================================================
        # DASHBOARD
        # ====================================================

        if op == "1":

            pausa("Dashboard Patrimonial")

        # ====================================================
        # PATRIMONIO MUNDIAL
        # ====================================================

        elif op == "2":

            submenu(
                "Patrimonio Mundial",
                [
                    "Sitios Históricos",
                    "Patrimonio Cultural",
                    "Patrimonio Natural",
                    "Patrimonio Digital",
                    "Revalorización"
                ]
            )

        # ====================================================
        # BIENES RAÍCES
        # ====================================================

        elif op == "3":

            submenu(
                "Bienes Raíces",
                [
                    "Residencial",
                    "Comercial",
                    "Industrial",
                    "Hotelería",
                    "Desarrollo"
                ]
            )

        # ====================================================
        # EMPRESAS
        # ====================================================

        elif op == "4":

            submenu(
                "Empresas",
                [
                    "Participaciones",
                    "Holdings",
                    "Subsidiarias",
                    "Acciones",
                    "Valoración"
                ]
            )

        # ====================================================
        # TIERRAS AGRÍCOLAS
        # ====================================================

        elif op == "5":

            submenu(
                "Tierras Agrícolas",
                [
                    "Producción",
                    "Ganadería",
                    "Forestal",
                    "Recursos Hídricos",
                    "Rendimiento"
                ]
            )

        # ====================================================
        # ARTE
        # ====================================================

        elif op == "6":

            submenu(
                "Arte",
                [
                    "Pintura",
                    "Escultura",
                    "Colecciones",
                    "Certificados",
                    "Valoración"
                ]
            )

        # ====================================================
        # METALES
        # ====================================================

        elif op == "7":

            submenu(
                "Metales",
                [
                    "Oro",
                    "Plata",
                    "Platino",
                    "Paladio",
                    "Reservas"
                ]
            )

        # ====================================================
        # COLECCIONABLES
        # ====================================================

        elif op == "8":

            submenu(
                "Coleccionables",
                [
                    "Monedas",
                    "Billetes",
                    "Trading Cards",
                    "Memorabilia",
                    "Subastas"
                ]
            )

        # ====================================================
        # VEHÍCULOS
        # ====================================================

        elif op == "9":

            submenu(
                "Vehículos",
                [
                    "Clásicos",
                    "Lujo",
                    "Flotas",
                    "Especiales",
                    "Valoración"
                ]
            )

        # ====================================================
        # TRUSTS
        # ====================================================

        elif op == "10":

            submenu(
                "Trusts",
                [
                    "Nacionales",
                    "Internacionales",
                    "Beneficiarios",
                    "Distribuciones",
                    "Protección Patrimonial"
                ]
            )

        # ====================================================
        # HERENCIAS
        # ====================================================

        elif op == "11":

            submenu(
                "Herencias",
                [
                    "Planificación",
                    "Ejecución",
                    "Beneficiarios",
                    "Sucesión",
                    "Auditoría"
                ]
            )

        # ====================================================
        # GOBIERNO FAMILIAR
        # ====================================================

        elif op == "12":

            submenu(
                "Gobierno Familiar",
                [
                    "Miembros",
                    "Protocolos",
                    "Decisiones",
                    "Riesgos",
                    "Continuidad Generacional"
                ]
            )

        # ====================================================
        # SALIR
        # ====================================================

        elif op == "0":
            break

        else:
            pausa("Opción inválida")
