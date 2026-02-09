import os
import django
import random
from faker import Faker

# 1️⃣ Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')  # adjust if needed
django.setup()

# 2️⃣ Import models AFTER Django setup

from tasks.models import Project, Task, TaskDetail
from django.contrib.auth import get_user_model

User = get_user_model()

# 3️⃣ Populate function
def populate_db():
    fake = Faker()

    # 3a. Use existing users
    users = list(User.objects.all())
    if not users:
        print("No users found in the database! Add some users first.")
        return
    print(f"Found {len(users)} existing users.")

    # 3b. Create projects
    projects = [
        Project.objects.create(
            name=fake.bs().capitalize(),
            description=fake.paragraph(),
            start_date=fake.date_this_year()
        )
        for _ in range(5)
    ]
    print(f"Created {len(projects)} projects.")

    # 3c. Create tasks
    tasks = []
    for _ in range(20):
        task = Task.objects.create(
            project=random.choice(projects),
            title=fake.sentence(),
            description=fake.paragraph(),
            due_date=fake.date_this_year(),
            status=random.choice(['PENDING', 'IN_PROGRESS', 'COMPLETED']),
        )
        # Assign 1-3 random existing users
        task.assigned_to.set(random.sample(users, random.randint(1, min(3, len(users)))))
        tasks.append(task)
    print(f"Created {len(tasks)} tasks.")

    # 3d. Create task details
    for task in tasks:
        TaskDetail.objects.create(
            task=task,
            priority=random.choice(['H', 'M', 'L']),
            notes=fake.paragraph()
        )
    print("Created TaskDetails for all tasks.")
    print("Database populated successfully!")

# 4️⃣ Run
if __name__ == "__main__":
    populate_db()
