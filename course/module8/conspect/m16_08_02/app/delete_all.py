from models import Task

if __name__ == '__main__':
    task = Task.objects()
    t = task.count()
    task.delete()
    print(f'Deleted {t} tasks')
