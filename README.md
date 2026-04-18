# Github CI Sandbox

## Python application

### Install dependencies

To install dependencies you will need to use the `uv`. Read the [installation guide](https://docs.astral.sh/uv/getting-started/installation/).

```bash
uv sync --frozen
```

### Launch the application

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 5000
```

```bash
curl http://0.0.0.0:5000/notes/
#[{"id": 1, "title": "My Note", "text": "..."}, {...}, ...]

curl http://0.0.0.0:5000/math/square/4
# {"message":16}

curl http://0.0.0.0:5000/math/cube/4.1
# {"message":68.92099999999998}

curl http://0.0.0.0:5000/math/sqrt/4
# {"message":2.0}
```
