from view.interface.pygame_view import PyGameView
from logic.context import Context
from common.logger import logger
from logic.command.move_command import MoveDirection
from logic.manager.command_manager import command_manager
from logic.interface.command import Command
from typing import Optional, Tuple
from logic.event.event import EntityCreateEvent, EntityDestroyEvent
from view.manager.animation_manager import animation_manager


class TankView(PyGameView):

    def __init__(self, gid: str, context: Context):
        super(TankView, self).__init__(gid, context)
        self.window_size: Tuple[float, float] = (780, 780)
        self.context.register_event("EntityCreateEvent", self.on_entity_create)
        self.context.register_event("EntityDestroyEvent", self.on_entity_destroy)

    def on_entity_create(self, event: EntityCreateEvent):
        logger.info(f"TankVieListen {event.uid} created.")
        entity = self.context.get_entity(event.uid)
        if not entity:
            return
        animation = animation_manager.get_animation(entity, "born")
        if not animation:
            return
        self.animations.append(animation)

    def on_entity_destroy(self, event: EntityDestroyEvent):
        logger.info(f"TankViewListen {event.uid} destroyed.")
        entity = self.context.get_entity(event.uid)
        if not entity:
            return
        animation = animation_manager.get_animation(entity, "boom")
        if not animation:
            return
        self.animations.append(animation)

    def handler(self, operation: str):

        cmd: Optional[Command] = None
        if operation == 'w' and self.player_uid:
            cmd = command_manager.get_move_cmd(self.player_uid, MoveDirection.UP)
        elif operation == 'a' and self.player_uid:
            cmd = command_manager.get_move_cmd(self.player_uid, MoveDirection.LEFT)
        elif operation == 's' and self.player_uid:
            cmd = command_manager.get_move_cmd(self.player_uid, MoveDirection.DOWN)
        elif operation == 'd' and self.player_uid:
            cmd = command_manager.get_move_cmd(self.player_uid, MoveDirection.RIGHT)
        elif operation == '-' and self.player_uid:
            cmd = command_manager.get_move_cmd(self.player_uid, MoveDirection.STOP)

        elif operation in 'n' and self.player_uid <= 0:
            entity = self.context.create_entity()
            player_count = self.context.get_player_count()
            cmd = command_manager.create_tank_player_cmd(entity.uid, "ribincao", player_count % 2 == 0)
            self.context.player_uid = entity.uid

        elif operation == 'j' and self.player_uid > 0:
            tank = self.behaviors.get(self.player_uid)
            if not tank or not tank.entity.model or not tank.entity.move:
                return
            entity = self.context.create_entity()
            cmd = command_manager.tank_shot_cmd(entity.uid, tank)

        elif operation == 't':
            entity = self.context.create_entity()
            cmd = command_manager.create_tank_enemy_cmd(entity.uid)
        self.send_cmd(cmd)
        
    def send_cmd(self, cmd: Optional[Command]):
        if not cmd:
            return
        logger.debug(f"SendCommand {cmd.__dict__}")
        self.context.input_command(cmd)
        if self.context.is_connected:
            self.context.input_message(cmd)

