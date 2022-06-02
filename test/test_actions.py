from .config import pytest, _Config, global_config, config
from bpm.actions import Message

@pytest.mark.asyncio
async def test_msg(config: _Config, global_config = global_config):
    msg = Message(config)
    msg.update()
