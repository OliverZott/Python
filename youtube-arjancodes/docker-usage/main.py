import json
from dataclasses import dataclass, field
from fastapi import FastAPI, HTTPException, Response

app = FastAPI()


@dataclass
class Channel:
    id: str
    name: str
    tags: list[str] = field(default_factory=list)
    description: str = ""


channels: dict[str, Channel] = {}

# REMARKS: file IO
# keyword argument - arbitrary
with open("channels.json", encoding="utf8") as file:
    channels_raw = json.load(file)
    for channel_raw in channels_raw:
        channel = Channel(**channel_raw)
        channels[channel.id] = channel


@app.get("/")
def read_root() -> Response:
    return Response("The server is running =)")


@app.get("/channels/{channel_id}", response_model=Channel)
def read_item(channel_id: str) -> Channel:
    if channel_id not in channels:
        raise HTTPException(
            status_code=404, detail="Channel not found")
    return channels[channel_id]


# Keyword argument example
"""
def intro(**data):
    print("\nData type of argument:", type(data))
    for key, value in data.items():
        print("{} is {}".format(key, value))
        
if __name__ == "__main__":
    intro(Firstname="Jane", Lastname="Doe", Age=22, Phone=1234567890)
    intro(arg1=24)
"""
