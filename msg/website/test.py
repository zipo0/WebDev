class news_publication:
    def __init__(self, title, sub, cont):
        self.title = title
        self.sub = sub
        self.cont = cont

post = [news_publication("a","a","a")]
post.append(news_publication('b','b','b'))
for index in post:
    print(index.title)