<h1 align="center">Guess It</h1>

A micro web project using the <a href="https://flask.palletsprojects.com/en/2.3.x/">flask</a> web framework for python.

You upload an image and get a list of 10 guesses about what the picture contains.

We are using the pretrained <a href="https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet50">Resnet50</a> for classification.

Project includes both the server and client components.

## Install and Run

### Client

To run the client you don't need to require any installation. Just open the `index.html` file in your browser.

---

### Server

The server is a flask app that uses a tensorflow model to make predictions.

To install the server, you need to install the requirements in a virtual environment.

It is suggested that you create a virtual environment using the python `venv` module.

```bash
python3 -m venv venv
```

Then activate the virtual environment

```bash
source venv/bin/activate
```

Then install the requirements from the 'requirements.txt' file.

```bash
pip install -r requirements.txt
```

To start the server, navigate to the `server` directory and use the `flask run` command.

```bash
cd server
flask run
```

The server will start on port 5000 by default. Ensure that no other process is using that port.

----