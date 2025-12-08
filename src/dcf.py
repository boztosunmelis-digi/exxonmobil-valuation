import numpy as np

def discount_fcf(fcfs, wacc):
    """
    Discount a list of projected Free Cash Flows using WACC.

    Parameters
    ----------
    fcfs : list[float]
        Projected free cash flows (per year).
    wacc : float
        Discount rate in decimal form, e.g. 0.08 for 8%.

    Returns
    -------
    float
        Present value of projected cash flows.
    """
    years = np.arange(1, len(fcfs) + 1)
    fcfs = np.array(fcfs, dtype=float)
    return float(np.sum(fcfs / (1 + wacc) ** years))


def calculate_terminal_value(final_fcf, wacc, growth_rate):
    """
    Perpetuity growth model for terminal value.

    Parameters
    ----------
    final_fcf : float
        Free cash flow in the final forecast year.
    wacc : float
        Discount rate (decimal).
    growth_rate : float
        Long-term growth rate (decimal).

    Returns
    -------
    float
        Terminal value at the end of the forecast period.
    """
    if growth_rate >= wacc:
        raise ValueError("Growth rate must be lower than WACC in a stable perpetuity.")
    return (final_fcf * (1 + growth_rate)) / (wacc - growth_rate)
