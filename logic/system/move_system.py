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
            if not entity.move or not entity.state or not entity.transform:
                continue
            if entity.move.speed <= 0:
                continue
            if entity.state.state != State.move:
                continue

            x, y = entity.transform.position
            entity.transform.last_position = (x, y)
            if entity.transform.rotation == 0:
                if entity.box2d_collider and entity.box2d_collider.collider_direction[1] > 0:
                    continue
                y -= entity.move.speed
            if entity.transform.rotation == 180:
                if entity.box2d_collider and entity.box2d_collider.collider_direction[1] < 0:
                    continue
                y += entity.move.speed
            if entity.transform.rotation == 90:
                if entity.box2d_collider and entity.box2d_collider.collider_direction[0] > 0:
                    continue
                x -= entity.move.speed
            if entity.transform.rotation == 270:
                if entity.box2d_collider and entity.box2d_collider.collider_direction[0] < 0:
                    continue
                x += entity.move.speed

            if entity.box2d_collider:
                x = min(max(x, entity.box2d_collider.width / 2), self.context.edge_size[0] - entity.box2d_collider.width / 2)
                y = min(max(y, entity.box2d_collider.height / 2), self.context.edge_size[1] - entity.box2d_collider.height / 2)
            entity.transform.position = (x, y)

            if entity.bullet and entity.transform.last_position == entity.transform.position:
                entity.state.state = State.destroy

