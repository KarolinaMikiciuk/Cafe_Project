import pandas
from sqlalchemy import create_engine

my_conn = create_engine("mysql+mysqldb://root:TwentyLeagues!?3@localhost/cafe")

def commit_to_db(category):
    df = pandas.read_csv(f"{category}_list.csv",sep=',',quotechar='\'',encoding='utf8')
    df.to_sql(con=my_conn, name=f'{category}', if_exists='replace')


