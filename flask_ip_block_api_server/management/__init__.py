def create_app():
    from flask import Flask
    from flask_cors import CORS
    from apps.middle import swagger
    app = Flask(__name__)
    CORS(app)
    app.config['SWAGGER'] = {
        'title': 'API DOC',
        'uiversion': 2
    }
    swagger.init_app(app)
    from apps import (main_page_api, detection_violation_page_api, laboratory_page_api, admin_page_api,
                      mitigation_page_api, investigation_page_api)
    app.register_blueprint(main_page_api)
    app.register_blueprint(detection_violation_page_api)
    app.register_blueprint(laboratory_page_api)
    app.register_blueprint(admin_page_api)
    app.register_blueprint(mitigation_page_api)
    app.register_blueprint(investigation_page_api)
    return app
