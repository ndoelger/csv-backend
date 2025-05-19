# Client CSV Uploader

`Client CSV Uploader` contains a boilerplate template in which clients can upload/edit their csv data on their own

- List all objects in a user's 
- Post
- Put

## How to start

There are two ways. First way is use [`cookiecutter`](https://github.com/audreyr/cookiecutter) template (it located in [different repository](https://github.com/xen/flask-ptc)):

    cookiecutter https://github.com/xen/flask-ptc.git

The second way is to manually clone this repository and change it later by own. Project is ready to run (with some requirements). You need to clone and run:

```sh
$ mkdir Project
$ cd Project
$ git clone git@github.com:xen/flask-project-template.git .
$ make
$ make run
```

Open http://127.0.0.1:5000/, customize project files and **have fun**.

If you have any ideas about how to improve it [Fork project](https://github.com/xen/flask-project-template/fork) and send me a pull request.

## Requirements

If you never worked with python projects then the simplest way is run project inside Docker. Follow instruction [how to install Docker in your OS](https://docs.docker.com/installation/).

If you familiar with web development then you need Python and Node.js:
- Recent Python supported version with SQLite library (usually it is included) 
- Working `virtualenv` command, a name can vary, so you can change it inside `Makefile`
- `make`
- [`bower`](http://bower.io/), if you already have `node.js` with `npm` then run this command:

```sh
npm install -g bower
```

## Included modules support

- [`Flask`](http://flask.pocoo.org/) & [`Werkzeug`](http://werkzeug.pocoo.org/) — base for everything.
- [`Flask`](http://flask.pocoo.org/) & [`Werkzeug`](http://werkzeug.pocoo.org/) — base for everything.
- [`Flask`](http://flask.pocoo.org/) & [`Werkzeug`](http://werkzeug.pocoo.org/) — base for everything.
- [`Flask`](http://flask.pocoo.org/) & [`Werkzeug`](http://werkzeug.pocoo.org/) — base for everything.