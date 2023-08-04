from dataclasses import dataclass


@dataclass
class UserDto:
    id: int
    username: str
    surname: str
    email: str
