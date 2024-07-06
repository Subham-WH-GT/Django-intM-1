import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Chat,Group

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName=self.scope['url_route']['kwargs']['groupkaname']
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )

        await self.accept()  

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_name
        )

    async def receive(self,text_data):
        text_data_json=json.loads(text_data)
        # print(text_data_json)
        message=text_data_json["message"]
        username=text_data_json["username"]
        group=await database_sync_to_async(Group.objects.get)(name=self.roomGroupName)
        chat=Chat(user=username ,content=message,group=group)
        await database_sync_to_async(chat.save)()
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type":"sendMessage",
                "message":message,
                "username":username,
            }
        )  

    async def sendMessage(self,event):
        message=event["message"]
        username=event["username"]
        await self.send(text_data=json.dumps({
            "message":message,
            "username":username
        }))  


class onetoone(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName="subham"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )

        await self.accept()  

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_name
        )

    async def receive(self,text_data):
        text_data_json=json.loads(text_data)
        # print(text_data_json)
        message=text_data_json["message"]
        username=text_data_json["username"]

        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type":"sendMessage",
                "message":message,
                "username":username,
            }
        )  

    async def sendMessage(self,event):
        message=event["message"]
        username=event["username"]
        await self.send(text_data=json.dumps({
            "message":message,
            "username":username
        }))            