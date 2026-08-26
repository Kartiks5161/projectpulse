# ProjectPulse

ProjectPulse is a learning-first, Excel-based project-controls analytics and optimization engine. Excel provides readable project input and reporting, while Python performs validation, scheduling, forecasting, simulation, and optimization.

> **Status:** Early development. The repository scaffold is complete; the first implementation milestone is the Excel schema, input validation, and a manually verified Critical Path Method (CPM) engine.

## Why this project exists

This project is being built to understand project controls—not to assemble a resume project from copied code. Every analytical module will be implemented incrementally, checked against small hand-worked examples, tested, and documented before it is described as complete.

## Planned capabilities

- Structured Excel input for WBS activities, dependencies, costs, progress, resources, risks, and scenarios
- Input validation with clear sheet, row, field, and correction details
- CPM scheduling with forward/backward passes, floats, cycle detection, and critical-path identification
- Earned Value Management (EVM) metrics and forecasting
- Resource conflict detection and resource-leveling optimization
- Monte Carlo schedule-risk analysis with P50/P80 completion estimates
- Time-cost trade-off and schedule-crashing analysis
- Readable Excel reports with Gantt, S-curve, resource, risk, and scenario outputs

Items above are planned capabilities, not claims of completed functionality. See [the roadmap](docs/ROADMAP.md) for the current state.

## Architecture

```text
ProjectPulse_Input.xlsx
          |
          v
Excel reader -> validation -> domain models
                              |
                              v
            CPM / EVM / resources / simulation / scenarios
                              |
                              v
                    Excel report generator
                              |
                              v
                 ProjectPulse_Report.xlsx
```

The calculation modules are kept independent of Excel formatting so that they can be tested with small, transparent datasets.

## Repository structure

```text
projectpulse/
|-- src/projectpulse/     Python package
|-- tests/                Unit and integration tests
|-- docs/                 Architecture, roadmap, and learning notes
|-- data/input/           Local input workbooks (ignored by Git)
|-- data/output/          Generated reports (ignored by Git)
|-- examples/             Small verified example projects
|-- notebooks/            Explanatory analysis notebooks
`-- pyproject.toml        Package and development configuration
```

## Getting started

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest
```

Advanced optimization and simulation dependencies can be installed later:

```powershell
python -m pip install -e ".[advanced,dev]"
```

## Development principles

1. Calculate a small example manually before coding it.
2. Implement one concept at a time.
3. Separate domain calculations from workbook input/output.
4. Add tests for normal cases, edge cases, and invalid inputs.
5. Record design decisions and learning in `LEARNING_LOG.md`.
6. Use only measured results in documentation and resume bullets.

## Current milestone

The first milestone will deliver:

- A documented Excel input schema
- Workbook parsing and validation
- A finish-to-start CPM network
- Forward and backward passes
- Total/free float and critical-path results
- Manually verified automated tests
- A basic Excel results sheet

## License

No license has been selected yet. Until one is added, all rights are reserved.
