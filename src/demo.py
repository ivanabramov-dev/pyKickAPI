from betterKickAPI import Kick, types
import asyncio
from os import environ

APP_ID: str = environ.get('KICK_APP_ID')
SECRET_ID: str = environ.get('KICK_SECRET_ID')


async def kick_example():
        kick = await Kick(APP_ID, SECRET_ID)

        channel = await kick.get_channels(slug='jesusavgn')

        print(channel[0].stream.viewer_count)

        # подписка на чат
        await kick.post_events_subscriptions(broadcaster_user_id=channel[0].broadcaster_user_id, events=[types.EventSubEvents.CHAT_MESSAGE])


asyncio.run(kick_example())