from apps.nexo.domain.risk.fraud_detection_engine import (
    FraudDetectionEngine,
)


class DetectFraudUseCase:

    def __init__(
        self,
        fraud_detection_engine: (
            FraudDetectionEngine
        ),
    ):
        self._fraud_detection_engine = (
            fraud_detection_engine
        )

    def execute(
        self,
        transaction_data: dict,
    ) -> dict:

        result = (
            self._fraud_detection_engine.detect(
                transaction_data=transaction_data,
            )
        )

        return {
            "fraud_analysis": result,
            "status": "ANALYZED",
        }
