"""
    Discord : Thibô#0001
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 10/02/2021
"""

# Import neded packages
from flask import Flask, redirect, flash


# Import personal modules



# Definition of the app
def create_app() -> Flask:
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = '29FTh4Swfr3DuMlNRcQcZxCk7IFBMooP'

    # Import blueprints
    

    # Error 404 handler
    @app.errorhandler(404)
    def pageNotFound(error):
        flash("HTTP 404 Not Found", "Red_flash")
        return redirect('/')

    return app


# Start app if file is not imported
if __name__ == "__main__":
    app = create_app()
    app.run(debug=1, host='0.0.0.0', port=5454)
