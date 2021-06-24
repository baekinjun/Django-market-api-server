import re
from ast import literal_eval

Messages = {
    200: "[OK]",
    201: "[Created]",
    202: "[Accepted] Analysis is not Complete",
    400: "[Bad Request] Parameter values are incorrect",
    401: "[Unauthorized] Required Login or API Token",
    403: "[Forbidden] The wrong approach",
    404: "[Not Found] Page Not Found",
    409: "[Conflict] The data already exist",
    412: "[Precondition Failed] Parameter values must be entered",
    413: "[Payload Too Large] Request data below 256MB",
    423: "[Locked] No more requests can be made",
    429: "[Rate Limit] Your API Rate is Limited",
    500: "[Internal Server Error] Unknown error",
    700: "[None of data]"
}


class ResponseConstants:
    DEFAULT_FAILED_MESSAGE = "Your request failed"
    DEFAULT_SUCCESS_MESSAGE = 'Your request is successful'


class ResponseHandler(Exception):
    status_code = 500

    def __init__(self, status_code=None):
        Exception.__init__(self)
        if status_code is not None:
            self.status_code = status_code

        if self.status_code not in [200, 201, 700]:
            self.response_result = ResponseConstants.DEFAULT_FAILED_MESSAGE
        else:
            self.response_result = ResponseConstants.DEFAULT_SUCCESS_MESSAGE

    def payload(self, payload):
        res = payload
        return res, self.status_code

    def response(self):
        return self.status_code, self.status_code

    def validator_response(self, error):
        res = {'error_message': None}

        res['error_message'] = literal_eval(error)
        return res, self.status_code


class ExecuteError(Exception):
    status_code = 500
    message = """[Execute Error] Please check SP or verify parameters, 
        Query: {}, 
        Error Code: {}, 
        Message: {}"""

    def __init__(self, query, error):
        Exception.__init__(self)
        query = query.splitlines()[0]
        try:
            code, error_message = literal_eval(str(error))
            self.status_code = self.get_status_code(int(code))
            self.message = self.message.format(query, code, error_message)
            print(self.message)
        except Exception as ex:
            raise ResponseHandler(500)

    def to_dict(self):
        rv = {"status": self.status_code, "result": "failed", "message": Messages[self.status_code]}
        return rv

    # need to add database execute error code
    def get_status_code(self, error_code):
        if error_code == 1062:
            return 409

        return 500

    def pretty_message(self, message):
        return re.sub("[\t\n\s]+", "", message)
