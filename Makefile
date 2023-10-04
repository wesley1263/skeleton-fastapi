COLOUR_GREEN=\033[0;32m
COLOUR_RED=\033[0;31m
COLOUR_BLUE=\033[0;34m
COLOUR_END=\033[0m

run-app:
	@echo "${COLOUR_BLUE}Running app...${COLOUR_END}"
	@aerich upgrade
	@python run.py

run-app-local:
	@echo "${COLOUR_BLUE}Running app in debug mode...${COLOUR_END}"
	@aerich upgrade
	@uvicorn app.main:app --reload

formatter:
	@black .
	@isort .
	@flake8
	@autoflake --remove-all-unused-imports --remove-unused-variables --recursive --in-place --ignore-init-module-imports .

testing:
	@pytest

create_module:
	@read -p "Enter Module Name: " MODULE \
	&& mkdir ./app/modules/$${MODULE} \
	&& mkdir ./tests/$${MODULE} \
	&& echo '' > ./app/modules/$${MODULE}/__init__.py \
	&& echo '' > ./app/modules/$${MODULE}/router.py \
	&& echo '' > ./app/modules/$${MODULE}/model.py \
	&& echo '' > ./app/modules/$${MODULE}/repository.py \
	&& echo '' > ./app/modules/$${MODULE}/schema.py \
	&& echo '' > ./app/modules/$${MODULE}/usecase.py \
	&& echo '' > ./tests/$${MODULE}/__init__.py \
	&& echo '' > ./tests/$${MODULE}/conftest.py \
	&& echo '' > ./tests/$${MODULE}/test_model.py \
	&& echo '' > ./tests/$${MODULE}/test_router.py \
	&& echo '' > ./tests/$${MODULE}/test_schema.py \
	&& echo "$(COLOUR_GREEN)#### MODULE $(MODULE) HAS BEEN CREATED ####$(COLOUR_END)" \
	&& echo "$(COLOUR_RED)#### DONT'T FORGET THAT ADD THIS MODULES IN app/config/settings.py ####$(COLOUR_END)"

makemigrations:
	@read -p "set your name migration: " MIGRATION \
	&& aerich migrate --name $${MIGRATION}

migrate:
	@aerich upgrade

init_db:
	@aerich init-db
