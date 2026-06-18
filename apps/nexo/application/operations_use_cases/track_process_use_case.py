from apps.nexo.domain.operations.process_tracking_engine import (
    ProcessTrackingEngine,
)


class TrackProcessUseCase:

    def __init__(
        self,
        process_tracking_engine: (
            ProcessTrackingEngine
        ),
    ):
        self._process_tracking_engine = (
            process_tracking_engine
        )

    def execute(
        self,
        process_id: str,
    ) -> dict:

        tracking = (
            self._process_tracking_engine.track_process(
                process_id=process_id,
            )
        )

        return {
            "process_id": process_id,
            "tracking": tracking,
            "status": tracking.get(
                "status",
                "UNKNOWN",
            ),
        }
