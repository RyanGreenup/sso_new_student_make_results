check:
    ruff format **/*.py
    ruff check chalsedony --fix
    # pyright chalsedony
    basedpyright chalsedony
    ruff format chalsedony/**/*.py
    mypy --strict chalsedony | grep -v rc | grep -v missing-import | grep -v 'missing library stubs' | grep -v 'ignore'
    # vulture chalsedony/*.py
    check-mypy

check-mypy:
    mypy --strict chalsedony | grep -v rc | grep -v missing-import | grep -v 'missing library stubs' | grep -v 'ignore'

run:
    # uv run -- python ./sso_new_student/main.py
    uv run sso &

build:
    uv build

install:
    uv tool install . --force
