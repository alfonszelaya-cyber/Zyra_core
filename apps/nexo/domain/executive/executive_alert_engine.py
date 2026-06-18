from datetime import datetime


class ExecutiveAlertEngine:

    def create_alert(
        self,
        level: str,
        title: str,
        description: str,
    ) -> dict:

        return {
            "level": level,
            "title": title,
            "description": description,
            "created_at": datetime.utcnow(),
            "status": "OPEN",
        }
