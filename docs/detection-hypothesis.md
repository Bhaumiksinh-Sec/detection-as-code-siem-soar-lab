# Detection Hypothesis

## 1. Suspicious Authentication Activity

### Hypothesis
Multiple failed authentication attempts against different user accounts
from the same source within a short time window may indicate
brute-force or password spraying activity.

### Why this matters
Password spraying is a common initial access technique used
to compromise valid user accounts without triggering account lockouts.

### Expected data sources
- Authentication logs (Windows / VPN / Cloud IdP)
- Fields such as username, source IP, timestamp, result

### High-confidence conditions
- Multiple failed attempts
- Same source IP
- Different user accounts
- Short time window
- Optional: followed by a successful login

### Expected response
- Create a security incident
- Enrich with IP reputation
- Notify or document for analyst review
