from AminoLightPy.lib.util.objects import UserProfile
from AminoLightPy.lib.util.objects import Message
from typing import Dict

class BotAccont(UserProfile):
    def __init__(self, data: Dict):
        super().__init__(data)

class EventsEnum:
    TEXT = "on_text_message"
    PHOTO = "on_image_message"
    AUDIO = "on_voice_message"
    STICKER = "on_sticker_message"