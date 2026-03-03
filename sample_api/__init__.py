import sys
import os

# Add the submodule directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "sample-api"))

from sample_api.hello import hello_world


def call_api():
    print(hello_world())


if __name__ == "__main__":
    call_api()
