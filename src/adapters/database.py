from typing import cast
from typing import Any
from typing import Optional
from typing import Union
from typing import Mapping

from databases import Database as _Database

from sqlalchemy import ClauseElement

from sqlalchemy.dialects import mysql

DIALECT = mysql.dialect()

Query = Union[str, ClauseElement]

Row = dict[str, Any]

class Database:
    def __init__(self, url: str) -> None:
        self._database = _Database(url)

    async def connect(self) -> None:
        await self._database.connect()

    async def disconnect(self) -> None:
        await self._database.disconnect()

    def _compile(self, clause_element: ClauseElement) -> str:
        compiled = clause_element.compile(dialect=DIALECT,
                                          compile_kwargs={"literal_binds": True})
    
        return str(compiled)

    async def execute(self, query: Query) -> int:
        if isinstance(query, ClauseElement):
            query = self._compile(query)
        
        rec_id = await self._database.execute(query)
        return cast(int, rec_id)
        
    async def fetch_one(self, query: Query) -> Optional[Row]:
        if isinstance(query, ClauseElement):
            query = self._compile(query)
            
        row = await self._database.fetch_one(query)
        
        return cast(Row, row._mapping) if row else None
    
    async def fetch_all(self, query: Query) -> list[Row]:
        if isinstance(query, ClauseElement):
            query = self._compile(query)
            
        rows = await self._database.fetch_all(query)
        
        return cast(list[Row], [row._mapping for row in rows])