from dataclasses import field, dataclass
from typing import Optional
from uuid import UUID, uuid4

import pymongo
from beanie import Document, Indexed
from pydantic import Field


@dataclass
class ProductDto:
    name: str
    price: float
    description: Optional[str] = field(default=None)


class Product(Document):
    id: str = Field(default_factory=lambda: uuid4().hex)
    name: str
    description: Optional[str] = None
    price: Indexed(float, pymongo.DESCENDING)

    class Settings:
        name = "products"
        indexes = [
            [
                ("name", pymongo.TEXT),
                ("description", pymongo.TEXT),
            ],
        ]

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
        }
