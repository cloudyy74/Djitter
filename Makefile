lint:
	uv run ruff check src
	uv run pyrefly check src

format:
	uv run ruff format src

run:
	uv run python3 manage.py runserver
