from typing import Any, cast

from db.pokemon import PokemonTable
import psycopg
from psycopg import sql
from psycopg.rows import dict_row

DB_URL = "postgresql://admin:admin@localhost:5432/pokemon_db"


class DatabaseClient:
    def __init__(self):
        self.conn = psycopg.connect(DB_URL)

    def _execute(
        self, query, params=None, fetch="one"
    ) -> dict[str, Any] | list[dict[str, Any]] | None:
        with self.conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(query, params)
            if fetch == "one":
                results = cursor.fetchall()
                if len(results) == 0:
                    return []
                if len(results) > 1:
                    raise ValueError(f"Expected one result, got {len(results)}")
                return results[0]
            elif fetch == "all":
                return cursor.fetchall()

    def count_all_entries(self, table_name):
        result = self._execute(
            sql.SQL("SELECT COUNT(*) FROM {}").format(sql.Identifier(table_name))
        )
        return cast(dict, result)["count"] if result is not None else 0

    def select(
        self, table_name, limit=None, offset=None, order_by=None, fetch="all", **kwargs
    ):
        query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))

        if kwargs:
            where = sql.SQL(" WHERE {}").format(
                sql.SQL(" AND ").join(
                    sql.SQL("{} = {}").format(sql.Identifier(k), sql.Placeholder())
                    for k in kwargs
                )
            )
            query = query + where

        if order_by is not None:
            query = query + sql.SQL(" ORDER BY {}").format(sql.Identifier(order_by))

        if limit is not None:
            query = query + sql.SQL(" LIMIT {}").format(sql.Literal(limit))

        if offset is not None:
            query = query + sql.SQL(" OFFSET {}").format(sql.Literal(offset))

        return self._execute(
            query, list(kwargs.values()) if kwargs else None, fetch=fetch
        )

    def close(self):
        self.conn.close()


class Database:
    def __init__(self, client: DatabaseClient):
        self.pokemon = PokemonTable(client)
