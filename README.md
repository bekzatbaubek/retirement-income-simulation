# Retirement Income Simulation

This was code part of a research project ran by Dr. Alex Zhu in Education University of Hong Kong.

## Structure

Depends on `matplotlib` to plot the results.

- `scenarioA.py`: Simulation of a retirement income strategy with interest only.
- `scenarioB.py`: Simulation of a retirement income strategy with interest and losses (job loss, emergencies).
- `scenarioC.py`: Simulation of a retirement income strategy with interest and an investment plan.

## Running the code

```sh
python3 -m venv .venv
source .venv/bin/activate

pip install matplotlib

(venv) python scenarioA.py
(venv) python scenarioB.py
(venv) python scenarioC.py
```
