# CreditLoop Perps Agent

- **Repo:** https://github.com/CrystallineButterfly/Synthesis-BondCredit
- **Primary track:** Bond.credit Agents that Pay
- **Overlap targets:** Bankr Gateway, Uniswap Agentic Finance, Lido stETH Treasury, ERC-8004 Receipts, PayWithLocus, MetaMask Delegations
- **Primary contract:** CreditLoopController
- **Primary operator module:** bondcredit_agent
- **Live TxIDs:** PENDING
- **ERC-8004 registrations:** PENDING
- **Demo link:** docs/demo_video_script.md

A bounded GMX trading desk that journals risk, routes profits toward compute or treasury replenishment, and prepares credit receipts.

## Track evidence

- `artifacts/onchain_intents/lido_yield_route.json`
- `artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json`
- `artifacts/onchain_intents/metamask_delegations_delegate_scope.json`

## Latest verification

```json
{
  "status": "verified",
  "project_name": "CreditLoop Perps Agent",
  "track": "Bond.credit Agents that Pay",
  "plan_id": "0xdfbff0103050a5068456dddceaf368bf90fce921c02404cd72612270911f0338",
  "simulation_hash": "0xc460d6b8d78dc35fe6175d4edcf74a87efe33cc09883316670ba1d43470efc76",
  "execution_status": "offline_prepared",
  "tx_ids": [],
  "artifact_paths": [
    "artifacts/onchain_intents/lido_yield_route.json",
    "artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json",
    "artifacts/onchain_intents/metamask_delegations_delegate_scope.json"
  ],
  "partner_statuses": {
    "Bond.credit": "awaiting_credentials",
    "Bankr Gateway": "awaiting_credentials",
    "Uniswap": "awaiting_credentials",
    "Lido": "prepared_contract_call",
    "ERC-8004 Receipts": "prepared_contract_call",
    "PayWithLocus": "awaiting_credentials",
    "MetaMask Delegations": "prepared_contract_call"
  },
  "created_at": "2026-03-19T03:52:09+00:00"
}
```
