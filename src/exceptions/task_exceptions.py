from builtins import Exception


class TaskNotFoundError(Exception):
    def __init__(self, task_id):
        self.task_id = task_id
        self.message = f'Task with id[{self.task_id}] not found'
        super().__init__(self.message)
