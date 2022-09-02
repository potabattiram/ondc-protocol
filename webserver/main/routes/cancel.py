from flask import g, request
from flask_expects_json import expects_json
from flask_restx import Namespace, Resource, reqparse
from jsonschema import validate

from main.service.common import add_bpp_response, get_bpp_response_for_message_id, bpp_post_call
from main.utils.schema_utils import get_json_schema_for_given_path, get_json_schema_for_response

cancel_namespace = Namespace('cancel', description='Cancel Namespace')


@cancel_namespace.route("/cancel")
class BPPCancel(Resource):

    def post(self):
        request_payload = request.get_json()
        return bpp_post_call('cancel', request_payload)


@cancel_namespace.route("/v1/on_cancel")
class AddCancelResponse(Resource):
    path_schema = get_json_schema_for_given_path('/on_cancel')

    @expects_json(path_schema)
    def post(self):
        resp = add_bpp_response(g.data, request_type='on_cancel')
        response_schema = get_json_schema_for_response('/on_cancel')
        validate(resp, response_schema)
        return resp


@cancel_namespace.route("/response/v1/on_cancel")
class GetCancelResponseForMessageId(Resource):

    def create_parser_with_args(self):
        parser = reqparse.RequestParser()
        parser.add_argument("messageId", dest='message_id', required=True)
        return parser.parse_args()

    def get(self):
        args = self.create_parser_with_args()
        return get_bpp_response_for_message_id(request_type='on_cancel', **args)

