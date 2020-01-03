from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    if response is not None:
        data = response.data
        response.data = {}
        errors = []
        for feild, value in data.items():
            errors.append("{}:{}".format(feild," ".join(value)))
            response.data['errors'] = errors
            response.data['status'] = response.status_code
            response.data['exception'] = str(exc)
        return response