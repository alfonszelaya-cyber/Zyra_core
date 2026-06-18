class ClientSegmentationEngine:

    def segment(
        self,
        annual_volume: float,
    ) -> str:

        if annual_volume >= 1000000:
            return "ENTERPRISE"

        if annual_volume >= 100000:
            return "BUSINESS"

        return "STANDARD"
