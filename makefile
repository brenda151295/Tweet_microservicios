# Microservices Project Make File

VIRTUALENV = $(shell which virtualenv)

clean:
	rm -fr microservices.egg-info
	rm -fr venv
	rm -fr /tmp/test.db

venv:
	$(VIRTUALENV) venv

createdb:
	. venv/bin/activate; python  services/persistence/init_db.py

install: clean venv
	. venv/bin/activate; python setup.py install
	. venv/bin/activate; python setup.py develop

launchuser:
	venv/bin/python services/user.py

launchtweet:
	venv/bin/python services/tweet.py

shutdown:
	ps -ef | grep "services/user.py" | grep -v grep | awk '{print $$2}' | xargs kill || echo "users service is not running"
	ps -ef | grep "services/tweet.py" | grep -v grep | awk '{print $$2}' | xargs kill || echo "tweets service is not running"
