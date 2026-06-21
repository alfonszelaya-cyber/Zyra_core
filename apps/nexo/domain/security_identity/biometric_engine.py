# ============================================================
# biometric_engine.py
# NEXO / ZYRA
# Biometric Identity Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4
import hashlib


class BiometricEngine:

    def __init__(self):

        self._registry = {}

    def register(
        self,
        identity_id: str,
        biometric_data: str,
        biometric_type: str,
    ) -> dict:

        biometric_hash = hashlib.sha256(
            biometric_data.encode()
        ).hexdigest()

        record = {

            "biometric_id":
                f"BIO-{uuid4()}",

            "identity_id":
                identity_id,

            "biometric_type":
                biometric_type,

            "biometric_hash":
                biometric_hash,

            "registered_at":
                datetime.utcnow().isoformat(),

            "status":
                "ACTIVE",
        }

        self._registry[
            identity_id
        ] = record

        return record

    def verify(
        self,
        identity_id: str,
        biometric_data: str,
    ) -> bool:

        if identity_id not in self._registry:
            return False

        biometric_hash = hashlib.sha256(
            biometric_data.encode()
        ).hexdigest()

        return (
            self._registry[
                identity_id
            ]["biometric_hash"]
            == biometric_hash
        )


biometric_engine = (
    BiometricEngine()
)
