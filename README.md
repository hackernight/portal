Portal
======

A combo hardware software project that allows one to open and close a garage door remotely via rest.  

## Tech Used:
Raspberry Pi
[Flask web microframework](http://www.fullstackpython.com/flask.html)
RPi.GPIO hardware integration
2x Low voltage activated relays rated to 25V (this garage door runs on 16V)
some solder, some wire, and raspi case.

## The Setup:
The RasPi was used just like a server wherein it's plugged in and always on and listening on port 8080 on my internal network.

The hardware uses two pins, and a graound from the RasPi GPIO block that are controlled via rest enpoint to toggle on and off when poked.

## Developing locally:
Through the nifty world of python metaclassing, you can run this in isolation without a raspberry pi attached.  Any call that would hit the hardware layer now just logs.

It is recommended that you use [virtualenv](https://virtualenv.readthedocs.org/en/latest/) and pip. Once you get into your virtual environment, `pip install -r requirements.txt` and you are ready to run.

To run the unit tests (which are the best way to get to know the project anyway) 

      python -m unittest [discover | name of the specific unit test]


Happy coding!
