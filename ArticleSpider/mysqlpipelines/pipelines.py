from .sql import Sql
from ArticleSpider.items import ArticlespiderItem

class articlesql(object):

    def process_item(self, item, spider):
        if isinstance(item, ArticlespiderItem):
            # ret = Sql.select_name(name)
            # if ret[0] == 1:
            #     print('已经存在了')
            # else:

            title=item['title']
            datetime=item['datetime']
            praise_num=item['praise_num']
            print("sql",title)
            Sql.insert_dd_name(title,datetime,praise_num)
            print('开始存小说标题')
