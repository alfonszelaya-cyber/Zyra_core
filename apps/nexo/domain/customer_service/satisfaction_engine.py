class SatisfactionEngine:

    def calculate(
        self,
        scores: list[int],
    ) -> float:

        if not scores:
            return 0.0

        return round(
            sum(scores) / len(scores),
            2,
        )
