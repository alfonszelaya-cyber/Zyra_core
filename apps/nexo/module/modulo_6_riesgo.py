# ==================================================
# MÓDULO 6 - CONTROL DE RIESGOS (CORE CALLABLE)
# ==================================================

import os

# ===============================
# UI BASE
# ===============================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def header():
    print("============================================================")
    print("        ZYRA / NEXO - MÓDULO 6 CONTROL DE RIESGOS            ")
    print("============================================================")

def pausa(msg=""):
    if msg:
        print(f"\n{msg}")
    input("\n[ENTER] para continuar...")

# ===============================
# RIESGO FINANCIERO
# ===============================
def riesgo_financiero():
    while True:
        clear()
        header()

        print("--- Riesgo Financiero ---")
        print("1) Liquidez")
        print("2) Crédito")
        print("3) Mercado")
        print("4) Más Opciones")
        print("0) Volver")

        op = input(">> ").strip()

        if op == "1":
            pausa("Liquidez")

        elif op == "2":
            pausa("Crédito")

        elif op == "3":
            pausa("Mercado")

        elif op == "4":

            while True:

                clear()
                header()

                print("--- Más Opciones Financieras ---")
                print("1) Historial Financiero")
                print("2) Riesgo País")
                print("3) Riesgo Geopolítico Financiero")
                print("4) Impacto de Sanciones")
                print("5) Exposición Internacional")
                print("6) Riesgo Cambiario")
                print("0) Volver")

                sub = input(">> ").strip()

                if sub == "1":
                    pausa("Historial Financiero")

                elif sub == "2":
                    pausa("Riesgo País")

                elif sub == "3":
                    pausa("Riesgo Geopolítico Financiero")

                elif sub == "4":
                    pausa("Impacto de Sanciones")

                elif sub == "5":
                    pausa("Exposición Internacional")

                elif sub == "6":
                    pausa("Riesgo Cambiario")

                elif sub == "0":
                    break

                else:
                    pausa("Opción inválida")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


# ===============================
# RIESGO OPERATIVO
# ===============================
def riesgo_operativo():
    while True:
        clear()
        header()

        print("--- Riesgo Operativo ---")
        print("1) Procesos Críticos")
        print("2) Incidencias")
        print("3) Continuidad")
        print("4) Más Opciones")
        print("0) Volver")

        op = input(">> ").strip()

        if op == "1":
            pausa("Procesos Críticos")

        elif op == "2":
            pausa("Incidencias")

        elif op == "3":
            pausa("Continuidad")

        elif op == "4":

            while True:

                clear()
                header()

                print("--- Más Opciones Operativas ---")
                print("1) Dependencias")
                print("2) Conflictos Internacionales")
                print("3) Supply Chain")
                print("4) Trade Route Risk")
                print("5) Riesgo Tecnológico")
                print("6) Riesgo de Terceros")
                print("0) Volver")

                sub = input(">> ").strip()

                if sub == "1":
                    pausa("Dependencias")

                elif sub == "2":
                    pausa("Conflictos Internacionales")

                elif sub == "3":
                    pausa("Supply Chain")

                elif sub == "4":
                    pausa("Trade Route Risk")

                elif sub == "5":
                    pausa("Riesgo Tecnológico")

                elif sub == "6":
                    pausa("Riesgo de Terceros")

                elif sub == "0":
                    break

                else:
                    pausa("Opción inválida")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


# ===============================
# RIESGO LEGAL & FISCAL
# ===============================
def riesgo_legal():
    while True:

        clear()
        header()

        print("--- Riesgo Legal & Fiscal ---")
        print("1) Cumplimiento")
        print("2) Fiscal")
        print("3) Legal")
        print("4) Más Opciones")
        print("0) Volver")

        op = input(">> ").strip()

        if op == "1":
            pausa("Cumplimiento")

        elif op == "2":
            pausa("Fiscal")

        elif op == "3":
            pausa("Legal")

        elif op == "4":

            while True:

                clear()
                header()

                print("--- Más Opciones Legales ---")
                print("1) Sanciones Internacionales")
                print("2) OFAC")
                print("3) Restricciones Comerciales")
                print("4) Riesgo Regulatorio Global")
                print("5) Auditorías")
                print("6) Litigios")
                print("0) Volver")

                sub = input(">> ").strip()

                if sub == "1":
                    pausa("Sanciones Internacionales")

                elif sub == "2":
                    pausa("OFAC")

                elif sub == "3":
                    pausa("Restricciones Comerciales")

                elif sub == "4":
                    pausa("Riesgo Regulatorio Global")

                elif sub == "5":
                    pausa("Auditorías")

                elif sub == "6":
                    pausa("Litigios")

                elif sub == "0":
                    break

                else:
                    pausa("Opción inválida")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")
            # ===============================
