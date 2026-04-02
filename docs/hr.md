# HR Module

Human Resources management: employees, departments, contracts, payroll, attendance, leaves, and more.

## Available Classes

| Class | Resource Path | Description |
|-------|--------------|-------------|
| `EmployeeApi` | `/api/hr/employees` | Employee lifecycle management |
| `DepartmentApi` | `/api/hr/departments` | Organizational departments |
| `ContractApi` | `/api/hr/contracts` | Employment contracts |
| `PayrollApi` | `/api/hr/payroll` | Payroll runs and processing |
| `AttendanceApi` | `/api/hr/attendance` | Time and attendance tracking |
| `LeaveApi` | `/api/hr/leaves` | Leave requests and balances |
| `BenefitApi` | `/api/hr/benefits` | Employee benefits |
| `LoanApi` | `/api/hr/loans` | Employee loans |
| `ExpenseApi` | `/api/hr/expenses` | Expense reports |
| `DisciplinaryApi` | `/api/hr/disciplinary` | Disciplinary actions |
| `DocumentApi` | `/api/hr/documents` | Employee documents |
| `HistoryApi` | `/api/hr/history` | Employment history |
| `PositionApi` | `/api/hr/positions` | Job positions |
| `PerformanceApi` | `/api/hr/performance` | Performance reviews |
| `RecruitmentApi` | `/api/hr/recruitment` | Recruitment pipeline |
| `SkillApi` | `/api/hr/skills` | Employee skills |
| `TrainingApi` | `/api/hr/training` | Training programs |
| `OnboardingApi` | `/api/hr/onboarding` | Onboarding checklists |
| `ShiftApi` | `/api/hr/shifts` | Shift definitions |
| `ShiftScheduleApi` | `/api/hr/shift_schedules` | Shift scheduling |
| `TimesheetApi` | `/api/hr/timesheets` | Timesheet entries |
| `WebhookApi` | `/api/hr/webhooks` | HR event webhooks |
| `ConfigApi` | `/api/hr/config` | Module configuration |
| `ReportApi` | `/api/hr/reports` | HR reports and analytics |

## Standard CRUD Methods

All resource classes (except `ConfigApi` and `ReportApi`) expose these methods:

```python
list(*, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse
list_all(*, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]
create(**data: Any) -> dict[str, Any]
retrieve(resource_id: str) -> dict[str, Any]
update(resource_id: str, **data: Any) -> dict[str, Any]
delete(resource_id: str) -> dict[str, Any]
```

## ConfigApi Methods

```python
get_settings(**params: Any) -> dict[str, Any]          # GET /api/hr/config/settings
update_settings(**data: Any) -> dict[str, Any]          # POST /api/hr/config/settings
get_leave_types(**params: Any) -> dict[str, Any]        # GET /api/hr/config/leave-types
get_pay_grades(**params: Any) -> dict[str, Any]         # GET /api/hr/config/pay-grades
```

## ReportApi Methods

```python
headcount(**params: Any) -> dict[str, Any]              # GET /api/hr/reports/headcount
turnover(**params: Any) -> dict[str, Any]               # GET /api/hr/reports/turnover
payroll_summary(**params: Any) -> dict[str, Any]        # GET /api/hr/reports/payroll-summary
leave_balance(**params: Any) -> dict[str, Any]          # GET /api/hr/reports/leave-balance
attendance_summary(**params: Any) -> dict[str, Any]     # GET /api/hr/reports/attendance-summary
```

## Code Examples

### Employee Management

```python
from essabu import Essabu

client = Essabu(api_key="your-api-key")

# List employees with filters
page = client.hr.employees.list(page=1, page_size=10, department="engineering")

# Iterate all pages
for page in client.hr.employees.list_all(page_size=50):
    for employee in page.data:
        print(employee["name"])

# Create an employee
employee = client.hr.employees.create(
    first_name="Jean",
    last_name="Dupont",
    email="jean.dupont@company.com",
    department_id="dept-uuid",
    position_id="pos-uuid",
    hire_date="2026-01-15",
)

# Retrieve, update, delete
emp = client.hr.employees.retrieve("emp-uuid")
client.hr.employees.update("emp-uuid", salary=55000)
client.hr.employees.delete("emp-uuid")
```

### Attendance Tracking

```python
records = client.hr.attendance.list(employee_id="emp-uuid", date="2026-03-26")
client.hr.attendance.create(employee_id="emp-uuid", check_in="08:00", check_out="17:00")
```

### Leave Management

```python
leave = client.hr.leaves.create(
    employee_id="emp-uuid",
    type="annual",
    start_date="2026-04-01",
    end_date="2026-04-05",
    reason="Vacation",
)
```

### Payroll

```python
run = client.hr.payroll.create(period="2026-03", department_id="dept-uuid")
details = client.hr.payroll.retrieve("run-uuid")
```

### Reports

```python
headcount = client.hr.reports.headcount(year=2026)
turnover = client.hr.reports.turnover(start_date="2026-01-01", end_date="2026-03-31")
balances = client.hr.reports.leave_balance(department_id="dept-uuid")
```

### Configuration

```python
settings = client.hr.config.get_settings()
leave_types = client.hr.config.get_leave_types()
pay_grades = client.hr.config.get_pay_grades()
client.hr.config.update_settings(default_leave_days=25, overtime_rate=1.5)
```
