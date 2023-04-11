from logic.manager.component_manager import component_manager
from logic.interface.component import Component
from logic.event.event import Event
from common.logger import logger
from typing import Optional, Dict


class GameLogicEntity(object):

    def __init__(self, uid: int, is_async: bool = True):
        self._uid: int = uid
        self.is_async: bool = is_async
        self._is_enable: bool = False
        self._components: Dict[str, Component] = {}
        self.on_component_add: Event = Event()
        self.on_component_remove: Event = Event()
        self.on_component_replace: Event = Event()

    def get_component(self, name: str) -> Optional[Component]:
        if not self.has(name):
            logger.warn(f"entity does not have {name} component.")
            return None
        return self._components[name]

    def __repr__(self):
        return f"[Entity.{self._uid}]: [{', '.join([str(comp) for _, comp in self._components.items()])}]"

    def destroy(self):
        self._is_enable = False
        self.remove_all_component()

    def add_component(self, comp: Component):
        if not self._is_enable:
            logger.error(f"Cannot add component for not enable entity.")
            return
        if self.has(comp.name):
            logger.error(f"entity already have {comp.name} component.")
            return
        self._components[comp.name] = comp
        self.on_component_add(self, comp)

    def replace_component(self, comp: Component):
        if not self._is_enable:
            logger.error(f"Cannot add component for not enable entity.")
            return
        if self.has(comp.name):
            self._replace_component(comp.name, comp)
        else:
            self.add_component(comp)

    def _replace_component(self, comp_name: str, new_comp: Optional[Component]):
        old_comp = self._components[comp_name]
        if not new_comp:
            del self._components[comp_name]
            self.on_component_remove(self, old_comp)
            return
        self._components[comp_name] = new_comp
        self.on_component_replace(old_comp, new_comp)

    def remove_component(self, comp_name: str):
        if not self._is_enable:
            logger.error(f"Cannot add component for not enable entity.")
            return
        if not self.has(comp_name):
            logger.warn(f"entity does not have {comp_name} component.")
            return
        self._replace_component(comp_name, None)

    def remove_all_component(self):
        for name, _ in self._components.items():
            self._replace_component(name, None)

    def has(self, *comp_names: str) -> bool:
        if len(comp_names) == 1:
            return comp_names[0] in self._components
        return all([t_comp in self._components for t_comp in comp_names])

    def has_any(self, *comp_names: str) -> bool:
        if len(comp_names) == 1:
            return comp_names[0] in self._components
        return any([t_comp in self._components for t_comp in comp_names])

    def export(self) -> dict:
        if not self._is_enable or not self.is_async:
            return {}
        d = {}
        for comp_name, component in self._components.items():
            info = component.serialize()
            if not info:
                continue
            d[comp_name] = info
        return d

    def update(self, snap: dict):
        for name, new_component in snap.items():
            component = self._components.get(name, None)
            if not component:
                component = component_manager.get_component(name)
            self._components.update(new_component)
            self._components[name] = component


