"""Tests for common models."""

from __future__ import annotations

from essabu.common.models import PageRequest, PageResponse


class TestPageRequest:
    def test_defaults(self):
        pr = PageRequest()
        assert pr.page == 1
        assert pr.page_size == 25

    def test_to_params(self):
        pr = PageRequest(page=3, page_size=50)
        params = pr.to_params()
        assert params == {"page": 3, "pageSize": 50}


class TestPageResponse:
    def test_from_response(self):
        body = {
            "data": [{"id": "1"}, {"id": "2"}],
            "total": 100,
            "page": 2,
            "pageSize": 25,
            "totalPages": 4,
        }
        pr = PageResponse.from_response(body)
        assert len(pr.data) == 2
        assert pr.total == 100
        assert pr.page == 2
        assert pr.page_size == 25
        assert pr.total_pages == 4

    def test_has_next(self):
        pr = PageResponse(page=2, total_pages=4)
        assert pr.has_next is True

    def test_no_next_on_last_page(self):
        pr = PageResponse(page=4, total_pages=4)
        assert pr.has_next is False

    def test_has_previous(self):
        pr = PageResponse(page=2)
        assert pr.has_previous is True

    def test_no_previous_on_first_page(self):
        pr = PageResponse(page=1)
        assert pr.has_previous is False

    def test_calculated_total_pages(self):
        body = {"data": [], "total": 99, "page": 1, "pageSize": 25}
        pr = PageResponse.from_response(body)
        assert pr.total_pages == 4

    def test_items_key_fallback(self):
        body = {"items": [{"id": "a"}], "totalItems": 50, "currentPage": 1, "itemsPerPage": 10}
        pr = PageResponse.from_response(body)
        assert len(pr.data) == 1
        assert pr.total == 50
