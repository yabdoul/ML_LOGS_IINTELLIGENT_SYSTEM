# 📊 Log Entry Schema

## Overview

The `LogEntry` schema defines the standard format for all logs generated and consumed within the ML Log Intelligence System.

This schema ensures **data consistency, validation, and reliability** across all services (API, ML pipeline, monitoring).

---

## 🎯 Purpose

- Enforce a strict contract for all logs
- Ensure ML models receive clean and structured data
- Enable reliable debugging and monitoring
- Prevent inconsistent or corrupted log formats

---

## 📦 Schema Definition

Each log entry must follow this structure:


| Field        | Type     | Description                               |
| ------------ | -------- | ----------------------------------------- |
| timestamp    | datetime | Time the event occurred                   |
| level        | string   | Log severity level                        |
| service_name | string   | Name of the service generating the log    |
| message      | string   | Human-readable log message                |
| request_id   | string   | Unique identifier for request tracing     |
| latency_ms   | int      | Request/operation latency in milliseconds |
| status_code  | int      | HTTP-style status code                    |

---

## 🚦 Allowed Values

### Log Levels

Only the following values are allowed:

- INFO
- WARN
- ERROR
- CRITICAL

Any other value will be rejected by validation.

---

## ⚠️ Validation Rules

- `service_name` cannot be empty
- `message` cannot be empty
- `request_id` cannot be empty
- `latency_ms` must be ≥ 0
- `status_code` must be between 100 and 599

Invalid data will be rejected at schema validation level.

---

## 🔄 Example Log Entry

```json
{
  "timestamp": "2026-04-16T12:00:00Z",
  "level": "ERROR",
  "service_name": "auth-service",
  "message": "Login failed due to invalid credentials",
  "request_id": "req_12345",
  "latency_ms": 120,
  "status_code": 401
}
```
