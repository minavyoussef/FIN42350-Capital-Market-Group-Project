"""Simple Streamlit demo for the FIN42350 portfolio-design project."""

from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="FIN42350 Capital Market - Group Project",
    page_icon="📊",
    layout="wide",
)

BASE_DIR = Path(__file__).resolve().parent
E2E_DIAGRAM = BASE_DIR / "report" / "fig-1-e2e-framework-diagram.png"
SCENARIO_GROWTH = BASE_DIR / "report" / "three-scenario-out-of-sample-growth.png"
MARKET_DATA = BASE_DIR / "output" / "five_phase_workflow" / "market_data_daily_eur.pkl"
TRADING_DAYS = 252
OUT_OF_SAMPLE_START = pd.Timestamp("2024-10-03")
REPRESENTATIVE_ETFS = {
    "Equity": ("SPY", "SPDR S&P 500 ETF Trust"),
    "Fixed Income": ("AGG", "iShares Core U.S. Aggregate Bond ETF"),
    "Cash": ("BIL", "SPDR Bloomberg 1-3 Month T-Bill ETF"),
    "Real Estate": ("VNQ", "Vanguard Real Estate ETF"),
    "Commodity": ("IAU", "iShares Gold Trust"),
}
PREFERENCE_TO_POINTS = {
    "Exclude": 0,
    "Very low": 1,
    "Low": 2,
    "Medium": 3,
    "High": 4,
    "Very high": 5,
}

PHASES = [
    "Home",
    "Phase I - Investor Profile",
    "Phase II - Asset-Class Allocation",
    "Phase III - Market Data",
    "Phase IV - Portfolio Optimization",
    "Phase V - Performance Analysis",
    "End-to-End - Summary",
]

