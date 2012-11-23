# jsonp

A JSONP proxy

## Install

    virtualenv .
    . bin/activate
    pip install -r requirements.txt

## Running
Start the server

    bottle.py jsonp

See `bottle.py --help` for more options (port, server, ...).

## Query

Set the callback and url params.

    curl -s 'http://localhost:8080/?callback=grid&url=http://a.tiles.mapbox.com/v3/mapbox.geography-class.json'

## License
Copyright (c) 2012 Frédéric Junod <frederic.junod@gmail.com>

Released under the [WTFPL version 2](http://sam.zoy.org/wtfpl/).
