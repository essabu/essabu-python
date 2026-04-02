"""Tests for the exception hierarchy."""

from __future__ import annotations

from essabu.common.exceptions import (
    AuthenticationError,
    AuthorizationError,
    ConflictError,
    EssabuError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)


class TestExceptions:
    def test_base_error(self):
        err = EssabuError("something went wrong", status_code=400)
        assert str(err) == "something went wrong"
        assert err.message == "something went wrong"
        assert err.status_code == 400
        assert err.body == {}

    def test_authentication_error(self):
        err = AuthenticationError()
        assert err.status_code == 401
        assert isinstance(err, EssabuError)

    def test_authorization_error(self):
        err = AuthorizationError()
        assert err.status_code == 403

    def test_not_found_error(self):
        err = NotFoundError("Employee not found")
        assert err.status_code == 404
        assert err.message == "Employee not found"

    def test_validation_error(self):
        errors = [{"field": "email", "message": "required"}]
        err = ValidationError(errors=errors)
        assert err.status_code == 422
        assert err.errors == errors

    def test_conflict_error(self):
        err = ConflictError()
        assert err.status_code == 409

    def test_rate_limit_error(self):
        err = RateLimitError(retry_after=30.0)
        assert err.status_code == 429
        assert err.retry_after == 30.0

    def test_server_error(self):
        err = ServerError(status_code=503)
        assert err.status_code == 503

    def test_error_repr(self):
        err = NotFoundError("not found")
        assert "NotFoundError" in repr(err)
        assert "404" in repr(err)
