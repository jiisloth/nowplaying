#!/bin/bash

source venv/bin/activate

python3 WebServer.py 8000 &

python3 GetData.py &
