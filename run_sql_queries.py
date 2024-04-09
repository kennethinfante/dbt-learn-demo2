#%%
import duckdb
import pandas as pd

#%%
q = '''
select * from fct_customer_orders
'''

with duckdb.connect("data/dbt_learn.db") as con:
    display(con.sql(q).df())

#%%
q1 = '''
create or replace table customers as 
    select * from
    read_csv_auto(
        'data/customers.csv',
        normalize_names=True
    )
'''

q2 = '''
create or replace table orders as 
    select * from
    read_csv_auto(
        'data/orders.csv',
        normalize_names=True
    )
'''

q3 = '''
create or replace table payments as 
    select * from
    read_csv_auto(
        'data/payments.csv',
        normalize_names=True
    )
'''

with duckdb.connect("data/dbt_learn.db") as con:
    con.sql(q1)
    con.sql(q2)
    con.sql(q3)

#%%

#%%