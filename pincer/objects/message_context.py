# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

from dataclasses import dataclass
from typing import Optional, Union

from .guild_member import GuildMember
from .user import User
from ..utils.snowflake import Snowflake


@dataclass
class MessageContext:
    """
    Represents the context of a message interaction.

    :param id:
        The ID of the interaction.

    :param author:
        The user whom invoked the interaction.

    :param guild_id:
        The ID of the guild the interaction was invoked in.
        Can be None if it wasn't invoked in a guild.

    :param channel_id:
        The ID of the channel the interaction was invoked in.
        Can be None if it wasn't invoked in a channel.
    """
    id: Snowflake
    author: Union[GuildMember, User]

    guild_id: Optional[Snowflake] = None
    channel_id: Optional[Snowflake] = None