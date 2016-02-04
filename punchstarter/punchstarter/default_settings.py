import os
import cloudinary

DEBUG=True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR + "/app.db"


cloudinary.config(
  cloud_name = "fvo2006",
  api_key = "153618543686195",
  api_secret = "gso1RKZn740oV1RagH8begwo2TY"
)
