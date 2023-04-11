from logic.matrix.system import System
from logic.matrix.context import Context
from logic.component.state_component import State
from logic.matrix.group import Group
from logic.matrix.matcher import Matcher


class MoveSystem(System):

    def __init__(self, context: Context):
        super(MoveSystem, self).__init__(context)
        self.move_group: Group = self.context.get_group(Matcher("move", "state"))

    def update(self):
        for entity in self.move_group.entities:
            if entity.get_component("move").speed <= 0:
                continue
            if entity.get_component("state").state != State.move:
                continue

            x, y = entity.get_component("transform").position
            entity.get_component("transform").last_position = (x, y)
            if entity.get_component("transform").rotation == 0:
                if entity.get_component("boxcollider") and entity.get_component("boxcollider").collider_direction[1] > 0:
                    continue
                y -= entity.get_component("move").speed
            if entity.get_component("transform").rotation == 180:
                if entity.get_component("boxcollider") and entity.get_component("boxcollider").collider_direction[1] < 0:
                    continue
                y += entity.get_component("move").speed
            if entity.get_component("transform").rotation == 90:
                if entity.get_component("boxcollider") and entity.get_component("boxcollider").collider_direction[0] > 0:
                    continue
                x -= entity.get_component("move").speed
            if entity.get_component("transform").rotation == 270:
                if entity.get_component("boxcollider") and entity.get_component("boxcollider").collider_direction[0] < 0:
                    continue
                x += entity.get_component("move").speed

            if entity.get_component("boxcollider"):
                x = min(max(x, entity.get_component("boxcollider").width / 2), self.context.edge_size[0] - entity.get_component("boxcollider").width / 2)
                y = min(max(y, entity.get_component("boxcollider").height / 2), self.context.edge_size[1] - entity.get_component("boxcollider").height / 2)
            entity.get_component("transform").position = (x, y)

            if entity.get_component("bullet") and entity.get_component("transform").last_position == entity.get_component("transform").position:
                entity.get_component("state").state = State.destroy

