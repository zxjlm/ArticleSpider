from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__name__)))

execute(['scrapy', 'crawl', 'lagou'])
# execute(['scrapy', 'crawl', 'jobbole'])
