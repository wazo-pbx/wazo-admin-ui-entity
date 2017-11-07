# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.plugin import create_blueprint
from wazo_admin_ui.helpers.destination import register_listing_url

from .service import EntityService
from .view import EntityListingView

entity = create_blueprint('entity', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        EntityListingView.service = EntityService()
        EntityListingView.register(entity, route_base='/entities_listing')

        register_listing_url('available_entity', 'entity.EntityListingView:list_entities')

        core.register_blueprint(entity)
