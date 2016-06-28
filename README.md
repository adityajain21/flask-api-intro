# flask-api-intro
This is a simple **flask api** program.

You should have Flask installed for running this.

To run:
$ cd flask-api-intro
$ python app.py &
$ curl -i -H "Content-Type: application/json" -X POST -d '{"name":"abcd","ph_no":"123"}' http://localhost:5000/tasks
