# ============================================================
# agro_adapter/mapper.py
# NEXO ↔ AGRO Data Mapper
# ============================================================

class AgroMapper:

    def map_company_to_producer(
        self,
        company: dict,
    ) -> dict:

        return {
            "producer_id": company.get("company_id"),
            "name": company.get("name"),
            "country": company.get("country"),
            "status": company.get("status", "ACTIVE"),
        }

    def map_invoice_to_agro(
        self,
        invoice: dict,
    ) -> dict:

        return {
            "invoice_id": invoice.get("invoice_id"),
            "client_id": invoice.get("client_id"),
            "amount": invoice.get("total"),
            "currency": invoice.get("currency", "USD"),
            "status": invoice.get("status"),
        }

    def map_inventory_to_agro(
        self,
        inventory: dict,
    ) -> dict:

        return {
            "product_id": inventory.get("product_id"),
            "name": inventory.get("name"),
            "quantity": inventory.get("quantity"),
            "unit": inventory.get("unit"),
        }
