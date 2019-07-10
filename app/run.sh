#!/bin/bash

gunicorn3 -w 15 -b 0.0.0.0:8080 app:app --daemon --name fitness
