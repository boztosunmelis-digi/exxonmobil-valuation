def enterprise_value(market_cap, net_debt):
    """
    Simple enterprise value calculation.

    EV = equity value (market cap) + net debt
    """
    return market_cap + net_debt


def ev_ebitda_multiple(market_cap, net_debt, ebitda):
    """
    EV / EBITDA trading multiple.
    """
    ev = enterprise_value(market_cap, net_debt)
    if ebitda == 0:
        raise ValueError("EBITDA cannot be zero when computing EV/EBITDA.")
    return ev / ebitda
