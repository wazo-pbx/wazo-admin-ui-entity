install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/entity.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-entity
	rm /etc/wazo-admin-ui/conf.d/entity.yml
	systemctl restart wazo-admin-ui
