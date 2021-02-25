class Weibo:
    def __init__(self):
        self.id = ''
        self.user_id = ''
        self.title = ''
        self.content = ''
        self.publish_time = ''

    def __str__(self):
        """打印一条微博"""
        result = self.content + '\n'
        result += self.title + '\n'
        result += u'发布时间：%s\n' % self.publish_time
        return result
