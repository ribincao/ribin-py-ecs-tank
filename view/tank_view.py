from view.iview import IView
from logic.context import Context
from common.logger import logger
from logic.entity.entity import GameLogicEntity
from view.behavior.tank_behavior import TankBehavior
from common.data_util import data_util
import asyncio
from logic.command.move_command import MoveCmd, UP, DOWN, LEFT, RIGHT


class TankView(IView):
    MODULE = 'tank'

    def __init__(self, context: Context):
        super(TankView, self).__init__(context)

    async def update(self):
        while True:
            behaviors = {}
            for entity in self.context.get_entities():
                behavior = self.behaviors.get(entity.uid, None)
                if behavior:
                    behavior.entity = entity
                    behaviors[entity.uid] = behavior
                    logger.debug(f"update_behavior {behavior.mode}")
                    continue
                behavior = self.create_behavior(entity)
                behaviors[entity.uid] = behavior
            self.behaviors = behaviors
            await asyncio.sleep(self.VIEW_RATE)

    def create_behavior(self, entity: GameLogicEntity):
        behavior = TankBehavior(entity)

        if entity.create:
            behavior.init_models(self.MODULE, entity.create.mod_id)
        self.behaviors[entity.uid] = behavior
        return behavior

    def init_view(self):
        scene_maps = data_util.load_from_json('./view/scene/tank.json')
        logger.info(f"view_load_tank_scene {scene_maps}")

    async def handle_event(self, operation: str):
        cmd = None
        if operation == 'w':
            cmd = MoveCmd(1)
            cmd.direction = UP
        elif operation == 'a':
            cmd = MoveCmd(1)
            cmd.direction = LEFT
        elif operation == 's':
            cmd = MoveCmd(1)
            cmd.direction = DOWN
        elif operation == 'd':
            cmd = MoveCmd(1)
            cmd.direction = RIGHT
        
        if cmd:
            self.context.input_command(cmd)
