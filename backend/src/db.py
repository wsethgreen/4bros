from sqlalchemy import create_engine
from db_scripts import create_db_tables, engine
from data import (
    data,
    def_stats,
    kicking_stats,
    player_info,
    commits,
    return_stats,
    off_stats,
    week_year,
    team_info
    )
from db_scripts import (
    create_db_tables,
    insert_data
    )


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

create_db_tables(data)
