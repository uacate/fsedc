import pydantic
from typing import List, Annotated
from annotated_types import Len

from pydantic import BaseModel, HttpUrl

class DCAT(BaseModel):

    conformsTo: HttpUrl
    dataset: Annotated[list[dict], Len(min_length=1)]
