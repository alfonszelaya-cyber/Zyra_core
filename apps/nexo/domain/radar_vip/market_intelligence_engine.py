# ============================================================
# market_intelligence_engine.py
# NEXO / ZYRA
# Radar VIP Market Intelligence Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class MarketIntelligenceEngine:

    def __init__(self):

        self._market_events: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def register_market_signal(
        self,
        source: str,
        category: str,
        details: Dict,
    ) -> Dict:

        signal = {

            "signal_id":
                f"SIG-{uuid4()}",

            "source":
                source,

            "category":
                category,

            "details":
                details,

            "created_at":
                self._now(),

            "status":
                "ACTIVE",
        }

        self._market_events.append(
            signal
        )

        return signal

    def get_signals(self):

        return list(
            self._market_events
        )


market_intelligence_engine = (
    MarketIntelligenceEngine()
)
