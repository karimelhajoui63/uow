import pretty_errors
from fastapi import FastAPI

from model import Item
from use_case import UseCase

pretty_errors.configure(
    separator_character="*",
    filename_display=pretty_errors.FILENAME_EXTENDED,
    line_number_first=True,
    display_link=True,
    lines_before=5,
    lines_after=2,
    line_color=pretty_errors.RED + "> " + pretty_errors.default_config.line_color,
    code_color="  " + pretty_errors.default_config.line_color,
    truncate_code=True,
    display_locals=True,
)

app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    UseCase.method(item=item)
    return item
