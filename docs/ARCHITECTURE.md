# Architecture

ProjectPulse begins as a modular Python application. It intentionally avoids a web frontend: Excel is the input and reporting interface, while the Python package owns validation and analytical logic.

## Intended modules

```text
src/projectpulse/
|-- domain/       Typed project, activity, dependency, resource, and risk models
|-- excel_io/     Workbook reading, schema validation, and report generation
|-- scheduling/   Graph construction, CPM, calendars, and schedule calculations
|-- evm/          Earned Value metrics and forecasts
|-- resources/    Utilization, conflicts, heuristics, and optimization
|-- risk/         Duration distributions and Monte Carlo simulation
|-- scenarios/    Baseline-preserving what-if comparisons
`-- reporting/    Tables, charts, warnings, and workbook presentation
```

These folders should be introduced only when their first real module is implemented. Empty architectural layers are avoided.

## Design rules

- Workbook code converts external data into validated domain objects.
- Calculation functions do not read or format Excel files directly.
- Baseline inputs remain immutable during scenario analysis.
- Algorithms return inspectable values rather than only charts.
- Errors identify their workbook location and recommended correction.
- Every formula or algorithm has at least one hand-verified example.
