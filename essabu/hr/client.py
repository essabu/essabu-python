"""HR module client for the Essabu SDK."""

from __future__ import annotations

from functools import cached_property

from essabu.common.http_client import HttpClient
from essabu.hr.api.attendance import AttendanceApi
from essabu.hr.api.benefits import BenefitApi
from essabu.hr.api.config_api import ConfigApi
from essabu.hr.api.contracts import ContractApi
from essabu.hr.api.departments import DepartmentApi
from essabu.hr.api.disciplinary import DisciplinaryApi
from essabu.hr.api.documents import DocumentApi
from essabu.hr.api.employees import EmployeeApi
from essabu.hr.api.expenses import ExpenseApi
from essabu.hr.api.history import HistoryApi
from essabu.hr.api.leaves import LeaveApi
from essabu.hr.api.loans import LoanApi
from essabu.hr.api.onboarding import OnboardingApi
from essabu.hr.api.payroll import PayrollApi
from essabu.hr.api.performance import PerformanceApi
from essabu.hr.api.positions import PositionApi
from essabu.hr.api.recruitment import RecruitmentApi
from essabu.hr.api.reports import ReportApi
from essabu.hr.api.shift_schedules import ShiftScheduleApi
from essabu.hr.api.shifts import ShiftApi
from essabu.hr.api.skills import SkillApi
from essabu.hr.api.timesheets import TimesheetApi
from essabu.hr.api.training import TrainingApi
from essabu.hr.api.webhooks import WebhookApi


class HrClient:
    """HR module client providing access to all HR API resources."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    @cached_property
    def employees(self) -> EmployeeApi:
        return EmployeeApi(self._http)

    @cached_property
    def departments(self) -> DepartmentApi:
        return DepartmentApi(self._http)

    @cached_property
    def positions(self) -> PositionApi:
        return PositionApi(self._http)

    @cached_property
    def contracts(self) -> ContractApi:
        return ContractApi(self._http)

    @cached_property
    def attendances(self) -> AttendanceApi:
        return AttendanceApi(self._http)

    @cached_property
    def leaves(self) -> LeaveApi:
        return LeaveApi(self._http)

    @cached_property
    def shifts(self) -> ShiftApi:
        return ShiftApi(self._http)

    @cached_property
    def shift_schedules(self) -> ShiftScheduleApi:
        return ShiftScheduleApi(self._http)

    @cached_property
    def trainings(self) -> TrainingApi:
        return TrainingApi(self._http)

    @cached_property
    def payrolls(self) -> PayrollApi:
        return PayrollApi(self._http)

    @cached_property
    def expenses(self) -> ExpenseApi:
        return ExpenseApi(self._http)

    @cached_property
    def recruitment(self) -> RecruitmentApi:
        return RecruitmentApi(self._http)

    @cached_property
    def performance(self) -> PerformanceApi:
        return PerformanceApi(self._http)

    @cached_property
    def onboarding(self) -> OnboardingApi:
        return OnboardingApi(self._http)

    @cached_property
    def documents(self) -> DocumentApi:
        return DocumentApi(self._http)

    @cached_property
    def disciplinary(self) -> DisciplinaryApi:
        return DisciplinaryApi(self._http)

    @cached_property
    def benefits(self) -> BenefitApi:
        return BenefitApi(self._http)

    @cached_property
    def loans(self) -> LoanApi:
        return LoanApi(self._http)

    @cached_property
    def timesheets(self) -> TimesheetApi:
        return TimesheetApi(self._http)

    @cached_property
    def skills(self) -> SkillApi:
        return SkillApi(self._http)

    @cached_property
    def reports(self) -> ReportApi:
        return ReportApi(self._http)

    @cached_property
    def webhooks(self) -> WebhookApi:
        return WebhookApi(self._http)

    @cached_property
    def config(self) -> ConfigApi:
        return ConfigApi(self._http)

    @cached_property
    def history(self) -> HistoryApi:
        return HistoryApi(self._http)
