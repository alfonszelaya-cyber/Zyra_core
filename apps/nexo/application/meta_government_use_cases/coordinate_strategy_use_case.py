from apps.nexo.domain.meta_government.strategy_engine import (
    StrategyEngine,
)


class CoordinateStrategyUseCase:

    def __init__(
        self,
        strategy_engine: StrategyEngine,
    ):
        self._strategy_engine = strategy_engine

    def execute(
        self,
        strategy_id: str,
        entities: list,
    ) -> dict:

        strategy = self._strategy_engine.coordinate(
            strategy_id=strategy_id,
            entities=entities,
        )

        return {
            "strategy_id": strategy_id,
            "entities": entities,
            "strategy": strategy,
            "status": "ACTIVE",
        }
