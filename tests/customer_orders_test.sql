{{ config(severity='warn') }}
select
    customer_id,
    sum(customer_lifetime_value) as total_cltv
from 
    {{ ref('fct_customer_orders') }}
group by customer_id
having total_cltv < 0