# 01 - Password Spray / Brute Force (Authentication)

## Objective
Detect possible password spraying or brute-force attempts by identifying
many failed logins from one source IP against multiple user accounts within a short time window.

## Data requirements (minimum)
Required fields:
- timestamp
- source.ip
- user.name (or user.id)
- event.outcome (success/failure)

Optional fields (nice to have):
- authentication.method
- geo.country
- device.id / host.name

## Detection logic (plain)
Trigger when:
- event.outcome = "failure"
- the same source.ip attempts logins to >= 8 distinct user accounts
- within 5 minutes

Increase confidence if:
- a successful login occurs from the same source.ip within 10 minutes after the failures

## Tuning / exclusions
Possible exclusions:
- known corporate VPN egress IP ranges
- known security scanner IPs
- password reset / SSO rollout windows

## Severity suggestion
- Medium by default
- High if followed by a success

## Expected response (SOAR-ready)
- Create incident record (GitHub Issue)
- Enrich source.ip (reputation/geo)
- Identify targeted users
- Recommend action: block IP / challenge MFA / review account activity
