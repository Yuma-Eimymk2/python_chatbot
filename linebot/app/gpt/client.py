from dataclasses import dataclass, field
import os
from typing import List

import openai
from openai.openai_object import OpenAIObject

from app.gpt.constants import Model
from app.gpt.message import Message

key = os.getenv("CHATGPT_API_KEY")
openai.api_key = key


@dataclass
class ChatGPTClient:
    model: Model
    messages: List[Message] = field(default_factory=list)

    def add_message(self, message: Message) -> None:
        self.messages.append(message)

    def create(self) -> OpenAIObject:
        res = openai.ChatCompletion.create(
            model=self.model.value,
            messages=[m.to_dict() for m in self.messages],
        )
        self.add_message(Message.from_dict(res["choices"][0]["message"]))
        return res
