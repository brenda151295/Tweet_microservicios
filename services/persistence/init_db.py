if __name__ == "__main__":
    from datetime import datetime
    from models import db, User, Tweet

    db.create_all()

    u = User(username='johann2357', email='johann2357@gmail.com')
    db.session.add(u)
    db.session.commit()

    tweet = Tweet(
        content="My first tweet!", author=u,
        pub_date=datetime.utcnow()
    )
    db.session.add(tweet)
    db.session.commit()

    tweet = Tweet(
        content="My second tweet!!", author=u,
        pub_date=datetime.utcnow()
    )
    db.session.add(tweet)
    db.session.commit()

    tweet = Tweet(
        content="My third tweet!!!", author=u,
        pub_date=datetime.utcnow()
    )
    db.session.add(tweet)
    db.session.commit()

    u = User(username='tester', email='tester@gmail.com')
    db.session.add(u)
    db.session.commit()

    tweet = Tweet(
        content="Test tweet!", author=u,
        pub_date=datetime.utcnow()
    )
    db.session.add(tweet)
    db.session.commit()

    tweet = Tweet(
        content="Test twitter!", author=u,
        pub_date=datetime.utcnow()
    )
    db.session.add(tweet)
    db.session.commit()
