"""Preprocessing entrypoint."""

from ml.data.preprocessing import run_preprocessing


def main() -> None:
    features, _, _ = run_preprocessing()
    print(features.shape)


if __name__ == "__main__":
    main()
