from datetime import datetime


class CustomerFeedbackEngine:

    def register_feedback(
        self,
        client_id: str,
        score: int,
        comments: str,
    ) -> dict:

        return {
            "client_id": client_id,
            "score": score,
            "comments": comments,
            "created_at": datetime.utcnow(),
        }
