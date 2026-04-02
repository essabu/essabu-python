"""API client for managing document resources."""

from __future__ import annotations

from typing import Any, BinaryIO

from essabu.hr.api.base import BaseApi

_BASE_PATH = "/api/hr/documents"


class DocumentApi(BaseApi):
    """Document management operations.

    Base path: /api/hr/documents
    """

    def upload(
        self,
        employee_id: str,
        document_type: str,
        file: BinaryIO,
        filename: str = "upload",
    ) -> dict[str, Any]:
        """Upload a document for an employee."""
        return self._http.post_multipart(
            _BASE_PATH,
            files={"file": (filename, file, "application/octet-stream")},
            data={"employeeId": employee_id, "documentType": document_type},
        )

    def list_by_employee(self, employee_id: str) -> list[dict[str, Any]]:
        """List documents for a specific employee."""
        return self._http.get(f"{_BASE_PATH}?employeeId={employee_id}")

    def download(self, document_id: str) -> bytes:
        """Download a document."""
        return self._http.get_bytes(f"{_BASE_PATH}/{document_id}/download")

    def delete(self, document_id: str) -> None:
        """Delete a document."""
        self._http.delete(f"{_BASE_PATH}/{document_id}")

    def get_expiring(self, within_days: int) -> list[dict[str, Any]]:
        """Get documents expiring within a given number of days."""
        return self._http.get(f"{_BASE_PATH}/expiring?withinDays={within_days}")
