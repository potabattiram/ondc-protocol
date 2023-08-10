import os 
from dotenv import load_dotenv

from main import create_app


app = create_app("dev")


if __name__ == "__main__":
    # if os.getenv("ENV") is not None:
        # flask_s3.create_all(app)
    app.run(host="0.0.0.0", port=9900)

# C:\Users\potab\envs\Scripts\activate.bat
