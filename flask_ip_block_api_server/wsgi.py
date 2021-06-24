from management import create_app
import gevent.monkey

gevent.monkey.patch_all()
app = create_app()
