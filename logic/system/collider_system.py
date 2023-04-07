from logic.interface.system import System
from logic.context import Context
from common.logger import logger


class ColliderSystem(System):

    def __init__(self, context: Context):
        super(ColliderSystem, self).__init__(context)

    async def update(self):
        entities = self.context.get_entities()
        for i in range(len(entities)):
            entity_a = entities[i]
            if not entity_a.box_collider or not entity_a.move:
                continue

            for j in range(i + 1, len(entities)):
                entity_b = entities[j]
                if not entity_b.box_collider:
                    continue
                if entity_a.box_collider.layer != entity_b.box_collider.layer:
                    continue

                position_a = entity_a.transform.position
                heigh_a = entity_a.box_collider.height
                width_a = entity_a.box_collider.width

                position_b = entity_b.transform.position
                height_b = entity_b.box_collider.height
                width_b = entity_b.box_collider.width

                collider_direction = [0, 0]
                if position_a[0] >= position_b[0] and position_a[1] >= position_b[1]:
                    distance_x = position_a[0] - position_b[0]
                    distance_y = position_a[1] - position_b[1]
                    if not (distance_x < (width_a + width_b) / 2 and distance_y < (heigh_a + height_b) / 2):
                        continue
                    collider_direction = [-1, -1]
                elif position_a[0] >= position_b[0] and position_a[1] < position_b[1]:
                    distance_x = position_a[0] - position_b[0]
                    distance_y = position_b[1] - position_a[1]
                    if not (distance_x < (width_a + width_b) / 2 and distance_y < (heigh_a + height_b) / 2):
                        continue
                    collider_direction = [-1, 1]
                elif position_a[0] < position_b[0] and position_a[1] < position_b[1]:
                    distance_x = position_b[0] - position_a[0]
                    distance_y = position_b[1] - position_a[1]
                    if not (distance_x < (width_a + width_b) / 2 and distance_y < (heigh_a + height_b) / 2):
                        continue
                    collider_direction = [1, 1]
                elif position_a[0] < position_b[0] and position_a[1] >= position_b[1]:
                    distance_x = position_b[0] - position_a[0]
                    distance_y = position_a[1] - position_b[1]
                    if not (distance_x < (width_a + width_b) / 2 and distance_y < (heigh_a + height_b) / 2):
                        continue
                    collider_direction = [1, -1]

                if position_a[0] == position_b[0]:
                    collider_direction[0] = 0
                if position_a[1] == position_b[1]:
                    collider_direction[1] = 0

                logger.info(f"box collider detect {collider_direction}: {entity_a.uid} -> {entity_b.uid}")

