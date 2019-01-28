from dataclasses import dataclass, field
import uuid
from typing import Dict
from models.model import Model
from common.database import Database
from models.store import StoreErrors


@dataclass
class Store(Model):
    collection: str = field(init=False, default="stores")
    name: str
    url_prefix: str
    tag_name: str
    query: Dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }

    @classmethod
    def get_by_name(cls, store_name: str) -> "Store":
        return cls.find_one_by("name", store_name)

    @classmethod
    def get_by_url_prefix(cls, url_prefix: str) -> "Store":
        url_regex = {"$regex": '^{}'.format(url_prefix)}
        return cls.find_one_by("url_prefix", url_regex)

    @classmethod
    def find_by_url(cls, url: str) -> "Store":
        """
        Return a store from a url like "http://www.johnlewis.com/item/sdfj4h5g4g21k.html"
        :param url: The item's URL
        :return: a Store, or raises a StoreNotFoundException if no store matches the URL
        """
        for i in range(len(url)+1, 0, -1):
            try:
                print(f"Trying to find store starting with {url[:i]}")
                store = cls.get_by_url_prefix(url[:i])
                return store
            except:
                continue
        else:
            raise StoreErrors.StoreNotFoundException("The URL Prefix used to find the store didn't give us any results!")
