#!./venv/bin/python
# Install uv:
# curl -LsSfk https://astral.sh/uv/install.sh | sh && source $HOME/.cargo/env
# Setup python env:
# uv venv && uv pip install duckdb
import duckdb

# Double quotes
duckdb.sql("""
SELECT *
FROM foo;
""")
# Single quotes
duckdb.sql("""
    SELECT *
    FROM foo;
    """)

# f-string
x = "foo"
duckdb.execute(f"""
    SELECT *
    FROM foo
    WHERE x = {x};
""")

# Single line non-multiline strings are not supported
duckdb.sql(" SELECT * FROM foo WHERE x = 'bar'; SELECT * FROM bar; ")
duckdb.sql(""" SELECT * FROM foo WHERE x = 'bar'; SELECT * FROM bar; """)

duckdb.aggregate("""SELECT * FROM foo;""")
# Normal multi-line is not highlighted
x = """
This will not SELECT
"""
x = f"FOO"
x = f"""FOO"""

# Known error: Strings after SQL are not syntax highlighed correctly
duckdb.execute(
    f"""
SELECT *
FROM $1;
""",
    "(select * from char)",
)

# Known error: A newline after a string is not syntax highlighed correctly
duckdb.execute(
    f"""
    SELECT *
    FROM $1;
    """
)
