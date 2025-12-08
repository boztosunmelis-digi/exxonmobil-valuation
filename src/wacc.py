def calculate_wacc(cost_of_equity, cost_of_debt, tax_rate, equity_weight, debt_weight):
    """
    Calculate the Weighted Average Cost of Capital (WACC).

    Parameters
    ----------
    cost_of_equity : float
        Cost of equity (decimal).
    cost_of_debt : float
        Pre-tax cost of debt (decimal).
    tax_rate : float
        Corporate tax rate (decimal).
    equity_weight : float
        Target equity weight (E / (D+E)).
    debt_weight : float
        Target debt weight (D / (D+E)).

    Returns
    -------
    float
        WACC in decimal form.
    """
    return equity_weight * cost_of_equity + debt_weight * cost_of_debt * (1 - tax_rate)
