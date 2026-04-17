import argparse
import json
import random
import uuid
from datetime import datetime, timezone

from faker import Faker

fake = Faker()


# ----------------------------
# NORMAL LOG
# ----------------------------
def generate_normal_log():
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": random.choice(["INFO", "WARN"]),
        "service_name": random.choice(
            [
                "auth-service",
                "payment-service",
                "user-service",
                "order-service",
            ]
        ),
        "message": random.choice(
            [
                "Request processed successfully",
                "User request completed",
                "Data fetched successfully",
                "Operation completed without issues",
            ]
        ),
        "request_id": str(uuid.uuid4()),
        "latency_ms": random.randint(50, 200),
        "status_code": random.choices(
            [200, 301],
            weights=[0.85, 0.15],
        )[0],
        "is_anomaly": False,
        "anomaly_type": None,
    }


# ----------------------------
# ANOMALOUS LOG
# ----------------------------
def generate_anomalous_log():
    anomaly_type = random.choice(
        [
            "latency_spike",
            "server_error",
            "critical_failure",
            "weird_behavior",
            "timeout_burst",
        ]
    )

    base_log = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": "ERROR",
        "service_name": random.choice(
            [
                "auth-service",
                "payment-service",
                "user-service",
                "order-service",
            ]
        ),
        "message": "Anomalous system behavior detected",
        "request_id": str(uuid.uuid4()),
        "latency_ms": 0,
        "status_code": 500,
        "is_anomaly": True,
        "anomaly_type": anomaly_type,
    }

    if anomaly_type == "latency_spike":
        base_log["latency_ms"] = random.randint(2000, 10000)
        base_log["status_code"] = 200
        base_log["message"] = f"Timeout in {base_log['service_name']} after heavy load"

    elif anomaly_type == "server_error":
        base_log["latency_ms"] = random.randint(100, 800)
        base_log["status_code"] = random.choice([500, 503])
        base_log["message"] = f"{fake.catch_phrase()} failed due to internal error"

    elif anomaly_type == "critical_failure":
        base_log["level"] = "CRITICAL"
        base_log["latency_ms"] = random.randint(1000, 5000)
        base_log["status_code"] = 500
        base_log["message"] = "Critical system failure in core module"

    elif anomaly_type == "weird_behavior":
        base_log["latency_ms"] = random.randint(300, 3000)
        base_log["status_code"] = random.choice([500, 502, 503])
        base_log["message"] = fake.text(max_nb_chars=80)

    elif anomaly_type == "timeout_burst":
        base_log["latency_ms"] = random.randint(5000, 15000)
        base_log["status_code"] = 504
        base_log["message"] = "Gateway timeout: cascading failure detected"

    return base_log


# ----------------------------
# GENERATOR CORE
# ----------------------------
def generate_logs(count: int, anomaly_ratio: float):
    logs = []

    for _ in range(count):
        if random.random() < anomaly_ratio:
            logs.append(generate_anomalous_log())
        else:
            logs.append(generate_normal_log())

    return logs


# ----------------------------
# CLI ARGS
# ----------------------------
def parse_args():
    parser = argparse.ArgumentParser(description="Synthetic production-like log generator")

    parser.add_argument(
        "--count",
        type=int,
        required=True,
        help="Number of logs to generate",
    )

    parser.add_argument(
        "--anomaly-ratio",
        type=float,
        default=0.05,
        help="Fraction of anomalies (default: 0.05)",
    )

    parser.add_argument(
        "--output-file",
        type=str,
        default=None,
        help="Output file path (JSONL format). If not set, prints to stdout.",
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducibility",
    )

    return parser.parse_args()


# ----------------------------
# MAIN
# ----------------------------
def main():
    args = parse_args()

    # reproducibility
    if args.seed is not None:
        random.seed(args.seed)
        fake.seed_instance(args.seed)

    logs = generate_logs(args.count, args.anomaly_ratio)

    output = "\n".join(json.dumps(log) for log in logs)

    if args.output_file:
        with open(args.output_file, "w") as f:
            f.write(output)
    else:
        print(output)


if __name__ == "__main__":
    main()
