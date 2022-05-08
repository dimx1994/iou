import logging
import os

workers = os.getenv('GUNICORN_WORKERS', '2')
timeout = os.getenv('GUNICORN_TIMEOUT', '2000')
threads = os.environ.get('GUNICORN_THREADS', '2')
bind = f"0.0.0.0:{os.getenv('GUNICORN_PORT', '8000')}"
worker_class = 'uvicorn.workers.UvicornWorker'

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s [%(name)s] %(levelname)s: %(message)s'
)
