import connexion
import flask
import glob
import os


def handle_cli():
    app = init_app()
    print('Starting local server on http://localhost:8000')
    app.run(port=8080, debug=True)


def init_app():
    specification_dir_path = os.path.join(os.getcwd(), 'swagger')
    app = connexion.FlaskApp(
        __name__,
        specification_dir =specification_dir_path,
        server='tornado'

    )
    api_files = glob.glob(os.path.join(specification_dir_path, '*.yaml'))
    for api_file in api_files:
        try:
            app.add_api(
                    api_file,
                    strict_validation=True,
                    validate_responses=True,
                    options={"swagger_ui": False}
                )
        except Exception as e:
            print(e)
    return app
