from app import app

# todo do you need threaded=True? Maybe it solves the performacne issue on local server?
app.run(debug=True, threaded=True)
