from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from django.conf import settings
import traceback
import logging
import requests, json

logger = logging.getLogger(__name__)


def send_slack_chan_message(end_point, status_code, method, err_message):
    url = 'https://hooks.slack.com/services/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'

    summary = f'*{timezone.localtime().strftime("%Y-%m-%d %H:%M:%S")} 버그 리포트*\n' \
        f'>*end_point*: `{end_point}`\n' \
        f'>*method*: `{method}`\n' \
        f'>*status_code*: `{status_code}`\n' \
        f'```{err_message}```'
    data = {
        'text': summary
    }

    response = requests.post(url, data=json.dumps(data))
    if response.status_code == 200:
        print('Send Bug Report Success')
    else:
        print('Send Bug Report Failed')


class LoggingMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response_data = {}
        if hasattr(response, "data"):
            response_data = dict(response.data) if response.data is not None else {}
        response_message = f'{request.environ.get("REMOTE_ADDR")}  ' \
            f'{request.user.id}  ' \
            f'{request.method}  ' \
            f'{request.path}  ' \
            f'{request.environ}  ' \
            f'{dict(request.POST) if request.POST else {}}  ' \
            f'{response.status_code}  ' \
            f'{response.template_name if hasattr(response, "template_name") else None}  ' \
            f'{response.exception if hasattr(response, "exception") else False}  ' \
            f'{response_data}'
        logger.info(response_message)
        except_status_code = [401, 403, 500]
        except_end_point = ['/', '/favicon.ico']
        if settings.SETTINGS_LEVEL == 'production':
            if not 200 <= int(response.status_code) < 400 and \
                    int(response.status_code) not in except_status_code and request.path not in except_end_point:
                send_slack_chan_message(request.path, response.status_code, request.method, response_data)
        return response

    def process_exception(self, request, exception):
        err_message = '\t'.join(traceback.format_exc().split('\n'))
        response_message = f'{request.environ.get("REMOTE_ADDR")}  ' \
            f'{request.user.id}  ' \
            f'{request.method}  ' \
            f'{request.path}  ' \
            f'{request.environ}  ' \
            f'{dict(request.POST) if request.POST else {}}  ' \
            f'{err_message}'
        logger.info(response_message)
        if settings.SETTINGS_LEVEL == 'production':
            send_slack_chan_message(request.path, 500, request.method, traceback.format_exc())
