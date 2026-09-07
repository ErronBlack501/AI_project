# ai-model

Python package that will provide the foundation for the project's machine learning components. It is built with `uv` and currently exposes a minimal CLI command.

## Current Status

The `ai-model` entry point prints a demo message. No model, dataset, or training pipeline has been implemented yet.

## Prerequisites

- Python `3.14`, specified by `.python-version` and required by the project;
- [uv](https://docs.astral.sh/uv/) to create the environment and install dependencies.

## Installation

From this directory:

```powershell
uv sync
```

This command installs runtime dependencies and the development group, then synchronizes the environment with `uv.lock`.

To install runtime dependencies only:

```powershell
uv sync --no-dev
```

## Dependencies

### Runtime

| Dependency | Declaration | Resolved version | Role |
| --- | --- | --- | --- |
| `scikit-learn` | `>=1.9.0` | `1.9.0` | Machine learning algorithms, preprocessing, model training, and evaluation. |

`scikit-learn` relies in particular on the following transitive dependencies, which are also present in `uv.lock`:

| Transitive dependency | Resolved version | Role |
| --- | --- | --- |
| `numpy` | `2.5.3` | Numerical computing and array manipulation. |
| `scipy` | `1.18.1` | Scientific computing used by several algorithms. |
| `joblib` | `1.6.0` | Serialization and parallel computation. |
| `threadpoolctl` | `3.6.0` | Thread-pool control for numerical libraries. |

These transitive dependencies should not be added directly to `pyproject.toml` unless the code uses them independently of scikit-learn.

### Development

| Dependency | Declaration | Resolved version | Role |
| --- | --- | --- | --- |
| `jupyterlab` | `>=4.6.3` | `4.6.3` | Interactive environment for exploring data and experimenting with models. |

JupyterLab installs several dependencies for notebooks, the Jupyter server, and the web interface. They are managed automatically by `uv.lock`.

### Package Build

The package uses the `uv_build` backend in the `>=0.12.9,<0.13.0` range. This dependency builds the package and is not required to run the model after installation.

## Usage

Run the current CLI command:

```powershell
uv run ai-model
```

Launch JupyterLab:

```powershell
uv run jupyter lab
```

Import the package from Python code:

```python
import ai_model
```

## Dependency Management

- Modify direct dependencies in `pyproject.toml`.
- Run `uv lock` after a change to recalculate resolved versions.
- Use `uv sync` to apply the lockfile to the local environment.
- Keep `uv.lock` under version control to reproduce installations.

## Structure

```text
ai_model/
├── pyproject.toml
├── uv.lock
├── .python-version
├── README.md
├── src/
  └── ai_model/
    └── __init__.py
```
