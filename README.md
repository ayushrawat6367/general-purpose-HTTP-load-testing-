# HTTP Load Testing and Benchmarking Library

Introduction:

This project is a general-purpose HTTP load-testing and benchmarking library designed to evaluate the performance and reliability of web services. Developed in Python, the library facilitates generating HTTP requests at a fixed rate and reporting key performance metrics such as latencies and error rates. By simulating real-world usage patterns, this tool helps developers and system administrators understand how their services perform under load and identify potential points of failure.

The key features of this project include:

Generating HTTP requests at a user-defined QPS (Queries Per Second)
Reporting detailed latency statistics (average, min, max, percentiles)
Handling and reporting error rates

Prerequisites

Python 3.7 or higher
Docker (optional, for containerized usage)

Installation:

1. Clone the repository:

git clone https://github.com/ayushrawat6367/general-purpose-HTTP-load-testing-.git
cd general-purpose-HTTP-load-testing-

2. Create and activate a virtual environment:

python3 -m venv venv  # Use 'python' instead of 'python3' if needed
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Run the HTTP load tester:

python main.py python main.py http://example.com --qps 5 --num-requests 20 --interval 5
http://example.com: URL to test (example)
--qps 5: Specifies the number of queries per second. In this example, it's set to 5 queries per second.
--num-requests 20: Defines the total number of requests to be sent during the test. Here, it's set to 20 requests.
--interval 5: Sets the interval in seconds for reporting the test results. This example uses an interval of 5 seconds

5. Output:
The script will output statistics such as average latency, minimum latency, maximum latency, percentiles, and error rates.

6. Run the unit tests:

pytest

7. Build the Docker image:

docker build -t http-load-tester .

8. Run the Docker container:

docker run http-load-tester http://example.com --qps 5 --num-requests 20 --interval 5

This ensures that we have all the necessary tools and dependencies to use and extend the HTTP load-testing library effectively.

Project Structure:

README.md: Project documentation.
requirements.txt: List of dependencies.
Dockerfile: Instructions to create a Docker image.
main.py: Main script for running the load tester.
test_main.py: Unit tests for the load tester.
venv: Virtual environment directory (if created).



