# ============================================================
# MODULO 5 — OPERACIONES & LOGÍSTICA
# ============================================================

import os

# ============================================================
# FUNCIONES DE APOYO
# ============================================================

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def header():
    print("============================================================")
    print("      ZYRA / NEXO - MODULO 5 OPERACIONES & LOGISTICA        ")
    print("============================================================")


def pausa(msg=""):
    if msg:
        print(f"\n{msg}")

    input("\n[ENTER] para continuar...")


# ============================================================
# OPERACIONES
# ============================================================

def operaciones():

    while True:

        clear()
        header()

        print("""

OPERACIONES

1. Órdenes Activas
2. Órdenes Completadas
3. Órdenes Canceladas
4. Historial
5. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

ÓRDENES ACTIVAS

1. Ver Órdenes
2. Asignaciones
3. Prioridades
4. Seguimiento
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

ÓRDENES COMPLETADAS

1. Ver Completadas
2. Evidencias
3. Entregas
4. Validaciones
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

ÓRDENES CANCELADAS

1. Ver Canceladas
2. Motivos
3. Reversión
4. Auditoría
5. Historial
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

HISTORIAL OPERATIVO

1. Operaciones
2. Cambios
3. Eventos
4. Bitácora
5. Auditoría
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

MÁS OPCIONES OPERACIONES

1. KPIs
2. Riesgos
3. Alertas
4. Productividad
5. Trazabilidad
6. Score ZYRA
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
# LOGÍSTICA
# ============================================================

def logistica():

    while True:

        clear()
        header()

        print("""

LOGÍSTICA

1. Terrestre
2. Marítimo
3. Aéreo
4. Proveedores
5. Costos
6. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

LOGÍSTICA TERRESTRE

1. Rutas
2. Vehículos
3. Conductores
4. Entregas
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

LOGÍSTICA MARÍTIMA

1. Navieras
2. Contenedores
3. Puertos
4. Tracking
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

LOGÍSTICA AÉREA

1. Aerolíneas
2. Carga
3. Tracking
4. Costos
5. Historial
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

PROVEEDORES LOGÍSTICOS

1. Registro
2. Evaluación
3. Contratos
4. Rendimiento
5. Historial
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

COSTOS LOGÍSTICOS

1. Transporte
2. Combustible
3. Peajes
4. Seguros
5. Resumen
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Módulo disponible.")

        elif op == "6":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES LOGÍSTICAS

1. KPIs
2. Riesgos
3. Alertas
4. Optimización
5. Supply Chain
6. Score ZYRA
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
# MODULO 5 — ADUANAS
# ============================================================

def aduanas():

    while True:

        clear()
        header()

        print("""

ADUANAS

1. Documentación
2. Despacho
3. Impuestos
4. Estados
5. Historial
6. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

DOCUMENTACIÓN ADUANERA

1. Facturas
2. Packing List
3. BL / AWB
4. Certificados
5. Expediente
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

DESPACHO ADUANERO

1. Iniciar Despacho
2. Validaciones
3. Observaciones
4. Liberaciones
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

IMPUESTOS ADUANEROS

1. Aranceles
2. IVA
3. Tasas
4. Cálculos
5. Historial
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

ESTADOS ADUANEROS

1. En Revisión
2. Observado
3. Liberado
4. Retenido
5. Historial
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

HISTORIAL ADUANERO

1. Importaciones
2. Exportaciones
3. Incidentes
4. Correcciones
5. Auditoría
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Módulo disponible.")

        elif op == "6":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES ADUANAS

1. Agentes Aduanales
2. Riesgo Aduanero
3. Alertas
4. Restricciones
5. Cumplimiento
6. Score ZYRA
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
# MODULO 5 — INVENTARIOS
# ============================================================

def inventarios():

    while True:

        clear()
        header()

        print("""

INVENTARIOS

1. Entradas
2. Salidas
3. Stock
4. Ubicaciones
5. Ajustes
6. Historial
7. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

ENTRADAS

1. Registrar Entrada
2. Recepción
3. Validación
4. Documentos
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

SALIDAS

1. Registrar Salida
2. Despacho
3. Transferencias
4. Validación
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

CONTROL DE STOCK

1. Stock Actual
2. Stock Mínimo
3. Stock Máximo
4. Disponibilidad
5. Historial
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

UBICACIONES

1. Bodegas
2. Estanterías
3. Zonas
4. Mapa de Ubicación
5. Historial
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

AJUSTES DE INVENTARIO

1. Corrección
2. Pérdidas
3. Daños
4. Reposición
5. Historial
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Módulo disponible.")

        elif op == "6":

            while True:

                clear()
                header()

                print("""

HISTORIAL INVENTARIO

1. Entradas
2. Salidas
3. Ajustes
4. Movimientos
5. Auditoría
0. Volver

""")

                sub = input("> ")

                if sub == "0":
                    break

                pausa("Módulo disponible.")

        elif op == "7":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES INVENTARIO

1. Rotación
2. Trazabilidad
3. Alertas
4. Vencimientos
5. Riesgos
6. Score ZYRA
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
# MODULO 5 — PROVEEDORES
# ============================================================

def proveedores():

    while True:

        clear()
        header()

        print("""

PROVEEDORES

1. Registro
2. Evaluación
3. Contratos
4. Historial
5. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

REGISTRO DE PROVEEDORES

1. Nuevo Proveedor
2. Actualizar Datos
3. Documentación
4. Validación
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

EVALUACIÓN DE PROVEEDORES

1. Rendimiento
2. Calidad
3. Tiempos de Entrega
4. Cumplimiento
5. Score
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

CONTRATOS

1. Nuevo Contrato
2. Renovaciones
3. Vencimientos
4. Condiciones
5. Historial
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

HISTORIAL DE PROVEEDORES

1. Operaciones
2. Evaluaciones
3. Contratos
4. Incidentes
5. Auditoría
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

MÁS OPCIONES PROVEEDORES

1. Riesgos
2. Alertas
3. Ranking
4. Certificaciones
5. Trazabilidad
6. Score ZYRA
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
# MODULO 5 — COSTOS OPERATIVOS
# ============================================================

def costos_operativos():

    while True:

        clear()
        header()

        print("""

COSTOS OPERATIVOS

1. Directos
2. Indirectos
3. Por Operación
4. Comparativos
5. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

COSTOS DIRECTOS

1. Mano de Obra
2. Transporte
3. Materiales
4. Servicios
5. Resumen
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

COSTOS INDIRECTOS

1. Administración
2. Infraestructura
3. Tecnología
4. Servicios Generales
5. Resumen
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

COSTOS POR OPERACIÓN

1. Importación
2. Exportación
3. Distribución
4. Producción
5. Resumen
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

COMPARATIVOS

1. Mensual
2. Trimestral
3. Anual
4. Proyecciones
5. Reportes
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

MÁS OPCIONES COSTOS

1. KPIs
2. Tendencias
3. Alertas
4. Optimización
5. Rentabilidad
6. Score ZYRA
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
# MODULO 5 — CUMPLIMIENTO OPERATIVO
# ============================================================

def cumplimiento_operativo():

    while True:

        clear()
        header()

        print("""

CUMPLIMIENTO OPERATIVO

1. Reglas
2. Restricciones
3. Validaciones
4. Alertas
5. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

REGLAS OPERATIVAS

1. Operaciones
2. Logística
3. Aduanas
4. Inventarios
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

RESTRICCIONES

1. Operativas
2. Legales
3. Logísticas
4. Comerciales
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

VALIDACIONES

1. Documentos
2. Procesos
3. Inventarios
4. Aduanas
5. Historial
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

ALERTAS

1. Riesgos
2. Incumplimientos
3. Retrasos
4. Observaciones
5. Historial
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

MÁS OPCIONES CUMPLIMIENTO

1. Auditoría
2. KPIs
3. Score Operativo
4. Evidencias
5. Bitácora
6. Score ZYRA
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
# MODULO 5 — INCIDENTES
# ============================================================

def incidentes():

    while True:

        clear()
        header()

        print("""

INCIDENTES

1. Reportar
2. Abiertos
3. Cerrados
4. Historial
5. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Reportar Incidente")

        elif op == "2":
            pausa("Incidentes Abiertos")

        elif op == "3":
            pausa("Incidentes Cerrados")

        elif op == "4":
            pausa("Historial de Incidentes")

        elif op == "5":

            while True:

                clear()
                header()

                print("""

MÁS OPCIONES INCIDENTES

1. Prioridades
2. Riesgos
3. Evidencias
4. Seguimiento
5. Auditoría
6. Score ZYRA
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
# MODULO 5 — PANEL OPERATIVO
# ============================================================

def panel_operativo():

    while True:

        clear()
        header()

        print("""

PANEL OPERATIVO

1. Estado General
2. Alertas
3. Cuellos de Botella
4. KPIs
5. Más Opciones
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

ESTADO GENERAL

1. Operaciones
2. Logística
3. Aduanas
4. Inventarios
5. Resumen Ejecutivo
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

ALERTAS OPERATIVAS

1. Riesgos
2. Retrasos
3. Incidentes
4. Cumplimiento
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

CUELLOS DE BOTELLA

1. Operaciones
2. Logística
3. Inventarios
4. Aduanas
5. Recomendaciones
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

KPIs OPERATIVOS

1. Eficiencia
2. Productividad
3. Tiempo de Entrega
4. Costos
5. Rentabilidad
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

MÁS OPCIONES PANEL OPERATIVO

1. Dashboard Ejecutivo
2. Score Operativo
3. Tendencias
4. Pronósticos
5. Auditoría
6. Score ZYRA
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
# MODULO 5 — MENÚ PRINCIPAL
# ============================================================

def modulo_5_logistica():

    while True:

        clear()
        header()

        print("""

ZYRA / NEXO CORE — OPERACIONES & LOGÍSTICA

1. Operaciones
2. Logística
3. Aduanas
4. Inventarios
5. Proveedores
6. Costos Operativos
7. Cumplimiento Operativo
8. Incidentes
9. Panel Operativo
0. Volver a ROOT

""")

        op = input("> ")

        if op == "1":
            operaciones()

        elif op == "2":
            logistica()

        elif op == "3":
            aduanas()

        elif op == "4":
            inventarios()

        elif op == "5":
            proveedores()

        elif op == "6":
            costos_operativos()

        elif op == "7":
            cumplimiento_operativo()

        elif op == "8":
            incidentes()

        elif op == "9":
            panel_operativo()

        elif op == "0":
            break

        else:
            pausa("Opción inválida")

# ============================================================
# FIN MÓDULO 5
# ============================================================

# FUNCIONES DEL MÓDULO:
#
# operaciones()
# logistica()
# aduanas()
# inventarios()
# proveedores()
# costos_operativos()
# cumplimiento_operativo()
# incidentes()
# panel_operativo()
# modulo_5_logistica()
#
# LLAMADA DESDE ROOT:
#
# elif op == "5":
#     modulo_5_logistica()
#
# ============================================================
