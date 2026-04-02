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

All classes share these standard methods for paginated listing, creation, retrieval, update, and deletion. The `list` method returns a `PageResponse` and supports keyword filters such as `project_id`, `status`, or `assignee_id`. The `list_all` method returns a generator that automatically fetches every page. All write methods return the created or updated resource as a dictionary.

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

Create, list, update, and retrieve projects. The `create` method requires `name`, `start_date`, and `end_date`, with optional fields like `description`, `budget`, `currency`, and `manager_id`. The `list` method supports filtering by `status` (e.g., `"active"`, `"completed"`, `"on_hold"`). The `update` method can change any project field including status transitions. Returns the full project object with computed fields like progress percentage.

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

Create and manage tasks within a project. The `create` method requires `project_id`, `title`, and supports optional fields like `description`, `assignee_id`, `priority` (`"low"`, `"medium"`, `"high"`, `"critical"`), `due_date`, and `estimated_hours`. The `list` method filters by `project_id` and `status` (`"todo"`, `"in_progress"`, `"done"`). Use `update` to change status and track progress as a percentage (0-100).

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

Create and track project milestones that mark key deliverables or phase completions. The `create` method requires `project_id`, `name`, and `due_date`, with an optional `description`. Milestones can be updated to `"completed"` status when the deliverable is achieved. Use `list` with a `project_id` filter to retrieve all milestones for a specific project, ordered by due date.

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

Assign team members to projects with specific roles and allocation percentages. The `create` method requires `project_id`, `user_id`, `role`, `allocation_percentage` (0-100), `start_date`, and `end_date`. This enables capacity planning and prevents over-allocation of team members across projects. The `list` method with a `project_id` filter returns all allocations for a given project.

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

Add, update, and delete discussion comments on tasks. The `create` method requires `task_id`, `author_id`, and `body` (the comment text, supporting plain text). Use `list` with a `task_id` filter to retrieve all comments in chronological order. Comments can be updated (edited) or deleted by their author. This provides an audit trail of task-related discussions and decisions.

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

Generate and retrieve project reports for tracking progress, budgets, and timelines. The `create` method generates a new report for a specific `project_id`, `type` (e.g., `"progress"`, `"budget"`, `"timeline"`), and `period`. The `list` method filters reports by `project_id`. The `retrieve` method returns the full report with detailed metrics, charts data, and recommendations.

```python
reports = client.project.reports.list(project_id=project["id"])
report = client.project.reports.create(
    project_id=project["id"],
    type="progress",
    period="2026-Q2",
)
details = client.project.reports.retrieve(report["id"])
```
