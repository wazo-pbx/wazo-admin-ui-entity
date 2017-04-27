# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask import jsonify, request
from wazo_admin_ui.helpers.classful import LoginRequiredView


class EntityListingView(LoginRequiredView):

    def list_entities(self):
        params = extract_select2_params(request.args)
        entities = self.service.list(**params)
        results = [{'id': entity['name'], 'text': entity['name']} for entity in entities['items']]
        return jsonify(build_select2_response(results, entities['total'], params))
