from logic.matrix.system import System
from logic.matrix.context import Context
from common.logger import logger
from logic.component.state_component import State
from logic.matrix.group import Group
from logic.matrix.matcher import Matcher


class ColliderSystem(System):

    def __init__(self, context: Context):
        super(ColliderSystem, self).__init__(context)
        self.box_collider_group: Group = self.context.get_group(Matcher("boxcollider"))

    def update(self):
        entities = list(self.context.entities)
        for i in range(len(entities)):
            entity_a = entities[i]
            if not entity_a.get_component("move"):
                continue

            entity_a.get_component("boxcollider").collider_direction = (0, 0)
            for j in range(len(entities)):
                if i == j:
                    continue

                entity_b = entities[j]
                entity_b.get_component("boxcollider").collider_direction = (0, 0)
                if entity_a.get_component("boxcollider").layer != entity_b.get_component("boxcollider").layer:
                    continue
                if (entity_b.get_component("bullet") and entity_b.get_component("bullet").belong == entity_a.uid) or \
                        (entity_a.get_component("bullet") and entity_a.get_component("bullet").belong == entity_b.uid):
                    continue

                position_a = entity_a.get_component("transform").position
                position_b = entity_b.get_component("transform").position
                distance_x = (entity_a.get_component("boxcollider").width + entity_b.get_component("boxcollider").width) / 2
                distance_y = (entity_a.get_component("boxcollider").height + entity_b.get_component("boxcollider").height) / 2

                if position_a[0] >= position_b[0] and position_a[1] >= position_b[1]:
                    delta_x = position_a[0] - position_b[0] - distance_x
                    delta_y = position_a[1] - position_b[1] - distance_y
                    if not (delta_x < 0 and delta_y < 0):
                        continue
                    collider_direction = [-delta_x, -delta_y]
                elif position_a[0] >= position_b[0] and position_a[1] < position_b[1]:
                    delta_x = position_a[0] - position_b[0] - distance_x
                    delta_y = position_b[1] - position_a[1] - distance_y
                    if not (delta_x < 0 and delta_y < 0):
                        continue
                    collider_direction = [-delta_x, delta_y]
                elif position_a[0] < position_b[0] and position_a[1] >= position_b[1]:
                    delta_x = position_b[0] - position_a[0] - distance_x
                    delta_y = position_a[1] - position_b[1] - distance_y
                    if not (delta_x < 0 and delta_y < 0):
                        continue
                    collider_direction = [delta_x, -delta_y]
                else:
                    delta_x = position_b[0] - position_a[0] - distance_x
                    delta_y = position_b[1] - position_a[1] - distance_y
                    if not (delta_x < 0 and delta_y < 0):
                        continue
                    collider_direction = [delta_x, delta_y]

                if entity_a.get_component("transform").rotation == 0.0 or entity_a.get_component("transform").rotation == 180.0:
                    collider_direction[0] = 0
                if entity_a.get_component("transform").rotation == 90.0 or entity_a.get_component("transform").rotation == 270.0:
                    collider_direction[1] = 0

                if collider_direction == [0, 0]:
                    continue

                if entity_a.get_component("bullet") and entity_b.get_component("model"):
                    if entity_b.model.model_name in ["wall", "enemy"]:
                        entity_b.state.state = State.destroy
                    if entity_b.model.model_index in ["symbol"]:
                        entity_b.model.model_index = "destroy"
                    if entity_b.model.model_name not in ["water"]:
                        entity_a.state.state = State.destroy
                    continue

                if entity_a.get_component("model") and entity_a.get_component("model").model_name == "enemy":
                    if entity_b.get_component("bullet") and entity_b.get_component("bullet").belong != entity_a.uid:
                        entity_a.get_component("state").state = State.destroy
                        continue

                if entity_a.get_component("state").state == State.move:
                    entity_a.get_component("transform").add_position(collider_direction[0], collider_direction[1])

                entity_a.get_component("boxcollider").collider_direction = (collider_direction[0], collider_direction[1])
                logger.debug(f"box collider detect {collider_direction}: {entity_a.uid} -> {entity_b.uid}")


