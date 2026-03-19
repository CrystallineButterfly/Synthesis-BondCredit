# Live readiness

- **Project:** CreditLoop Perps Agent
- **Track:** Bond.credit Agents that Pay
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:09+00:00`

## Trust boundaries

- **Bond.credit** — `rest_json` — Journal bounded trades and credit-profile updates.
- **Bankr Gateway** — `rest_json` — Route inference through cost-aware model selection.
- **Uniswap** — `rest_json` — Quote swaps and bounded liquidity moves.
- **Lido** — `contract_call` — Route staking yield through guarded treasury actions.
- **ERC-8004 Receipts** — `contract_call` — Anchor identity, task receipts, and reputation updates.
- **PayWithLocus** — `rest_json` — Create bounded subaccounts and controlled spend flows.
- **MetaMask Delegations** — `contract_call` — Enforce delegation scopes, expiries, and intent envelopes.

## Offline-ready partner paths

- **Lido** — prepared_contract_call
- **ERC-8004 Receipts** — prepared_contract_call
- **MetaMask Delegations** — prepared_contract_call

## Live-only partner blockers

- **Bond.credit**: GMX_ORDER_URL, BOND_CREDIT_PROFILE_URL — https://bond.credit/
- **Bankr Gateway**: BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL — https://bankr.bot/
- **Uniswap**: UNISWAP_API_KEY, UNISWAP_QUOTE_URL — https://developers.uniswap.org/
- **PayWithLocus**: LOCUS_API_KEY, LOCUS_PAYMENT_URL — https://docs.locus.finance/

## Highest-sensitivity actions

- `bond_credit_credit_trade` — Bond.credit — Use Bond.credit for a bounded action in this repo.
- `bankr_gateway_compute_route` — Bankr Gateway — Use Bankr Gateway for a bounded action in this repo.
- `metamask_delegations_delegate_scope` — MetaMask Delegations — Use MetaMask Delegations for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for CreditLoopController.
- Run python3 scripts/run_agent.py to produce a dry run for bondcredit_agent.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
