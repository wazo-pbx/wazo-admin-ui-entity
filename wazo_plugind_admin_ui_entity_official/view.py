# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask import jsonify, request
from wazo_admin_ui.helpers.classful import LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response


class EntityListingView(LoginRequiredView):

    def list_entities(self):
        params = extract_select2_params(request.args)
        entities = self.service.list(**params)
        results = [{'id': entity['id'], 'text': entity['display_name']} for entity in entities['items']]
        return jsonify(build_select2_response(results, entities['total'], params))
