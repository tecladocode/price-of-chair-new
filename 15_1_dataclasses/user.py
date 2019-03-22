import uuid
from typing import Dict
from dataclasses import dataclass, field


def generate_hex():
    return uuid.uui4().hex


@dataclass
class User:
    _id: str = field(default_factory=generate_hex)  # field(default_factory=lambda: uuid.uuid4().hex)
    username: str
    password: str = field(repr=False, compare=False)
    country: str = field(default="United Kingdom")

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "username": self.username
        }
