"""Companies API module."""

from essabu.identity.api.base import CrudApi
from essabu.common.http_client import HttpClient
from essabu.identity.models.company import CompanyResponse


class CompaniesApi(CrudApi):
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http, "/companies", CompanyResponse)
