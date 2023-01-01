query_kwargs = """
SELECT database() as server, login 
FROM mt4_trades 
WHERE login in ({logins}) and reg_date <= '{search_date}'
LIMIT 5
"""

query_args = """
SELECT database() as server, login 
FROM mt4_trades 
WHERE login in ({}) and reg_date <= '{}'
LIMIT 5
"""

def get_data_args(query: str, *args: tuple):
    print(f"args: {args}")
    query = query.format(*args)
    print(query)

def get_data_kwargs(query: str, **kwargs: dict):
    print(f"kwargs: {kwargs}")
    print(kwargs.get('logins'))
    query = query.format(**kwargs)
    print(query)

get_data_args(query_args, 123, "2023-01-01")
get_data_kwargs(query_kwargs, logins = 123, search_date = "2023-01-01")

# output: 
# args: (123, '2023-01-01')
# kwargs: {}

# get_data_args(query_args, 123, "2023-01-01", key = 1, value = 2)
# output: (123, '2023-01-01')
# kwargs: {'key': 1, 'value': 2}

# get_data(query, 123, key = 2, '2023-01-01')
# # SyntaxError: positional argument follows keyword argument

# kwargs沒有字串的變數時
get_data_kwargs(query_kwargs, logins = 1, search_date = 3)
print(query_kwargs.format(logins = 1, search_date = 3))