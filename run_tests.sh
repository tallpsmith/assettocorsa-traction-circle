#!/bin/bash
pushd apps/tests
    for i in *.py
    do
        PYTHONPATH=../python/traction-circle python3.4 -m unittest ${i/.py/}
    done
popd
