data = [('himakar', 16), ('swagath', 25), ('venkat', 24),
        ('rahul', 12), ('sunil', 16), ('bharathc', 30)]

from sqlalchemy import create_engine, text
drop_t = "drop table if exists people"
create_t = """
create table if not exists people( name string, age int)
"""
insert_t = "insert into people values(:name, :age)"
eng = create_engine("sqlite:///./people.db")
with eng.connect() as conn:
    conn.execute(text(drop_t))
    conn.execute(text(create_t))
    for name, age in data:
        conn.execute(text(insert_t), dict(name=name, age=age))
    conn.commit()