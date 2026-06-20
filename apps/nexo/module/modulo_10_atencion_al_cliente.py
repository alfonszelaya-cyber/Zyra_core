# ============================================================
# MODULO 10 — ESCALAMIENTO GLOBAL
# ============================================================

def escalar_soporte_global():

    while True:

        clear()
        header()

        print("""

ESCALAMIENTO GLOBAL

1. Detectar Caso Transversal
2. Crear Ticket Global
3. Transferir Evidencia
4. Seguimiento de Escalamiento
5. Historial de Escalamientos
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

DETECTAR CASO TRANSVERSAL

1. NEXO + AXIS
2. NEXO + SEMILLA
3. NEXO + AGRO
4. NEXO + SUBASTAS
5. Ecosistema Completo
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Módulo disponible.")

        elif op == "2":

            while True:

                clear()
                header()

                print("""

CREAR TICKET GLOBAL

1. Ticket Operativo
2. Ticket Financiero
3. Ticket Fiscal
4. Ticket Tecnológico
5. Ticket Estratégico
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Módulo disponible.")

        elif op == "3":

            while True:

                clear()
                header()

                print("""

TRANSFERIR EVIDENCIA

1. Documentos
2. Logs
3. Auditorías
4. Evidencias Operativas
5. Evidencias Financieras
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Módulo disponible.")

        elif op == "4":

            while True:

                clear()
                header()

                print("""

SEGUIMIENTO DE ESCALAMIENTO

1. Casos Abiertos
2. Casos en Proceso
3. Casos Prioritarios
4. Casos Críticos
5. Estado General
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Módulo disponible.")

        elif op == "5":

            while True:

                clear()
                header()

                print("""

HISTORIAL DE ESCALAMIENTOS

1. Operativos
2. Financieros
3. Fiscales
4. Tecnológicos
5. Estratégicos
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Módulo disponible.")

        elif op == "0":

            return

        else:

            pausa("Opción inválida")

# ============================================================
# MODULO 10 — ATENCIÓN HUMANA NEXO
# ============================================================

def atencion_humana():

    while True:

        clear()
        header()

        print("""

ATENCIÓN HUMANA NEXO

1. Asignación de Agente NEXO
2. Intervención Especializada NEXO
3. Resolución Manual NEXO
4. Validación Final NEXO
5. Escalar a Soporte Global
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

ASIGNACIÓN DE AGENTE NEXO

1. Agente Operativo
2. Agente Financiero
3. Agente Fiscal
4. Agente Técnico
5. Historial
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Módulo disponible.")

        elif op == "2":

            while True:

                clear()
                header()

                print("""

INTERVENCIÓN ESPECIALIZADA NEXO

1. Operaciones
2. Finanzas
3. Fiscal
4. Tecnología
5. Historial
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Módulo disponible.")

        elif op == "3":

            while True:

                clear()
                header()

                print("""

RESOLUCIÓN MANUAL NEXO

1. Corrección Operativa
2. Corrección Financiera
3. Corrección Fiscal
4. Corrección Técnica
5. Evidencias
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Módulo disponible.")

        elif op == "4":

            while True:

                clear()
                header()

                print("""

VALIDACIÓN FINAL NEXO

1. Validar Resolución
2. Validar Evidencias
3. Confirmar Cliente
4. Cerrar Caso
5. Historial
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Módulo disponible.")

        elif op == "5":

            escalar_soporte_global()

        elif op == "0":

            return

        else:

            pausa("Opción inválida")

# ============================================================
# MODULO 10 — MENÚ PRINCIPAL
# ============================================================

def modulo_10_atencion_al_cliente():

    while True:

        clear()
        header()

        print("""

ZYRA / NEXO CORE — ATENCIÓN AL CLIENTE & SOPORTE

1. Entrada de Soporte
2. Atención Automatizada ZYRA
3. Asesoría Operativa
4. Incidencias Financieras
5. Incidencias Operativas
6. Atención Humana NEXO
7. Seguimiento de Casos
8. Alertas & SLA
9. Escalamiento Global
10. Cierre del Caso
11. Aprendizaje ZYRA
0. Volver a ROOT

""")

        op = input("> ")

        if op == "1":

            entrada_soporte()

        elif op == "2":

            atencion_automatica()

        elif op == "3":

            asesoria_operativa()

        elif op == "4":

            incidencias_financieras()

        elif op == "5":

            incidencias_operativas()

        elif op == "6":

            atencion_humana()

        elif op == "7":

            seguimiento_casos()

        elif op == "8":

            alertas_sla()

        elif op == "9":

            escalar_soporte_global()

        elif op == "10":

            cierre_caso()

        elif op == "11":

            aprendizaje_zyra()

        elif op == "0":

            break

        else:

            pausa("Opción inválida")

# ============================================================
# FIN MÓDULO 10
# ============================================================

# FUNCIONES DEL MÓDULO:
#
# entrada_soporte()
# atencion_automatica()
# asesoria_operativa()
# incidencias_financieras()
# incidencias_operativas()
# atencion_humana()
# seguimiento_casos()
# alertas_sla()
# escalar_soporte_global()
# cierre_caso()
# aprendizaje_zyra()
# modulo_10_atencion_al_cliente()
#
# LLAMADA DESDE ROOT:
#
# elif op == "10":
#     modulo_10_atencion_al_cliente()
#
# ============================================================
