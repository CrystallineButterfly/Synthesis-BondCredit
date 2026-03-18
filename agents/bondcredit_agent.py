"""Project-specific context module."""

from __future__ import annotations

PROJECT_CONTEXT = {
  "project_name": "CreditLoop Perps Agent",
  "track": "Bond.credit Agents that Pay",
  "pitch": "A bounded GMX trading desk that journals risk, routes profits toward compute or treasury replenishment, and prepares credit receipts.",
  "overlap_targets": [
    "Bankr Gateway",
    "Uniswap Agentic Finance",
    "Lido stETH Treasury",
    "ERC-8004 Receipts",
    "PayWithLocus",
    "MetaMask Delegations"
  ],
  "goals": [
    "discover a bounded opportunity",
    "plan a dry-run-first action",
    "verify receipts and proofs"
  ]
}


def seed_targets() -> list[str]:
    """Return the first batch of overlap targets for planning."""
    return list(PROJECT_CONTEXT['overlap_targets'])
