from apps.nexo.domain.government.document_submission_engine import (
    DocumentSubmissionEngine,
)


class SubmitGovernmentDocumentUseCase:

    def __init__(
        self,
        submission_engine: DocumentSubmissionEngine,
    ):
        self._submission_engine = submission_engine

    def execute(
        self,
        institution_id: str,
        document_id: str,
        document_type: str,
    ) -> dict:

        submission = (
            self._submission_engine.submit(
                institution_id=institution_id,
                document_id=document_id,
                document_type=document_type,
            )
        )

        return {
            "institution_id": institution_id,
            "document_id": document_id,
            "document_type": document_type,
            "submission": submission,
        }