# RIESGO LOGÍSTICO
# ===============================
def riesgo_logistico():
    while True:
        clear()
        header()

        print("--- Riesgo Logístico ---")
        print("1) Transporte")
        print("2) Aduanas")
        print("3) Puertos")
        print("4) Más Opciones")
        print("0) Volver")

        op = input(">> ").strip()

        if op == "1":
            pausa("Transporte")

        elif op == "2":
            pausa("Aduanas")

        elif op == "3":
            pausa("Puertos")

        elif op == "4":

            while True:

                clear()
                header()

                print("--- Más Opciones Logísticas ---")
                print("1) Supply Chain")
                print("2) Rutas Comerciales")
                print("3) Global Supply Alert")
                print("4) Trade Route Risk")
                print("5) Riesgo de Importación")
                print("6) Riesgo de Exportación")
                print("0) Volver")

                sub = input(">> ").strip()

                if sub == "1":
                    pausa("Supply Chain")

                elif sub == "2":
                    pausa("Rutas Comerciales")

                elif sub == "3":
                    pausa("Global Supply Alert")

                elif sub == "4":
                    pausa("Trade Route Risk")

                elif sub == "5":
                    pausa("Riesgo de Importación")

                elif sub == "6":
                    pausa("Riesgo de Exportación")

                elif sub == "0":
                    break

                else:
                    pausa("Opción inválida")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


# ===============================
# RIESGO REPUTACIONAL
# ===============================
def riesgo_reputacional():
    while True:

        clear()
        header()

        print("--- Riesgo Reputacional ---")
        print("1) Imagen Corporativa")
        print("2) Medios")
        print("3) Redes Sociales")
        print("4) Más Opciones")
        print("0) Volver")

        op = input(">> ").strip()

        if op == "1":
            pausa("Imagen Corporativa")

        elif op == "2":
            pausa("Medios")

        elif op == "3":
            pausa("Redes Sociales")

        elif op == "4":

            while True:

                clear()
                header()

                print("--- Más Opciones Reputacionales ---")
                print("1) Riesgo País")
                print("2) Conflictos")
                print("3) War Alert")
                print("4) Alertas Globales")
                print("5) Riesgo de Marca")
                print("6) Crisis de Comunicación")
                print("0) Volver")

                sub = input(">> ").strip()

                if sub == "1":
                    pausa("Riesgo País")

                elif sub == "2":
                    pausa("Conflictos")

                elif sub == "3":
                    pausa("War Alert")

                elif sub == "4":
                    pausa("Alertas Globales")

                elif sub == "5":
                    pausa("Riesgo de Marca")

                elif sub == "6":
                    pausa("Crisis de Comunicación")

                elif sub == "0":
                    break

                else:
                    pausa("Opción inválida")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


# ===============================
# ALERTAS & EVENTOS
# ===============================
def alertas_eventos():
    while True:

        clear()
        header()

        print("--- Alertas & Eventos ---")
        print("1) Eventos Geopolíticos")
        print("2) Eventos Comerciales")
        print("3) Eventos Críticos")
        print("4) Más Opciones")
        print("0) Volver")

        op = input(">> ").strip()

        if op == "1":
            pausa("Eventos Geopolíticos")

        elif op == "2":
            pausa("Eventos Comerciales")

        elif op == "3":
            pausa("Eventos Críticos")

        elif op == "4":

            while True:

                clear()
                header()

                print("--- Eventos Registrados ---")
                print("1) COUNTRY_RISK_CHANGED")
                print("2) SANCTION_DETECTED")
                print("3) WAR_ALERT")
                print("4) TRADE_ROUTE_RISK")
                print("5) GLOBAL_SUPPLY_ALERT")
                print("6) ALERTA_RIESGO")
                print("0) Volver")

                sub = input(">> ").strip()

                if sub == "1":
                    pausa("COUNTRY_RISK_CHANGED")

                elif sub == "2":
                    pausa("SANCTION_DETECTED")

                elif sub == "3":
                    pausa("WAR_ALERT")

                elif sub == "4":
                    pausa("TRADE_ROUTE_RISK")

                elif sub == "5":
                    pausa("GLOBAL_SUPPLY_ALERT")

                elif sub == "6":
                    pausa("ALERTA_RIESGO")

                elif sub == "0":
                    break

                else:
                    pausa("Opción inválida")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")
            # ===============================
