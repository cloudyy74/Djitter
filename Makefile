lint:
	uv run ruff check src

type_check:
	uv run mypy src

format:
	uv run ruff format src

run:
	uv run python3 src/manage.py runserver