SCENARIOS = {
    "Risky investor": {
        "description": "Prioritizes long-term growth and accepts substantial short-term losses.",
        "answers": {
            "Risk tolerance": ("Very high", 3),
            "Investment horizon": ("Very long", 2),
            "Growth objective": ("Very high", 3),
            "Capital preservation": ("Low", 1),
            "Liquidity requirement": ("Low", 1),
        },
        "risk_score": 0.950,
        "risk_profile": "Aggressive",
        "risk_aversion": 1,
        "allocation": {
            "Equity": 30.96,
            "Fixed Income": 12.48,
            "Cash": 6.32,
            "Real Estate": 26.26,
            "Commodity": 23.99,
        },
        "optimization": {
            "Expected annual return": "17.59%",
            "Annualized volatility": "21.66%",
            "Sharpe ratio": "0.812",
            "Selected assets": "9",
        },
        "holdings": [
            ("United States Brent Oil Fund", "Commodity", 15.00),
            ("VanEck Semiconductor ETF", "Equity", 15.00),
            ("iShares Semiconductor ETF", "Equity", 15.00),
            ("Real Estate Select Sector SPDR Fund", "Real Estate", 15.00),
            ("SPDR Bloomberg High Yield Bond ETF", "Fixed Income", 12.48),
            ("Vanguard Real Estate ETF", "Real Estate", 11.26),
            ("iShares Silver Trust", "Commodity", 8.99),
            ("SPDR Bloomberg 1-3 Month T-Bill ETF", "Cash", 6.32),
            ("Global X MSCI Argentina ETF", "Equity", 0.96),
        ],
        "performance": {
            "Total return": "70.56%",
            "Annualized return": "30.67%",
            "Annualized volatility": "21.03%",
            "Sharpe ratio": "1.458",
            "Maximum drawdown": "20.87%",
            "Ending value": "€1,705,595",
        },
        "tail_risk": [("95%", "2.19%", "3.32%"), ("99%", "3.86%", "5.85%")],
        "simulation": ("€1,161,882", "€820,441", "€1,657,255"),
    },
    "Balanced investor": {
        "description": "Balances capital growth with preservation and liquidity.",
        "answers": {
            "Risk tolerance": ("Moderate", 3),
            "Investment horizon": ("Medium", 2),
            "Growth objective": ("Medium", 2),
            "Capital preservation": ("Medium", 2),
            "Liquidity requirement": ("Medium", 1),
        },
        "risk_score": 0.500,
        "risk_profile": "Moderate",
        "risk_aversion": 5,
        "allocation": {
            "Equity": 18.37,
            "Fixed Income": 26.02,
            "Cash": 23.09,
            "Real Estate": 17.40,
            "Commodity": 15.12,
        },
        "optimization": {
            "Expected annual return": "11.01%",
            "Annualized volatility": "12.72%",
            "Sharpe ratio": "0.865",
            "Selected assets": "11",
        },
        "holdings": [
            ("SPDR Bloomberg 1-3 Month T-Bill ETF", "Cash", 23.09),
            ("VanEck Semiconductor ETF", "Equity", 15.00),
            ("Real Estate Select Sector SPDR Fund", "Real Estate", 15.00),
            ("Schwab US TIPS ETF", "Fixed Income", 15.00),
            ("Vanguard Short-Term Treasury ETF", "Fixed Income", 8.56),
            ("iShares Gold Trust", "Commodity", 6.53),
            ("Invesco DB Agriculture Fund", "Commodity", 5.90),
            ("Global X MSCI Argentina ETF", "Equity", 3.37),
            ("United States Brent Oil Fund", "Commodity", 2.69),
            ("iShares TIPS Bond ETF", "Fixed Income", 2.45),
            ("Vanguard Real Estate ETF", "Real Estate", 2.40),
        ],
        "performance": {
            "Total return": "32.71%",
            "Annualized return": "15.23%",
            "Annualized volatility": "12.22%",
            "Sharpe ratio": "1.247",
            "Maximum drawdown": "13.08%",
            "Ending value": "€1,327,058",
        },
        "tail_risk": [("95%", "1.24%", "1.77%"), ("99%", "2.35%", "2.97%")],
        "simulation": ("€1,108,812", "€897,039", "€1,364,307"),
    },
    "Conservative investor": {
        "description": "Prioritizes capital stability, liquidity, and downside protection.",
        "answers": {
            "Risk tolerance": ("Low", 3),
            "Investment horizon": ("Short", 2),
            "Growth objective": ("Low", 1),
            "Capital preservation": ("High", 3),
            "Liquidity requirement": ("High", 1),
        },
        "risk_score": 0.250,
        "risk_profile": "Conservative",
        "risk_aversion": 8,
        "allocation": {
            "Equity": 10.09,
            "Fixed Income": 33.21,
            "Cash": 34.31,
            "Real Estate": 11.56,
            "Commodity": 10.83,
        },
        "optimization": {
            "Expected annual return": "7.54%",
            "Annualized volatility": "9.80%",
            "Sharpe ratio": "0.769",
            "Selected assets": "10",
        },
        "holdings": [
            ("SPDR Bloomberg 1-3 Month T-Bill ETF", "Cash", 34.31),
            ("Schwab US TIPS ETF", "Fixed Income", 15.00),
            ("Vanguard Short-Term Treasury ETF", "Fixed Income", 15.00),
            ("Real Estate Select Sector SPDR Fund", "Real Estate", 11.56),
            ("VanEck Semiconductor ETF", "Equity", 10.09),
            ("Invesco DB Agriculture Fund", "Commodity", 5.58),
            ("iShares Gold Trust", "Commodity", 3.89),
            ("Vanguard Short-Term Corporate Bond ETF", "Fixed Income", 3.21),
            ("United States Brent Oil Fund", "Commodity", 1.29),
            ("United States Copper Index Fund", "Commodity", 0.06),
        ],
        "performance": {
            "Total return": "22.53%",
            "Annualized return": "10.72%",
            "Annualized volatility": "9.79%",
            "Sharpe ratio": "1.095",
            "Maximum drawdown": "12.09%",
            "Ending value": "€1,225,349",
        },
        "tail_risk": [("95%", "0.92%", "1.37%"), ("99%", "2.12%", "2.31%")],
        "simulation": ("€1,073,354", "€912,024", "€1,259,734"),
    },
}


