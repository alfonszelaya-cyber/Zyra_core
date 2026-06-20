# ============================================================
# MODULO 4 — MOTOR DE EVENTOS
# ============================================================

def motor_eventos():

    while True:

        clear()
        header()

        print("""

MOTOR DE EVENTOS

1. Venta
2. Compra
3. Importación
4. Exportación
5. Pago
6. Cobro
7. Ajuste / Cancelación
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

VENTAS

1. Nueva Venta
2. Facturación
3. Impuestos
4. Asiento Contable
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

COMPRAS

1. Nueva Compra
2. Proveedor
3. Impuestos
4. Asiento Contable
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

IMPORTACIONES

1. Proveedor Exterior
2. Aduana
3. Aranceles
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

EXPORTACIONES

1. Cliente Exterior
2. Logística
3. Costos
4. Impuestos
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

PAGOS

1. Proveedores
2. Nómina
3. Bancos
4. Cripto
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

COBROS

1. Clientes
2. Bancos
3. Cripto
4. Confirmaciones
5. Historial
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

AJUSTE / CANCELACIÓN

1. Ajuste Contable
2. Reversión
3. Corrección
4. Bitácora
5. Auditoría
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
# MODULO 4 — CONTABILIDAD AUTOMÁTICA
# ============================================================

def contabilidad_automatica():

    while True:

        clear()
        header()

        print("""

CONTABILIDAD AUTOMÁTICA

1. Asientos
2. Libros
3. Conciliaciones
4. Historial
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

ASIENTOS CONTABLES

1. Generar Asiento
2. Editar Asiento
3. Reversar Asiento
4. Validar Asiento
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

LIBROS CONTABLES

1. Libro Diario
2. Libro Mayor
3. Balance General
4. Estado de Resultados
5. Exportar
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

CONCILIACIONES

1. Bancaria
2. Caja
3. Cripto
4. Cuentas por Cobrar
5. Cuentas por Pagar
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

HISTORIAL CONTABLE

1. Asientos Generados
2. Modificaciones
3. Correcciones
4. Bitácora
5. Auditoría
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
# MODULO 4 — MOTOR FISCAL
# ============================================================

def motor_fiscal():

    while True:

        clear()
        header()

        print("""

MOTOR FISCAL

1. Reglas
2. Impuestos
3. Calendario
4. Simulación
5. Historial
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

REGLAS FISCALES

1. IVA
2. Renta
3. Retenciones
4. Percepciones
5. Configuración Fiscal
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

IMPUESTOS

1. IVA
2. ISR
3. Impuestos Municipales
4. Impuestos Especiales
5. Resumen Tributario
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

CALENDARIO FISCAL

1. Declaraciones
2. Pagos
3. Vencimientos
4. Alertas
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

SIMULACIÓN FISCAL

1. Simular IVA
2. Simular ISR
3. Simular Retenciones
4. Escenarios
5. Proyección Anual
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

HISTORIAL FISCAL

1. Declaraciones
2. Pagos
3. Correcciones
4. Fiscalizaciones
5. Bitácora Fiscal
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
# MODULO 4 — FACTURACIÓN
# ============================================================

def facturacion():

    while True:

        clear()
        header()

        print("""

FACTURACIÓN

1. Factura Venta
2. Factura Compra
3. Notas Crédito / Débito
4. Historial
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

FACTURA DE VENTA

1. Nueva Factura
2. Emitir DTE
3. Enviar Cliente
4. Imprimir
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

FACTURA DE COMPRA

1. Registrar
2. Validar
3. Adjuntar Documento
4. Contabilizar
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

NOTAS CRÉDITO / DÉBITO

1. Nueva Nota Crédito
2. Nueva Nota Débito
3. Correcciones
4. Anulaciones
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

HISTORIAL FACTURACIÓN

1. Ventas
2. Compras
3. Notas
4. Rechazadas
5. Auditoría
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
# MODULO 4 — ENTREGABLES OFICIALES
# ============================================================

def entregables_oficiales():

    while True:

        clear()
        header()

        print("""

ENTREGABLES OFICIALES

1. Gobierno
2. Bancos
3. Auditoría
4. Cliente
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

GOBIERNO

1. Declaraciones
2. Reportes Fiscales
3. DTE
4. Cumplimiento
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

BANCOS

1. Estados Financieros
2. Flujo de Caja
3. Referencias
4. Riesgo Financiero
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

AUDITORÍA EXTERNA

1. Estados Auditados
2. Evidencias
3. Reportes
4. Hallazgos
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

CLIENTE

1. Reportes
2. Estados Financieros
3. Facturación
4. Resúmenes
5. Historial
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
# MODULO 4 — FIRMAS
# ============================================================

def firmas():

    while True:

        clear()
        header()

        print("""

FIRMAS

1. ZYRA
2. Contador
3. Legal
4. Registro
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

FIRMA ZYRA

1. Validar Documento
2. Firmar Documento
3. Historial
4. Certificados
5. Auditoría
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

FIRMA CONTADOR

1. Balance General
2. Estado Resultados
3. Declaraciones
4. Reportes
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

FIRMA LEGAL

1. Contratos
2. Poderes
3. Validaciones
4. Certificaciones
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

REGISTRO

1. Registro Mercantil
2. Registro Fiscal
3. Licencias
4. Permisos
5. Historial
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
# MODULO 4 — CONTROL DE RIESGO
# ============================================================

def control_riesgo():

    while True:

        clear()
        header()

        print("""

CONTROL DE RIESGO

1. Fiscal
2. Contable
3. Liquidez
4. Bloqueos
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

RIESGO FISCAL

1. Declaraciones
2. Multas
3. Fiscalizaciones
4. Alertas
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

RIESGO CONTABLE

1. Asientos
2. Conciliaciones
3. Diferencias
4. Observaciones
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

RIESGO DE LIQUIDEZ

1. Flujo de Caja
2. Disponibilidad
3. Proyección
4. Alertas
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

BLOQUEOS

1. Operaciones
2. Cuentas
3. Clientes
4. Empresas
5. Historial
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
# MODULO 4 — AUDITORÍA
# ============================================================

def auditoria_financiera_core():

    while True:

        clear()
        header()

        print("""

AUDITORÍA

1. Interna
2. Externa
3. Fiscal
4. Historial
0. Volver

""")

        op = input("> ")

        if op == "1":

            while True:

                clear()
                header()

                print("""

AUDITORÍA INTERNA

1. Finanzas
2. Tesorería
3. Facturación
4. Riesgos
5. Hallazgos
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

AUDITORÍA EXTERNA

1. Evidencias
2. Reportes
3. Observaciones
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

AUDITORÍA FISCAL

1. IVA
2. ISR
3. Declaraciones
4. Fiscalizaciones
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

HISTORIAL DE AUDITORÍA

1. Interna
2. Externa
3. Fiscal
4. Bitácora
5. Evidencias
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
# MODULO 4 — PANEL FINANCIERO
# ============================================================

def panel_financiero():

    while True:

        clear()
        header()

        ingresos, egresos, utilidad = calcular_finanzas(SIM_LEDGER)
        estado = estado_contable(utilidad)

        print(f"""

PANEL FINANCIERO

Ingresos Totales : {ingresos}
Egresos Totales  : {egresos}
Utilidad Neta    : {utilidad}
Estado Contable  : {estado}

1. Dashboard
2. KPIs
3. Utilidad
4. Estado Contable
5. Alertas
0. Volver

""")

        op = input("> ")

        if op == "1":
            pausa("Dashboard")

        elif op == "2":
            pausa("KPIs")

        elif op == "3":
            pausa("Utilidad")

        elif op == "4":
            pausa("Estado Contable")

        elif op == "5":
            pausa("Alertas")

        elif op == "0":
            return

        else:
            pausa("Opción inválida")


# ============================================================
# MODULO 4 — FINANZAAS CORE (MENÚ PRINCIPAL)
# ============================================================

def modulo_4_finanzaas_condoble():

    while True:

        clear()
        header()

        print("""

1. Motor de Eventos
2. Contabilidad Automática
3. Motor Fiscal
4. Facturación
5. Tesorería
6. Cumplimiento Legal
7. Entregables Oficiales
8. Firmas
9. Control de Riesgo
10. Auditoría
11. Panel Financiero
0. Volver a ROOT

""")

        op = input("> ")

        if op == "1":
            motor_eventos()

        elif op == "2":
            contabilidad_automatica()

        elif op == "3":
            motor_fiscal()

        elif op == "4":
            facturacion()

        elif op == "5":
            tesoreria()

        elif op == "6":
            cumplimiento_legal()

        elif op == "7":
            entregables_oficiales()

        elif op == "8":
            firmas()

        elif op == "9":
            control_riesgo()

        elif op == "10":
            auditoria_financiera_core()

        elif op == "11":
            panel_financiero()

        elif op == "0":
            break

        else:
            pausa("Opción inválida")
