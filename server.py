from api.app.app import create_app
import os
app = create_app()
app.run(host='0.0.0.0', port=os.environ['PORT'])