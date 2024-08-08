from email import message
import json
import logging 
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
logger = logging.getLogger(__name__)
class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'public_room'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        logger.info(f'WebSocket {self.channel_name} connected.')

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        logger.info(f'WebSocket {self.channel_name} disconnected with close code {close_code}.')


    async def send_notification(self, event):
        await self.send(text_data=json.dumps({ 'message': event['message'] 
    }))

    logger.info(f'Message sent: {message}')
    