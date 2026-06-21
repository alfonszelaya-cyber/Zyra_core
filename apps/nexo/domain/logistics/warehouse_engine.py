# ============================================================
# warehouse_engine.py
# NEXO / ZYRA
# Warehouse Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class WarehouseEngine:

    def __init__(self):

        self._warehouses: List[dict] = []

        self._inventory: List[dict] = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    # ========================================================
    # ALMACENES
    # ========================================================

    def create_warehouse(
        self,
        name: str,
        location: str,
        capacity: float,
    ) -> Dict:

        warehouse = {

            "warehouse_id":
                f"WH-{uuid4()}",

            "name":
                name,

            "location":
                location,

            "capacity":
                capacity,

            "created_at":
                self._now(),

            "status":
                "ACTIVE",
        }

        self._warehouses.append(
            warehouse
        )

        return warehouse

    def get_warehouses(
        self,
    ):

        return list(
            self._warehouses
        )

    # ========================================================
    # INVENTARIO
    # ========================================================

    def add_inventory(
        self,
        warehouse_id: str,
        product_id: str,
        quantity: float,
    ) -> Dict:

        item = {

            "inventory_id":
                f"INV-{uuid4()}",

            "warehouse_id":
                warehouse_id,

            "product_id":
                product_id,

            "quantity":
                quantity,

            "created_at":
                self._now(),

            "status":
                "AVAILABLE",
        }

        self._inventory.append(
            item
        )

        return item

    def update_inventory(
        self,
        inventory_id: str,
        quantity: float,
    ) -> Optional[Dict]:

        for item in self._inventory:

            if (
                item["inventory_id"]
                == inventory_id
            ):

                item["quantity"] = quantity

                item["updated_at"] = (
                    self._now()
                )

                return item

        return None

    def get_inventory(
        self,
        warehouse_id: str = None,
    ):

        if warehouse_id:

            return [

                item

                for item
                in self._inventory

                if (
                    item["warehouse_id"]
                    == warehouse_id
                )
            ]

        return list(
            self._inventory
        )

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def get_summary(
        self,
    ):

        return {

            "warehouses":
                len(
                    self._warehouses
                ),

            "inventory_items":
                len(
                    self._inventory
                ),

            "generated_at":
                self._now(),
        }


warehouse_engine = (
    WarehouseEngine()
)

# ============================================================
# FIN
# warehouse_engine.py
# ============================================================
