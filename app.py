from flask import Flask
from views import *

import translators as ts

# Configure Flask
app = Flask(__name__)

# Configure Urls
app.add_url_rule('/translate/<string:from_lang>/<string:target_lang>/<string:provider>',
                 "translate",
                 translate,
                 methods=["GET", "POST"],
                 )

app.add_url_rule('/translate/<string:target_lang>/',
                 "translate",
                 translate,
                 methods=["GET", "POST"],
                 defaults={"from_lang": None, "provider": "google"}
                 )

app.add_url_rule('/translate/<string:from_lang>/<string:target_lang>',
                 "translate",
                 translate,
                 methods=["GET", "POST"],
                 defaults={"provider": None}
                 )
if __name__ == '__main__':
    app.run(host='0.0.0.0')
