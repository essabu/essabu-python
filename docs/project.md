# Project Module

Project management: projects, tasks, milestones, resource allocations, task comments, and reports.

## Available Classes

| Class | Resource Path | Description |
|-------|--------------|-------------|
| `ProjectApi` | `/api/project/projects` | Project management |
| `TaskApi` | `/api/project/tasks` | Task tracking |
| `MilestoneApi` | `/api/project/milestones` | Project milestones |
| `ResourceAllocationApi` | `/api/project/resource_allocations` | Resource assignments |
| `TaskCommentApi` | `/api/project/task_comments` | Task discussion comments |
| `ReportApi` | `/api/project/reports` | Project reports |

## Standard CRUD Methods

All classes share:

```python
list(*, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse
list_all(*, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]
create(**data: Any) -> dict[str, Any]
retrieve(resource_id: str) -> dict[str, Any]
update(resource_id: str, **data: Any) -> dict[str, Any]
delete(resource_id: str) -> dict[str, Any]
```

## Code Examples

### Project Lifecycle

```python
from essabu import Essabu

client = Essabu(api_key="your-api-key")

# Create a project
project = client.project.projects.create(
    name="Website Redesign",
    description="Complete redesign of the corporate website",
    start_date="2026-04-01",
    end_date="2026-09-30",
    budget=50000,
    currency="USD",
    manager_id="user-uuid",
)

# List active projects
projects = client.project.projects.list(status="active")

# Update project
client.project.projects.update(project["id"], status="in_progress")

# Retrieve project details
details = client.project.projects.retrieve(project["id"])
```

### Tasks

```python
# Create a task
task = client.project.tasks.create(
    project_id=project["id"],
    title="Design mockups",
    description="Create wireframes and high-fidelity mockups",
    assignee_id="user-uuid",
    priority="high",
    due_date="2026-04-15",
    estimated_hours=40,
)

# List tasks for a project
tasks = client.project.tasks.list(project_id=project["id"], status="todo")

# Update task progress
client.project.tasks.update(task["id"], status="in_progress", progress=50)

# Iterate all tasks
for page in client.project.tasks.list_all(project_id=project["id"]):
    for t in page.data:
        print(f"{t['title']}: {t['status']}")
```

### Milestones

```python
milestone = client.project.milestones.create(
    project_id=project["id"],
    name="Design Phase Complete",
    due_date="2026-05-01",
    description="All design deliverables approved",
)
milestones = client.project.milestones.list(project_id=project["id"])
client.project.milestones.update(milestone["id"], status="completed")
```

### Resource Allocations

```python
allocation = client.project.resource_allocations.create(
    project_id=project["id"],
    user_id="user-uuid",
    role="Designer",
    allocation_percentage=80,
    start_date="2026-04-01",
    end_date="2026-05-31",
)
allocations = client.project.resource_allocations.list(project_id=project["id"])
```

### Task Comments

```python
comment = client.project.task_comments.create(
    task_id=task["id"],
    author_id="user-uuid",
    body="Mockups are ready for review. See attached files.",
)
comments = client.project.task_comments.list(task_id=task["id"])
client.project.task_comments.update(comment["id"], body="Updated comment text")
client.project.task_comments.delete(comment["id"])
```

### Reports

```python
reports = client.project.reports.list(project_id=project["id"])
report = client.project.reports.create(
    project_id=project["id"],
    type="progress",
    period="2026-Q2",
)
details = client.project.reports.retrieve(report["id"])
```