@st.cache_data
def load_market_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load the saved EUR prices and returns used by the project."""
    if not MARKET_DATA.exists():
        raise FileNotFoundError(f"Market data not found: {MARKET_DATA}")
    market_df = pd.read_pickle(MARKET_DATA)
    market_df["date"] = pd.to_datetime(market_df["date"])
    tickers = [ticker for ticker, _ in REPRESENTATIVE_ETFS.values()]
    returns = (
        market_df[market_df["ticker"].isin(tickers)]
        .pivot(index="date", columns="ticker", values="daily_return_euro")
        .sort_index()
    )
    prices = (
        market_df[market_df["ticker"].isin(tickers)]
        .pivot(index="date", columns="ticker", values="adjusted_close_euro")
        .sort_index()
    )
    return returns, prices


def historical_var_es(returns: pd.Series, confidence: float) -> tuple[float, float]:
    losses = -returns.dropna()
    value_at_risk = float(np.quantile(losses, confidence, method="higher"))
    expected_shortfall = float(losses[losses >= value_at_risk].mean())
    return value_at_risk, expected_shortfall


def performance_metrics(values: pd.Series) -> dict[str, str]:
    returns = values.pct_change(fill_method=None).dropna()
    years = (values.index[-1] - values.index[0]).days / 365.25
    total_return = values.iloc[-1] / values.iloc[0] - 1
    annualized_return = (1 + total_return) ** (1 / years) - 1
    volatility = returns.std(ddof=1) * np.sqrt(TRADING_DAYS)
    drawdown = values / values.cummax() - 1
    return {
        "Total return": f"{total_return:.2%}",
        "Annualized return": f"{annualized_return:.2%}",
        "Annualized volatility": f"{volatility:.2%}",
        "Sharpe ratio": f"{annualized_return / volatility:.3f}",
        "Maximum drawdown": f"{abs(drawdown.min()):.2%}",
        "Ending value": f"€{values.iloc[-1]:,.0f}",
    }


def monte_carlo_wealth(
    expected_return: float,
    volatility: float,
    initial_capital: float,
    scenarios: int = 2_000,
) -> tuple[pd.DataFrame, tuple[str, str, str]]:
    """Return one-year Monte Carlo percentile paths and terminal statistics."""
    rng = np.random.default_rng(42_350)
    shocks = rng.standard_normal((scenarios, TRADING_DAYS))
    daily_log_returns = (
        (expected_return - 0.5 * volatility**2) / TRADING_DAYS
        + volatility * shocks / np.sqrt(TRADING_DAYS)
    )
    simulated_values = initial_capital * np.exp(np.cumsum(daily_log_returns, axis=1))
    simulated_values = np.column_stack(
        [np.full(scenarios, initial_capital), simulated_values]
    )
    percentiles = pd.DataFrame(
        {
            "5th percentile": np.quantile(simulated_values, 0.05, axis=0),
            "Median": np.median(simulated_values, axis=0),
            "95th percentile": np.quantile(simulated_values, 0.95, axis=0),
        },
        index=pd.Index(range(TRADING_DAYS + 1), name="Trading day"),
    )
    terminal = simulated_values[:, -1]
    summary = (
        f"€{np.median(terminal):,.0f}",
        f"€{np.quantile(terminal, 0.05):,.0f}",
        f"€{np.quantile(terminal, 0.95):,.0f}",
    )
    return percentiles, summary


def build_custom_scenario(allocation: dict[str, float], initial_capital: float) -> dict:
    """Calculate a custom representative-ETF portfolio from user-entered weights."""
    returns, prices = load_market_data()
    ticker_weights = pd.Series(
        {
            REPRESENTATIVE_ETFS[asset_class][0]: weight / 100
            for asset_class, weight in allocation.items()
        }
    )

    in_sample_returns = returns.loc[returns.index < OUT_OF_SAMPLE_START, ticker_weights.index].dropna()
    portfolio_returns = in_sample_returns.dot(ticker_weights)
    expected_return = float(portfolio_returns.mean() * TRADING_DAYS)
    volatility = float(portfolio_returns.std(ddof=1) * np.sqrt(TRADING_DAYS))

    out_of_sample_prices = prices.loc[
        prices.index >= OUT_OF_SAMPLE_START, ticker_weights.index
    ].dropna()
    units = initial_capital * ticker_weights / out_of_sample_prices.iloc[0]
    growth = out_of_sample_prices.mul(units, axis=1).sum(axis=1)
    daily_returns = growth.pct_change(fill_method=None).dropna()

    tail_risk = []
    for confidence in (0.95, 0.99):
        value_at_risk, expected_shortfall = historical_var_es(daily_returns, confidence)
        tail_risk.append(
            (f"{confidence:.0%}", f"{value_at_risk:.2%}", f"{expected_shortfall:.2%}")
        )

    _, simulation_summary = monte_carlo_wealth(
        expected_return, volatility, initial_capital
    )
    holdings = [
        (REPRESENTATIVE_ETFS[asset_class][1], asset_class, weight)
        for asset_class, weight in allocation.items()
        if weight > 0
    ]
    return {
        "description": "A user-defined allocation implemented with one representative ETF per asset class.",
        "allocation": allocation,
        "risk_score": None,
        "risk_profile": "User defined",
        "risk_aversion": None,
        "optimization": {
            "Expected annual return": f"{expected_return:.2%}",
            "Annualized volatility": f"{volatility:.2%}",
            "Sharpe ratio": f"{expected_return / volatility:.3f}",
            "Selected assets": str(len(holdings)),
        },
        "holdings": holdings,
        "performance": performance_metrics(growth),
        "tail_risk": tail_risk,
        "simulation": simulation_summary,
        "mc_expected_return": expected_return,
        "mc_volatility": volatility,
        "capital": initial_capital,
        "growth": growth,
    }


def metric_row(values: dict[str, str]) -> None:
    """Display a compact row of Streamlit metrics."""
    columns = st.columns(len(values))
    for column, (label, value) in zip(columns, values.items(), strict=True):
        column.metric(label, value)


def show_home() -> None:
    st.title("FIN42350 Capital Market - Group Project")
    st.markdown("### Student Name: Mina Youssef\n### Student Number: 14200381")
    st.write(
        "A simple demonstration of an end-to-end, client-specific portfolio "
        "construction workflow. Select an investor and a phase from the master "
        "panel to inspect the corresponding output."
    )
    if E2E_DIAGRAM.exists():
        st.image(E2E_DIAGRAM, caption="End-to-end five-phase portfolio framework", use_container_width=True)
    else:
        st.warning(f"Diagram not found: {E2E_DIAGRAM}")


def show_phase_one(name: str, scenario: dict) -> None:
    st.title("Phase I - Investor Profile and Risk Assessment")
    st.subheader(name)
    st.caption(scenario["description"])
    if "answers" not in scenario:
        st.info(
            "The custom portfolio bypasses the questionnaire. Its weights are entered directly in the master panel."
        )
        return
    answers_df = pd.DataFrame(
        [
            {"Question": question, "Answer": answer, "Importance points": points}
            for question, (answer, points) in scenario["answers"].items()
        ]
    )
    st.dataframe(answers_df, hide_index=True, use_container_width=True)
    metric_row(
        {
            "Risk score": f"{scenario['risk_score']:.3f}",
            "Risk profile": scenario["risk_profile"],
            "Risk-aversion λ": str(scenario["risk_aversion"]),
        }
    )
    st.info("The questionnaire score determines the risk profile and the λ used by the optimizer.")


def show_phase_two(name: str, scenario: dict) -> None:
    st.title("Phase II - Investor Suitability and Asset-Class Allocation")
    st.subheader(name)
    allocation_df = pd.DataFrame(
        scenario["allocation"].items(), columns=["Asset class", "Target weight (%)"]
    )
    st.bar_chart(allocation_df.set_index("Asset class"), y="Target weight (%)")
    st.dataframe(
        allocation_df.style.format({"Target weight (%)": "{:.2f}%"}),
        hide_index=True,
        use_container_width=True,
    )
    st.info("Suitability scores are normalized so the strategic asset-class allocation totals 100%.")


def show_phase_three() -> None:
    st.title("Phase III - Market Data Preparation")
    metric_row(
        {
            "Eligible assets": "119",
            "In-sample observations": "1,257",
            "Out-of-sample observations": "501",
        }
    )
    sample_df = pd.DataFrame(
        [
            ("Full sample", "3 Oct 2019", "2 Oct 2026", "Seven-year market window"),
            ("In-sample", "4 Oct 2019", "2 Oct 2024", "Estimate return and covariance"),
            ("Out-of-sample", "3 Oct 2024", "2 Oct 2026", "Evaluate frozen weights"),
        ],
        columns=["Dataset", "Start", "End", "Purpose"],
    )
    st.dataframe(sample_df, hide_index=True, use_container_width=True)
    st.info("The same daily EUR-denominated data and estimates are used for all three investors.")


def show_phase_four(name: str, scenario: dict, initial_capital: float) -> None:
    st.title("Phase IV - Portfolio Optimization")
    st.subheader(name)
    metric_row(scenario["optimization"])
    holdings_df = pd.DataFrame(
        scenario["holdings"], columns=["Investment", "Asset class", "Weight (%)"]
    )
    holdings_df["Allocation (€)"] = holdings_df["Weight (%)"] * initial_capital / 100
    st.bar_chart(holdings_df.set_index("Investment"), y="Weight (%)")
    st.dataframe(
        holdings_df.style.format({"Weight (%)": "{:.2f}%", "Allocation (€)": "€{:,.0f}"}),
        hide_index=True,
        use_container_width=True,
    )
    if "answers" in scenario:
        st.info("Weights maximize estimated mean–variance utility subject to the investor's asset-class targets and ETF limits.")
    else:
        st.info("The entered asset-class weights are implemented with representative ETFs and update automatically.")


def show_phase_five(name: str, scenario: dict, initial_capital: float) -> None:
    st.title("Phase V - Portfolio Benchmarking and Performance Analysis")
    st.subheader(name)
    metric_row(scenario["performance"])

    st.markdown("#### Relevant performance indicators")
    performance_df = pd.DataFrame(
        scenario["performance"].items(), columns=["Indicator", "Value"]
    )
    st.dataframe(performance_df, hide_index=True, use_container_width=True)

    left, right = st.columns(2)
    with left:
        st.markdown("#### Historical downside risk")
        tail_df = pd.DataFrame(
            scenario["tail_risk"], columns=["Confidence", "One-day VaR", "Expected Shortfall"]
        )
        st.dataframe(tail_df, hide_index=True, use_container_width=True)
    with right:
        st.markdown("#### One-year Monte Carlo wealth")
        median, lower, upper = scenario["simulation"]
        simulation_df = pd.DataFrame(
            [("Median", median), ("5th percentile", lower), ("95th percentile", upper)],
            columns=["Statistic", "Terminal wealth"],
        )
        st.dataframe(simulation_df, hide_index=True, use_container_width=True)

    expected_return = scenario.get(
        "mc_expected_return",
        float(scenario["optimization"]["Expected annual return"].rstrip("%")) / 100,
    )
    volatility = scenario.get(
        "mc_volatility",
        float(scenario["optimization"]["Annualized volatility"].rstrip("%")) / 100,
    )
    monte_carlo_df, _ = monte_carlo_wealth(expected_return, volatility, initial_capital)
    st.markdown("#### One-year Monte Carlo wealth paths")
    st.line_chart(monte_carlo_df, y=["5th percentile", "Median", "95th percentile"])
    st.caption("Illustrative simulation using the in-sample annualized return and volatility.")

    if "growth" in scenario:
        st.markdown("#### Custom portfolio out-of-sample growth")
        st.line_chart(scenario["growth"].rename("Portfolio value (€)"))
    elif SCENARIO_GROWTH.exists():
        st.image(SCENARIO_GROWTH, caption="Out-of-sample growth from an initial €1 million", use_container_width=True)
    st.info("Results use frozen weights and daily returns measured in euros.")


def show_end_to_end(name: str, scenario: dict, initial_capital: float) -> None:
    """Show the selected portfolio's complete five-phase journey on one page."""
    st.title("End-to-End Portfolio Summary")
    st.subheader(name)
    st.caption(scenario["description"])
    st.markdown(
        "**Investor profile** → **Asset-class allocation** → **Market data** → "
        "**Portfolio construction** → **Performance evaluation**"
    )

    st.divider()
    st.markdown("## Phase I - Investor Profile and Risk Assessment")
    if "answers" in scenario:
        answers_df = pd.DataFrame(
            [
                {"Question": question, "Answer": answer, "Importance points": points}
                for question, (answer, points) in scenario["answers"].items()
            ]
        )
        st.dataframe(answers_df, hide_index=True, use_container_width=True)
        metric_row(
            {
                "Risk score": f"{scenario['risk_score']:.3f}",
                "Risk profile": scenario["risk_profile"],
                "Risk-aversion λ": str(scenario["risk_aversion"]),
            }
        )
    else:
        st.info(
            "Custom portfolio: the questionnaire is bypassed and preferences are converted directly into normalized weights."
        )

    st.divider()
    st.markdown("## Phase II - Investor Suitability and Asset-Class Allocation")
    allocation_df = pd.DataFrame(
        scenario["allocation"].items(), columns=["Asset class", "Weight (%)"]
    )
    st.bar_chart(allocation_df.set_index("Asset class"), y="Weight (%)")
    st.dataframe(
        allocation_df.style.format({"Weight (%)": "{:.2f}%"}),
        hide_index=True,
        use_container_width=True,
    )

    st.divider()
    st.markdown("## Phase III - Market Data Preparation")
    metric_row(
        {
            "Eligible assets": "119",
            "In-sample observations": "1,257",
            "Out-of-sample observations": "501",
        }
    )
    market_df = pd.DataFrame(
        [
            ("Full sample", "3 Oct 2019", "2 Oct 2026", "Seven-year market window"),
            ("In-sample", "4 Oct 2019", "2 Oct 2024", "Estimate return and covariance"),
            ("Out-of-sample", "3 Oct 2024", "2 Oct 2026", "Evaluate frozen weights"),
        ],
        columns=["Dataset", "Start", "End", "Purpose"],
    )
    st.dataframe(market_df, hide_index=True, use_container_width=True)
    st.caption("Prices and returns are converted to euros before estimation and evaluation.")

    st.divider()
    st.markdown("## Phase IV - Portfolio Optimization")
    metric_row(scenario["optimization"])
    holdings_df = pd.DataFrame(
        scenario["holdings"], columns=["Investment", "Asset class", "Weight (%)"]
    )
    holdings_df["Allocation (€)"] = holdings_df["Weight (%)"] * initial_capital / 100
    st.bar_chart(holdings_df.set_index("Investment"), y="Weight (%)")
    st.dataframe(
        holdings_df.style.format({"Weight (%)": "{:.2f}%", "Allocation (€)": "€{:,.0f}"}),
        hide_index=True,
        use_container_width=True,
    )

    st.divider()
    st.markdown("## Phase V - Portfolio Benchmarking and Performance Analysis")
    metric_row(scenario["performance"])
    performance_df = pd.DataFrame(
        scenario["performance"].items(), columns=["Performance indicator", "Value"]
    )
    st.dataframe(performance_df, hide_index=True, use_container_width=True)

    left, right = st.columns(2)
    tail_df = pd.DataFrame(
        scenario["tail_risk"], columns=["Confidence", "One-day VaR", "Expected Shortfall"]
    )
    left.markdown("### Historical downside risk")
    left.dataframe(tail_df, hide_index=True, use_container_width=True)
    median, lower, upper = scenario["simulation"]
    simulation_df = pd.DataFrame(
        [("Median", median), ("5th percentile", lower), ("95th percentile", upper)],
        columns=["Monte Carlo statistic", "Terminal wealth"],
    )
    right.markdown("### Simulated terminal wealth")
    right.dataframe(simulation_df, hide_index=True, use_container_width=True)

    expected_return = scenario.get(
        "mc_expected_return",
        float(scenario["optimization"]["Expected annual return"].rstrip("%")) / 100,
    )
    volatility = scenario.get(
        "mc_volatility",
        float(scenario["optimization"]["Annualized volatility"].rstrip("%")) / 100,
    )
    monte_carlo_df, _ = monte_carlo_wealth(expected_return, volatility, initial_capital)
    st.markdown("### One-year Monte Carlo wealth paths")
    st.line_chart(monte_carlo_df, y=["5th percentile", "Median", "95th percentile"])

    if "growth" in scenario:
        st.markdown("### Out-of-sample portfolio growth")
        st.line_chart(scenario["growth"].rename("Portfolio value (€)"))
    elif SCENARIO_GROWTH.exists():
        st.image(
            SCENARIO_GROWTH,
            caption="Out-of-sample growth from an initial €1 million",
            use_container_width=True,
        )

    st.success(
        "The complete workflow connects investor inputs to the final allocation, historical evaluation, downside risk, and simulated outcome."
    )


