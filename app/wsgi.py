from app import app as application

# do some production specific things to the app
app.config['DEBUG'] = False

if __name__ == "__main__":
    app.run()