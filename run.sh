#!/bin/bash

docker-compose build

docker-compose run -e HOST=selenium_firefox tests

function cleanup {
    set +e
    if [[ -d reports ]] ; then
        docker-compose run tests chmod 777 reports
    fi
    docker-compose stop selenium_firefox
}
trap cleanup EXIT

