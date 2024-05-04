from enum import Enum

class Role(Enum):
    SYETEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class Model(Enum):
    GPT35TURBO = "gpt-3.5-turbo"

