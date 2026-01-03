from pydantic import BaseModel

class SuperHero(BaseModel):
    name: str
    alias: str | None = None
    superpower: str | None = None
    age: int | None = None

class CapedHero(SuperHero):
    cape_color: str

flying_dick = CapedHero(
    name="Flying Dick",
    cape_color="Green"
)

response = chat(
    messages = [
        {}
    ]
    format=CapedHero.model_json_schema()
)