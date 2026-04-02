"""Example: Create an employee in the HR module.

Demonstrates employee creation with required fields, paginated listing,
full-page iteration, and updating an employee record. All operations use
the client.hr.employees resource.
"""

from essabu import Essabu

# Initialize the client with API key and tenant ID. All subsequent API calls
# will be authenticated with this key and scoped to this tenant.
client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

# Create a new employee record. Required fields are first_name, last_name, and email.
# Optional fields include department_id, position_id, and hire_date. Returns the
# created employee as a dictionary including the generated UUID. Raises ValidationError
# if required fields are missing or the email is already in use.
employee = client.hr.employees.create(
    first_name="Jean",
    last_name="Mukendi",
    email="jean.mukendi@company.com",
    department_id="dept-engineering",
    position_id="pos-senior-dev",
    hire_date="2024-01-15",
)
print(f"Created employee: {employee['id']}")

# List employees with pagination. Returns a PageResponse with total count, current
# page number, and the data array. The page_size parameter controls items per page
# (default 25, max 100). Use the total property to display summary information.
page = client.hr.employees.list(page=1, page_size=10)
print(f"Total employees: {page.total}")
for emp in page.data:
    print(f"  - {emp['first_name']} {emp['last_name']}")

# Iterate through all employees across every page using the list_all generator.
# Each iteration yields a PageResponse for one page. The SDK handles pagination
# automatically, fetching the next page when the current one is exhausted.
for page in client.hr.employees.list_all(page_size=50):
    for emp in page.data:
        print(f"  - {emp['first_name']} {emp['last_name']}")

# Update an employee's position by passing the employee ID and the fields to change.
# Only the specified fields are updated; all other fields remain unchanged. Returns
# the full updated employee record. Raises NotFoundError if the ID does not exist.
updated = client.hr.employees.update(employee["id"], position_id="pos-lead-dev")
print(f"Updated position for: {updated['id']}")

client.close()
