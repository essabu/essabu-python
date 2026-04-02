"""Example: Create an employee in the HR module."""

from essabu import Essabu

client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

# Create a new employee
employee = client.hr.employees.create(
    first_name="Jean",
    last_name="Mukendi",
    email="jean.mukendi@company.com",
    department_id="dept-engineering",
    position_id="pos-senior-dev",
    hire_date="2024-01-15",
)
print(f"Created employee: {employee['id']}")

# List all employees with pagination
page = client.hr.employees.list(page=1, page_size=10)
print(f"Total employees: {page.total}")
for emp in page.data:
    print(f"  - {emp['first_name']} {emp['last_name']}")

# Iterate all pages
for page in client.hr.employees.list_all(page_size=50):
    for emp in page.data:
        print(f"  - {emp['first_name']} {emp['last_name']}")

# Update an employee
updated = client.hr.employees.update(employee["id"], position_id="pos-lead-dev")
print(f"Updated position for: {updated['id']}")

client.close()
