from rel_one_to_many import User, Article, session

if __name__ == "__main__":
    article = session.get(Article, 1)
    article.content = "Very important content for the article"
    session.add(article)
    session.commit()
