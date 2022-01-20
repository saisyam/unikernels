# Sentiment analysis with FastAPI and Vader Unikernel
I used Ubuntu 20.04 to build this nanos unikernel. Refer to [OPS City](http://ops.city) for the tool to build the unikernel. This application is built using FastAPI and Vader Sentiment Analyzer. Follow the below steps to build the unikernel.

## Installing OPS tool
Run the following command to install `ops` tool to build unikernel images
```
$ curl https://ops.city/get.sh -sSfL | sh
```
## Setup Python virtual environment
```
$ python3 -m venv .venv --prompt nanos
$ source .venv/bin/activate
$ (nanos): pip install --upgrade pip
$ (nanos): pip install -r requirements.txt
```

## Run the application
To run the application as unikernel, run the following command:
```
$ ops pkg load python_3.8.6 -c config.json -p 8000
```
Your FastAPI application will be up and running as unikernel. Press `Ctrl+C` to terminate the process.

**Note:** As I am running this on Linux, the `/usr/lib64` folder is mapped to local `/usr/lib/x86_64-linux-gnu` folder in the `config.json` file. Because to run this program you need `libgcc_s.so.1` and `libz.so.1`. Refer to this [link](https://github.com/nanovms/ops-examples/tree/master/python/python3.8) for more information.  
