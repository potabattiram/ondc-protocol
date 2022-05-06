from flask import g, request
from flask_expects_json import expects_json
from flask_restx import Namespace, Resource, reqparse

from main.service.search import add_search_catalogues, get_catalogues_for_message_id
from main.utils.schema_utils import get_json_schema_for_given_path

search_namespace = Namespace('search', description='Search Namespace')


@search_namespace.route("/v1/on_search")
class AddSearchCatalogues(Resource):
    path_schema = get_json_schema_for_given_path('/on_search')

    @expects_json(path_schema)
    def post(self):
        return add_search_catalogues(g.data)


@search_namespace.route("/response/v1/on_search")
class GetCataloguesForMessageId(Resource):

    def create_parser_with_args(self):
        parser = reqparse.RequestParser()
        parser.add_argument("messageId", dest='message_id', required=True)
        return parser.parse_args()

    def get(self):
        args = self.create_parser_with_args()
        return get_catalogues_for_message_id(**args)

