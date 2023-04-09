from logic.interface.system import System
from logic.context import Context
from common.logger import logger
from logic.component.state_component import State


class ColliderSystem(System):

    def __init__(self, context: Context):
        super(ColliderSystem, self).__init__(context)

    def update(self):
        entities = self.context.get_entities()
        for i in range(len(entities)):
            entity_a = entities[i]
            if not entity_a.box_collider or not entity_a.move:
                continue

            entity_a.box_collider.collider_direction = (0, 0)
            for j in range(len(entities)):
                if i == j:
                    continue

                entity_b = entities[j]
                if not entity_b.box_collider:
                    continue
                entity_b.box_collider.collider_direction = (0, 0)
                if entity_a.box_collider.layer != entity_b.box_collider.layer:
                    continue
                if (entity_b.bullet and entity_b.bullet.belong == entity_a.uid) or \
                        (entity_a.bullet and entity_a.bullet.belong == entity_b.uid):
                    continue

                position_a = entity_a.transform.position
                position_b = entity_b.transform.position
                distance_x = (entity_a.box_collider.width + entity_b.box_collider.width) / 2
                distance_y = (entity_a.box_collider.height + entity_b.box_collider.height) / 2

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

                if entity_a.transform.rotation == 0.0 or entity_a.transform.rotation == 180.0:
                    collider_direction[0] = 0
                if entity_a.transform.rotation == 90.0 or entity_a.transform.rotation == 270.0:
                    collider_direction[1] = 0

                if collider_direction == [0, 0]:
                    continue

                entity_a.box_collider.collider_direction = (collider_direction[0], collider_direction[1])
                logger.debug(f"box collider detect {collider_direction}: {entity_a.uid} -> {entity_b.uid}")

                if entity_a.bullet:
                    entity_a.state.state = State.destroy
                    continue

                if entity_a.state.state == State.move:
                    entity_a.transform.add_position(collider_direction[0], collider_direction[1])


