from typing import Optional, List
from logic.logic_entity import GameLogicEntity


class Matcher(object):

    def __init__(self, *t_comps, **kwargs):
        self._all: Optional[List[str]] = list(t_comps) if t_comps else kwargs.get("all_of", None)
        self._any: Optional[List[str]] = kwargs.get("any_of", None)
        self._none: Optional[List[str]] = kwargs.get("none_of", None)

    def matches(self, entity: GameLogicEntity) -> bool:
        all_condition = self._all is None or entity.has(*self._all)
        any_condition = self._any is None or entity.has_any(*self._any)
        none_condition = self._none is None or not entity.has_any(*self._none)
        return all_condition and any_condition and none_condition



