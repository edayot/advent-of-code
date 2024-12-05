from typing import Any, ClassVar, Generator
from networkx import selfloop_edges
from pydantic import BaseModel, Field

class Page(BaseModel):
    number: int = -1
    pages_before: set["Page"] = Field(default_factory=set)
    pages_after: set["Page"] = Field(default_factory=set)

    registry: ClassVar[dict[int, "Page"]] = {}

    def __repr__(self):
        return f"Page(number={self.number})"
    
    def __str__(self):
        return repr(self)

    def model_post_init(self, __context: Any):
        assert self.number not in self.__class__.registry
        self.__class__.registry[self.number] = self

    @classmethod
    def get(cls, number: int):
        if number in cls.registry:
            return cls.registry[number]
        return cls(number=number)

    def __hash__(self):
        return hash(self.number)
    
    def get_pages_before(self) -> Generator["Page", None, None]:
        for before in self.pages_before:
            yield before
            # yield from before.get_pages_before()
    def get_pages_after(self) -> Generator["Page", None, None]:
        for after in self.pages_after:
            yield after
            # yield from after.get_pages_after()
    
    def is_good_printing(self, befores: list["Page"], afters: list["Page"]) -> bool:
        self_pages_before = list(self.get_pages_before())
        self_pages_after = list(self.get_pages_after())
        for before in befores:
            if not (before in self_pages_before):
                return False
            if before in self_pages_after:
                return False
        for after in afters:
            if not (after in self_pages_after):
                return False
            if after in self_pages_before:
                return False
        return True

