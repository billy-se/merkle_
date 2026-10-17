# Merkle Tree Audit Engine

A lightweight Python implementation of a Merkle Tree for tamper-evident audit logging using SHA-256.

## Current Status (v1.0)
- SHA-256 cryptographic hashing & recursive tree building.
- Heavily commented inline for deep learning and line-by-line reference.

## Scaling Roadmap (Future Plan)
- [ ] Wrap into a **FastAPI** microservice (`POST /logs`, `GET /root`).
- [ ] Implement **Merkle Inclusion Proofs** for cryptographic verification.
- [ ] Add **PostgreSQL** persistence for historical audit trails.

## Quick Usage
```bash
python merkle_tree.py