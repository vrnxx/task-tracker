from builtins import Exception


class StatusNotFoundError(Exception):
    def __init__(self, status_id):
        self.status_id = status_id
        self.message = f'Status with id[{self.status_id}] not found'
        super().__init__(self.message)
