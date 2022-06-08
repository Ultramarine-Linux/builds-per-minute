from .config import pytest, _Config, global_config, config
from bpm.actions import Message


@pytest.mark.asyncio
async def test_msg(config: _Config):
    msg = Message(config)
    msg.update()