with st.sidebar:
    st.title("Portfolio Design")
    investor_options = [*SCENARIOS, "Custom portfolio"]
    selected_investor = st.radio("Investor scenario", investor_options, index=1)
    initial_capital = 1_000_000.0
    custom_allocation = None
    if selected_investor == "Custom portfolio":
        st.markdown("#### Custom inputs")
        initial_capital = st.number_input(
            "Initial capital (€)", min_value=1_000.0, value=1_000_000.0, step=10_000.0
        )
        preference_options = list(PREFERENCE_TO_POINTS)
        preferences = {
            "Equity": st.selectbox("Equity preference", preference_options, index=4),
            "Fixed Income": st.selectbox("Fixed-income preference", preference_options, index=4),
            "Cash": st.selectbox("Cash preference", preference_options, index=3),
            "Real Estate": st.selectbox("Real-estate preference", preference_options, index=3),
            "Commodity": st.selectbox("Commodity preference", preference_options, index=2),
        }
        preference_points = {
            asset_class: PREFERENCE_TO_POINTS[preference]
            for asset_class, preference in preferences.items()
        }
        total_points = sum(preference_points.values())
        if total_points <= 0:
            st.error("Select at least one asset class above Exclude.")
            st.stop()
        custom_allocation = {
            asset_class: points / total_points * 100
            for asset_class, points in preference_points.items()
        }
        st.caption(
            "Preferences are converted to points (Exclude = 0 through Very high = 5) "
            "and normalized automatically to 100%."
        )
    st.divider()
    selected_phase = st.radio("View", PHASES)
    st.divider()
    st.caption("FIN42350 | Portfolio Design Demo")

if selected_investor == "Custom portfolio":
    try:
        selected_scenario = build_custom_scenario(custom_allocation, initial_capital)
    except FileNotFoundError as error:
        st.error(str(error))
        st.stop()
else:
    selected_scenario = SCENARIOS[selected_investor]

if selected_phase == "Home":
    show_home()
elif selected_phase == "Phase I - Investor Profile":
    show_phase_one(selected_investor, selected_scenario)
elif selected_phase == "Phase II - Asset-Class Allocation":
    show_phase_two(selected_investor, selected_scenario)
elif selected_phase == "Phase III - Market Data":
    show_phase_three()
elif selected_phase == "Phase IV - Portfolio Optimization":
    show_phase_four(selected_investor, selected_scenario, initial_capital)
elif selected_phase == "Phase V - Performance Analysis":
    show_phase_five(selected_investor, selected_scenario, initial_capital)
else:
    show_end_to_end(selected_investor, selected_scenario, initial_capital)
