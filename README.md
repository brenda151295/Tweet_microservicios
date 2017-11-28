# Twitting - (Extremely Simplified) Example of Microservices in Python


Overview
========

Twitting is an example project which demonstrates the use of microservices for a fictional simple twitter.
The Twitting backend is powered by 2 microservices, all of which happen to be written in Python using
Flask.

 * Tweet Service: Provides tweets information and allows new tweets creation.
 * Users Service: Provides users information.

Requirements
===========

* Python 2.7
* Works on Linux, Windows, Mac OSX and (quite possibly) BSD.

Install
=======

The quick way is use the provided `make` file.

<code>
$ make install
$ make createdb
</code>

Starting and Stopping Services
==============================

To launch the services:

<code>
$ make launch
</code>

To stop the services:

<code>
$ make shutdown
</code>


APIs and Documentation
======================

## Tweet Service (port 5001)

This service is used to get information about tweets. It provides the tweet
content, creation date and the user id. Also filter tweets by user

To lookup all tweets in the database, hit: `http://127.0.0.1:5001/tweets`


    GET /tweets
    Returns a list of all tweets.

To lookup a list of tweets by its `username`:

    GET /tweets/johann2357
    Returns the list of tweets of johann2357.


## User Service (port 5000)

This service returns information about the users.

To get a list of all the users in the system, hit: `http://127.0.0.1:5000/users`

    GET /users
    Returns a list of all users in the database.

To lookup information about a user:

    GET /users/johann2357


TODO
======================

## Features

Implement user creation and login

## Tests

Implement all the tests :(
