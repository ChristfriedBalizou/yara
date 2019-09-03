# Yara
Yara - Yet Another Rest API


## Context

Now days they are lot of rest API application out there
the question is always what to use.

In this demo I am focussing on:
* Django (DRF)
* FastAPI
* Flask
* Falcon

Each one of them are very use and have their own use case. 
The reason why I am implementing Yara (Yet Another Rest API)
Is to show that switching from one to another because it's new
or become a brand, better or faster is not enough reason the change 
your framework.

Choosing a framework should be base on a strong.

In this example we are going to implement a Rest API
that do some simple computations and return JSON response.

In our example I can state that if we want to make simple
and just have basic rest maybe we don't even need a framework.
But if you think you might need to manage configurations, 
Databases, schedules, swagger, Admin interfaces, ... Maybe you should
Agnostic select a Framework to do so with less code writing to do
so.


We are going to use built-in python http.server
https://docs.python.org/3/library/http.server.html#module-http.server

## Getting started

Easy to start with:

1 - Clone the repo:

    ```
    git clone https://github.com/ChristfriedBalizou/yara.git && cd yara
    ```

2 - Run the server:
     
    ```
    python serve [port] [host]
    ```
