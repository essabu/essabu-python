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

All resource classes (except `ConfigApi` and `ReportApi`) expose these standard methods for paginated listing, full-page iteration, creation, retrieval by ID, update, and soft deletion. The `list` method accepts optional keyword filters such as `department`, `status`, or `employee_id`. The `list_all` method returns a generator that automatically fetches every page. All write methods return the created or updated resource as a dictionary.

```python
list(*, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse
list_all(*, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]
create(**data: Any) -> dict[str, Any]
retrieve(resource_id: str) -> dict[str, Any]
update(resource_id: str, **data: Any) -> dict[str, Any]
delete(resource_id: str) -> dict[str, Any]
```

## ConfigApi Methods

The `ConfigApi` provides methods for reading and updating HR module configuration. The `get_settings` method returns the current HR configuration including defaults for leave, overtime, and pay grades. The `update_settings` method accepts keyword arguments for any setting field. The `get_leave_types` and `get_pay_grades` methods return the configured leave type definitions and salary grade structures respectively.

```python
get_settings(**params: Any) -> dict[str, Any]          # GET /api/hr/config/settings
update_settings(**data: Any) -> dict[str, Any]          # POST /api/hr/config/settings
get_leave_types(**params: Any) -> dict[str, Any]        # GET /api/hr/config/leave-types
get_pay_grades(**params: Any) -> dict[str, Any]         # GET /api/hr/config/pay-grades
```

## ReportApi Methods

The `ReportApi` provides specialized methods for generating HR analytics. The `headcount` method returns employee counts by department and status for a given year. The `turnover` method calculates hiring and departure rates over a date range. The `payroll_summary` aggregates payroll costs by department and period. The `leave_balance` shows remaining leave days per employee, and `attendance_summary` provides attendance statistics.

```python
headcount(**params: Any) -> dict[str, Any]              # GET /api/hr/reports/headcount
turnover(**params: Any) -> dict[str, Any]               # GET /api/hr/reports/turnover
payroll_summary(**params: Any) -> dict[str, Any]        # GET /api/hr/reports/payroll-summary
leave_balance(**params: Any) -> dict[str, Any]          # GET /api/hr/reports/leave-balance
attendance_summary(**params: Any) -> dict[str, Any]     # GET /api/hr/reports/attendance-summary
```

## Code Examples

### Employee Management

Create, list, iterate, retrieve, update, and delete employee records. The `create` method requires `first_name`, `last_name`, `email`, and optionally accepts `department_id`, `position_id`, and `hire_date`. The `list` method supports filtering by `department` and pagination with `page` and `page_size`. Use `list_all` to iterate through all employees across pages. The `update` method accepts any employee field as a keyword argument.

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

Record and query employee attendance entries. The `create` method requires `employee_id`, `check_in`, and `check_out` times. The `list` method supports filtering by `employee_id` and `date` to retrieve attendance records for a specific employee on a given day. Returns a paginated list of attendance entries with computed fields like total hours worked.

```python
records = client.hr.attendance.list(employee_id="emp-uuid", date="2026-03-26")
client.hr.attendance.create(employee_id="emp-uuid", check_in="08:00", check_out="17:00")
```

### Leave Management

Submit leave requests for employees. The `create` method requires `employee_id`, `type` (e.g., `"annual"`, `"sick"`, `"maternity"`), `start_date`, `end_date`, and an optional `reason`. The request is created with a `"pending"` status and must be approved by a manager. The number of leave days is calculated automatically from the date range, excluding weekends and configured holidays.

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

Create and manage payroll runs for a given period and department. The `create` method requires `period` (in `"YYYY-MM"` format) and `department_id`. It calculates gross pay, deductions, and net pay for all employees in the department based on their contracts and attendance. The `retrieve` method returns the full payroll run with individual pay slip details for each employee.

```python
run = client.hr.payroll.create(period="2026-03", department_id="dept-uuid")
details = client.hr.payroll.retrieve("run-uuid")
```

### Reports

Generate HR analytics reports for organizational insights. The `headcount` method accepts a `year` parameter and returns employee counts grouped by department and employment status. The `turnover` method calculates hiring and departure rates for a date range. The `leave_balance` method shows remaining leave days, optionally filtered by `department_id`.

```python
headcount = client.hr.reports.headcount(year=2026)
turnover = client.hr.reports.turnover(start_date="2026-01-01", end_date="2026-03-31")
balances = client.hr.reports.leave_balance(department_id="dept-uuid")
```

### Configuration

Read and update HR module settings. The `get_settings` method returns the current configuration including default leave allowances, overtime rates, and working hours. The `get_leave_types` method returns all configured leave type definitions. The `get_pay_grades` method returns the salary grade structure. The `update_settings` method accepts keyword arguments for any configuration field and returns the updated settings.

```python
settings = client.hr.config.get_settings()
leave_types = client.hr.config.get_leave_types()
pay_grades = client.hr.config.get_pay_grades()
client.hr.config.update_settings(default_leave_days=25, overtime_rate=1.5)
```
