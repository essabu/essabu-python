"""HR module client."""

from __future__ import annotations

from typing import TYPE_CHECKING

from essabu.common.http_client import HttpClient

if TYPE_CHECKING:
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


class HRClient:
    """Client for the HR module."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http
        self._employees: EmployeeApi | None = None
        self._contracts: ContractApi | None = None
        self._leaves: LeaveApi | None = None
        self._payroll: PayrollApi | None = None
        self._shifts: ShiftApi | None = None
        self._shift_schedules: ShiftScheduleApi | None = None
        self._recruitment: RecruitmentApi | None = None
        self._performance: PerformanceApi | None = None
        self._attendance: AttendanceApi | None = None
        self._benefits: BenefitApi | None = None
        self._departments: DepartmentApi | None = None
        self._documents: DocumentApi | None = None
        self._expenses: ExpenseApi | None = None
        self._loans: LoanApi | None = None
        self._onboarding: OnboardingApi | None = None
        self._positions: PositionApi | None = None
        self._skills: SkillApi | None = None
        self._timesheets: TimesheetApi | None = None
        self._training: TrainingApi | None = None
        self._disciplinary: DisciplinaryApi | None = None
        self._history: HistoryApi | None = None
        self._config: ConfigApi | None = None
        self._reports: ReportApi | None = None
        self._webhooks: WebhookApi | None = None

    @property
    def employees(self) -> EmployeeApi:
        if self._employees is None:
            from essabu.hr.api.employees import EmployeeApi
            self._employees = EmployeeApi(self._http)
        return self._employees
    @property
    def contracts(self) -> ContractApi:
        if self._contracts is None:
            from essabu.hr.api.contracts import ContractApi
            self._contracts = ContractApi(self._http)
        return self._contracts
    @property
    def leaves(self) -> LeaveApi:
        if self._leaves is None:
            from essabu.hr.api.leaves import LeaveApi
            self._leaves = LeaveApi(self._http)
        return self._leaves
    @property
    def payroll(self) -> PayrollApi:
        if self._payroll is None:
            from essabu.hr.api.payroll import PayrollApi
            self._payroll = PayrollApi(self._http)
        return self._payroll
    @property
    def shifts(self) -> ShiftApi:
        if self._shifts is None:
            from essabu.hr.api.shifts import ShiftApi
            self._shifts = ShiftApi(self._http)
        return self._shifts
    @property
    def shift_schedules(self) -> ShiftScheduleApi:
        if self._shift_schedules is None:
            from essabu.hr.api.shift_schedules import ShiftScheduleApi
            self._shift_schedules = ShiftScheduleApi(self._http)
        return self._shift_schedules
    @property
    def recruitment(self) -> RecruitmentApi:
        if self._recruitment is None:
            from essabu.hr.api.recruitment import RecruitmentApi
            self._recruitment = RecruitmentApi(self._http)
        return self._recruitment
    @property
    def performance(self) -> PerformanceApi:
        if self._performance is None:
            from essabu.hr.api.performance import PerformanceApi
            self._performance = PerformanceApi(self._http)
        return self._performance
    @property
    def attendance(self) -> AttendanceApi:
        if self._attendance is None:
            from essabu.hr.api.attendance import AttendanceApi
            self._attendance = AttendanceApi(self._http)
        return self._attendance
    @property
    def benefits(self) -> BenefitApi:
        if self._benefits is None:
            from essabu.hr.api.benefits import BenefitApi
            self._benefits = BenefitApi(self._http)
        return self._benefits
    @property
    def departments(self) -> DepartmentApi:
        if self._departments is None:
            from essabu.hr.api.departments import DepartmentApi
            self._departments = DepartmentApi(self._http)
        return self._departments
    @property
    def documents(self) -> DocumentApi:
        if self._documents is None:
            from essabu.hr.api.documents import DocumentApi
            self._documents = DocumentApi(self._http)
        return self._documents
    @property
    def expenses(self) -> ExpenseApi:
        if self._expenses is None:
            from essabu.hr.api.expenses import ExpenseApi
            self._expenses = ExpenseApi(self._http)
        return self._expenses
    @property
    def loans(self) -> LoanApi:
        if self._loans is None:
            from essabu.hr.api.loans import LoanApi
            self._loans = LoanApi(self._http)
        return self._loans
    @property
    def onboarding(self) -> OnboardingApi:
        if self._onboarding is None:
            from essabu.hr.api.onboarding import OnboardingApi
            self._onboarding = OnboardingApi(self._http)
        return self._onboarding
    @property
    def positions(self) -> PositionApi:
        if self._positions is None:
            from essabu.hr.api.positions import PositionApi
            self._positions = PositionApi(self._http)
        return self._positions
    @property
    def skills(self) -> SkillApi:
        if self._skills is None:
            from essabu.hr.api.skills import SkillApi
            self._skills = SkillApi(self._http)
        return self._skills
    @property
    def timesheets(self) -> TimesheetApi:
        if self._timesheets is None:
            from essabu.hr.api.timesheets import TimesheetApi
            self._timesheets = TimesheetApi(self._http)
        return self._timesheets
    @property
    def training(self) -> TrainingApi:
        if self._training is None:
            from essabu.hr.api.training import TrainingApi
            self._training = TrainingApi(self._http)
        return self._training
    @property
    def disciplinary(self) -> DisciplinaryApi:
        if self._disciplinary is None:
            from essabu.hr.api.disciplinary import DisciplinaryApi
            self._disciplinary = DisciplinaryApi(self._http)
        return self._disciplinary
    @property
    def history(self) -> HistoryApi:
        if self._history is None:
            from essabu.hr.api.history import HistoryApi
            self._history = HistoryApi(self._http)
        return self._history
    @property
    def config(self) -> ConfigApi:
        if self._config is None:
            from essabu.hr.api.config_api import ConfigApi
            self._config = ConfigApi(self._http)
        return self._config
    @property
    def reports(self) -> ReportApi:
        if self._reports is None:
            from essabu.hr.api.reports import ReportApi
            self._reports = ReportApi(self._http)
        return self._reports
    @property
    def webhooks(self) -> WebhookApi:
        if self._webhooks is None:
            from essabu.hr.api.webhooks import WebhookApi
            self._webhooks = WebhookApi(self._http)
        return self._webhooks
