# Learning and development roadmap

This roadmap separates completed work from planned work. A feature is marked complete only after it has tests, documentation, and a verified example.

## Phase 0 — Repository foundation

- [x] Initialize the Python package structure
- [x] Add development configuration and a smoke test
- [x] Document the learning-first project principles
- [ ] Create the first GitHub issue and learning entry

## Phase 1 — Excel schema and validation

- [ ] Define the Project Setup, Activities, and Dependencies tables
- [ ] Create a small example workbook
- [ ] Parse Excel Tables into typed domain models
- [ ] Report missing sheets, columns, IDs, and invalid values
- [ ] Detect duplicate activity IDs and missing dependencies
- [ ] Test valid and invalid workbooks

## Phase 2 — Critical Path Method

- [ ] Solve a small activity network manually
- [ ] Build a directed activity graph
- [ ] Detect dependency cycles
- [ ] Implement topological ordering
- [ ] Implement the forward pass
- [ ] Implement the backward pass
- [ ] Calculate total float, free float, and critical activities
- [ ] Export results to Excel

## Phase 3 — Earned Value Management

- [ ] Define the progress and cost data model
- [ ] Implement PV, EV, AC, CV, SV, CPI, and SPI
- [ ] Implement EAC, ETC, VAC, and TCPI alternatives
- [ ] Generate WBS and project summaries
- [ ] Create planned, earned, and actual S-curves

## Phase 4 — Resources

- [ ] Detect demand above availability
- [ ] Create a resource-utilization report
- [ ] Implement and explain a simple leveling heuristic
- [ ] Add OR-Tools optimization after validating the heuristic
- [ ] Compare schedule and conflict changes

## Phase 5 — Risk and scenarios

- [ ] Model three-point activity-duration estimates
- [ ] Implement reproducible Monte Carlo simulation
- [ ] Calculate P50/P80 dates and target-date probability
- [ ] Add criticality and sensitivity analysis
- [ ] Implement schedule crashing and scenario comparison

## Phase 6 — Portfolio completion

- [ ] Build a realistic 40–100 activity case study
- [ ] Generate a polished Excel report workbook
- [ ] Measure calculation and simulation performance
- [ ] Document limitations and design decisions
- [ ] Record a short demonstration
- [ ] Write resume bullets using verified results only
