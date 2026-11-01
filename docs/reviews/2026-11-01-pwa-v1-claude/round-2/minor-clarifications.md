# Follow-up to round-2 minor findings

R2-1: Customer tax uses the final owner-selected segment selling amount after override/markup; manual items follow their segment. Manual material costs explicitly declare purchase-tax inclusion/rate. No automatic selling override split by cost category. Trial acceptance includes a $2,000 override/10% synthetic tax fixture. No tax-service integration or real tax rate is invented.

R2-2: Office and field use the same frozen quote record. Field snapshots are Preliminary; an office-reviewed snapshot may be frozen Preliminary or Issued. Status is immutable with the snapshot; issuing an old preliminary creates a new snapshot. Comparing alternatives/revisions remains complete v1. Backup/restore explicitly includes all quote snapshots and source-ID mappings.

Only the spec changed for these clarifications. No backlog, implementation plan or application code.
