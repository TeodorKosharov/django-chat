# Django chat

Django chat is a real-time chat application, which is using <b>Django channels</b> and <b>WebSockets</b> for receiving updates immediately.
The application is offering a fully responsive design.

## Installation 

To start the application, recent versions of Python, Django and Docker will be needed. <br>
Install all the required dependencies:

```pip install -r requirements.txt```

Channel layer (kind of communication system) needs to be enabled. We will use a channel layer that uses 
<b>Redis</b> as its backing store. To start a Redis server on port 6379, run the following command:

```docker run -p 6379:6379 -d redis:5```


## Usage/Examples

### Non-authenticated user

A not logged-in user can not enter any chat rooms or create a new one.


### Authenticated user

A logged-in user is able to enter any chat room or create a new one. Settings can be accessed by
authenticated users where they can manage their chat rooms and change the color theme of the whole application.


### Chat room

Once a chat room is created, it can be accessed by every authenticated user. New messages will appear/disappear immediately.
The message can be deleted only by its sender.



