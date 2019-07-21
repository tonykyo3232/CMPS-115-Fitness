Warning: Please use python `> 3.6`!!

# To setup python libraries
```bash
pip install -r requirements.txt

# If your python3 uses pip3...
#pip3 install -r requirements.txt
```

# 1. Set up data
```
# Parse program/routine description in ../Workout Dataset/ and Save it in ./pickles/
python data_update.py

# If your python is not linked with python3
python3 data_update.py
```

# 2. Run server
```bash
# Default: Run server on port 8080 (http://localhost:8080)
python app.py

# You can specify port (please choose port number 10000 ~ 20000 for debugging)
python app.py 12345 # Run server on port 12345

# If your python is not linked with python3
python3 app.py

# Run server in background
./run.sh
./restart.sh

# You can stop background server by ./stop.sh
```

# Recommendation when running server
* For debug purpose, use `python app.py [port number between 10000 ~ 20000]`
* Otherwise, use `./run.sh` or `./restart.sh`
