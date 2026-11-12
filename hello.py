"""Minimal hello world program."""

GREETING = "Hello, World!"


def greet() -> str:
    """Return the greeting printed by this program."""
    return GREETING


def main() -> None:
    """Print the greeting to standard output."""
    print(greet())


if __name__ == "__main__":
    main()
