import jwt
from flask import Flask
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

app = Flask(__name__)


@app.route('/generatetoken/<u_id>/<time>')
def token_generator(u_id, time):
  
  exp = dt.utcnow() + relativedelta(time=+1)
  
  if u_id:
    token = jwt.encode({"id": u_id, "exp": exp}, str("SECRET_KEY"))
    return {'token': token.decode("UTF-8"), 'id': u_id, 'expire': exp}
  return None    
  
  
if __name__ == "__main__":
  app.run()
