import argparse

def run_pipeline(
        test: str = "default_value"
):
    print(f"Test value is: {test}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Template for Pipeline")
    # p.add_argument("--test_value", help="testing to see hoe values are added")

    args = p.parse_args()

    run_pipeline(
        test = args.test_value
    )
