#!/usr/bin/env python3
"""CRI 2030 AI-estate napkin cost model.

This adapts the Chapter 16 starter. Prices are course snapshots, not quotes.
Re-check vendor pricing before a procurement decision.
"""

MONTHLY_INPUT_TOKENS = 400_000_000
MONTHLY_OUTPUT_TOKENS = 100_000_000

API_PRICES = {
    "claude-haiku-4-5":  {"in": 1.0,  "out": 5.0},
    "claude-sonnet-4-6": {"in": 3.0,  "out": 15.0},
    "gpt-5.5":           {"in": 5.0,  "out": 30.0},
    "gemini-3-flash":    {"in": 0.50, "out": 3.0},
}

SELFHOST_NODE_USD_PER_MONTH = 22_000
SELFHOST_TOKENS_PER_MONTH = 1_500_000_000


def api_monthly_cost(model: str) -> float:
    p = API_PRICES[model]

    return (
        (MONTHLY_INPUT_TOKENS / 1e6) * p["in"]
        + (MONTHLY_OUTPUT_TOKENS / 1e6) * p["out"]
    )


def blended_api_cost_per_million(model: str) -> float:
    total = MONTHLY_INPUT_TOKENS + MONTHLY_OUTPUT_TOKENS

    input_share = MONTHLY_INPUT_TOKENS / total
    output_share = MONTHLY_OUTPUT_TOKENS / total

    p = API_PRICES[model]

    return (
        input_share * p["in"]
        + output_share * p["out"]
    )


def crossover_tokens_per_month(model: str) -> float:
    return (
        SELFHOST_NODE_USD_PER_MONTH
        / blended_api_cost_per_million(model)
        * 1_000_000
    )


def selfhost_cost_per_million() -> float:
    total = MONTHLY_INPUT_TOKENS + MONTHLY_OUTPUT_TOKENS

    return (
        SELFHOST_NODE_USD_PER_MONTH
        / (total / 1e6)
    )


if __name__ == "__main__":

    total_tokens = (
        MONTHLY_INPUT_TOKENS
        + MONTHLY_OUTPUT_TOKENS
    )

    print(
        f"Workload: {total_tokens/1e6:.0f}M tokens/month "
        f"({MONTHLY_INPUT_TOKENS/1e6:.0f}M in / "
        f"{MONTHLY_OUTPUT_TOKENS/1e6:.0f}M out)\n"
    )

    print(
        "Per-token API (course price snapshots):"
    )

    for model in API_PRICES:

        print(
            f"  {model:20s} "
            f"${api_monthly_cost(model):>12,.0f}/mo "
            f"blended=${blended_api_cost_per_million(model):.2f}/1M"
        )

    print(
        "\nSelf-host (illustrative reserved node):"
    )

    print(
        f"  8xH100 node          "
        f"${SELFHOST_NODE_USD_PER_MONTH:>12,.0f}/mo "
        f"(capacity="
        f"{SELFHOST_TOKENS_PER_MONTH/1e9:.1f}B tokens/mo; "
        f"headroom="
        f"{SELFHOST_TOKENS_PER_MONTH/total_tokens:.1f}x)"
    )

    print(
        "  effective $/1M tokens at current volume: "
        f"${selfhost_cost_per_million():.2f}"
    )

    print(
        "\nTheoretical API-to-self-host crossover:"
    )

    for model in API_PRICES:

        crossover = (
            crossover_tokens_per_month(
                model
            )
        )

        capacity_status = (
            "WITHIN node capacity"
            if crossover
            <= SELFHOST_TOKENS_PER_MONTH
            else "ABOVE node capacity"
        )

        print(
            f"  {model:20s} "
            f"{crossover/1e9:>6.2f}B tokens/mo "
            f"({capacity_status})"
        )

    print(
        "\nCRI architectural conclusion:"
    )

    print(
        "  Under these course assumptions, the single 8xH100 node does not "
        "beat any listed API on token cost within its 1.5B-token monthly capacity."
    )

    print(
        "  Therefore self-hosting restricted beneficiary RAG must be justified "
        "by privacy, residency, control, or resilience - not by this token-cost model."
    )
