install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check --fix brain_games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calculate

brain-gcd:
	uv run brain-gcd

brain-prog:
	uv run brain-progression