# EVALUACIONES DE RIESGO
# ===============================
def evaluaciones_riesgo():
    while True:

        clear()
        header()

        print("--- Evaluaciones de Riesgo ---")
        print("1) Financiero")
        print("2) Operativo")
        print("3) Legal")
        print("4) Más Opciones")
        print("0) Volver")

        op = input(">> ").strip()

        if op == "1":
            pausa("Financiero")

        elif op == "2":
            pausa("Operativo")

        elif op == "3":
            pausa("Legal")

        elif op == "4":

            while True:

                clear()
                header()

                print("--- Más Evaluaciones ---")
                print("1) Logístico")
                print("2) Reputacional")
                print("3) Riesgo País")
                print("4) Riesgo Geopolítico")
                print("5) Supply Chain")
                print("6) Score General ZYRA")
                print("0) Volver")

                sub = input(">> ").strip()

                if sub == "1":
                    pausa("Logístico")

                elif sub == "2":
                    pausa("Reputacional")

                elif sub == "3":
                    pausa("Riesgo País")

                elif sub == "4":
                    pausa("Riesgo Geopolítico")

                elif sub == "5":
                    pausa("Supply Chain")

                elif sub == "6":
                    pausa("Score General ZYRA")

                elif sub == "0":
                    break

                else:
                    pausa("Opción inválida")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


# ===============================
# HISTORIAL DE INCIDENTES
# ===============================
def historial_incidentes():
    while True:

        clear()
        header()

        print("--- Historial de Incidentes ---")
        print("1) Financieros")
        print("2) Operativos")
        print("3) Legales")
        print("4) Más Opciones")
        print("0) Volver")

        op = input(">> ").strip()

        if op == "1":
            pausa("Incidentes Financieros")

        elif op == "2":
            pausa("Incidentes Operativos")

        elif op == "3":
            pausa("Incidentes Legales")

        elif op == "4":

            while True:

                clear()
                header()

                print("--- Más Incidentes ---")
                print("1) Logísticos")
                print("2) Reputacionales")
                print("3) Geopolíticos")
                print("4) Sanciones")
                print("5) Supply Chain")
                print("6) Auditoría")
                print("0) Volver")

                sub = input(">> ").strip()

                if sub == "1":
                    pausa("Logísticos")

                elif sub == "2":
                    pausa("Reputacionales")

                elif sub == "3":
                    pausa("Geopolíticos")

                elif sub == "4":
                    pausa("Sanciones")

                elif sub == "5":
                    pausa("Supply Chain")

                elif sub == "6":
                    pausa("Auditoría")

                elif sub == "0":
                    break

                else:
                    pausa("Opción inválida")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


# ===============================
# PANEL DE RIESGOS (KPIs)
# ===============================
def panel_kpis():
    while True:

        clear()
        header()

        print("--- Panel de Riesgos (KPIs) ---")
        print("1) Riesgo Financiero")
        print("2) Riesgo Operativo")
        print("3) Riesgo País")
        print("4) Más Opciones")
        print("0) Volver")

        op = input(">> ").strip()

        if op == "1":
            pausa("Riesgo Financiero")

        elif op == "2":
            pausa("Riesgo Operativo")

        elif op == "3":
            pausa("Riesgo País")

        elif op == "4":

            while True:

                clear()
                header()

                print("--- Más KPIs ---")
                print("1) Geopolítico")
                print("2) Sanciones")
                print("3) Conflictos")
                print("4) Supply Chain")
                print("5) Alertas Globales")
                print("6) Score General ZYRA")
                print("0) Volver")

                sub = input(">> ").strip()

                if sub == "1":
                    pausa("Geopolítico")

                elif sub == "2":
                    pausa("Sanciones")

                elif sub == "3":
                    pausa("Conflictos")

                elif sub == "4":
                    pausa("Supply Chain")

                elif sub == "5":
                    pausa("Alertas Globales")

                elif sub == "6":
                    pausa("Score General ZYRA")

                elif sub == "0":
                    break

                else:
                    pausa("Opción inválida")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")
