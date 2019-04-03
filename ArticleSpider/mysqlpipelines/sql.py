import mysql.connector
from ArticleSpider import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB,
                              port=MYSQL_PORT)
cur = cnx.cursor(buffered=True)


class Sql:

    @classmethod
    def insert_dd_name(cls, title, datetime, praise_num):
        insert_sql = """
                    insert into article_spider(title,datetime,praise_num)
                    value (%(title)s,%(datetime)s,%(praise_num)s)
                """
        value = {
            'title': title,
            'datetime': datetime,
            'praise_num': praise_num,
        }
        cur.execute(insert_sql, value)

        # cur.execute("INSERT INTO movie(`name`,`star`,`movieinfo`,`quote`) VALUES ('%s','%s','%s','%s')",(name,star,movieinfo,quote))
        cnx.commit()
