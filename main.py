import argparse
import requests
import time
import threading
import numpy as np


def send_request(url):
    start_time = time.time()
    try:
        response = requests.get(url)
        latency = time.time() - start_time
        return latency, response.status_code
    except requests.RequestException as e:
        return None, str(e)
    
def calculate_statistics(latencies):
    avg_latency = np.mean(latencies)
    min_latency = np.min(latencies)
    max_latency = np.max(latencies)
    p50_latency = np.percentile(latencies, 50)
    p95_latency = np.percentile(latencies, 95)
    p99_latency = np.percentile(latencies, 99)

    return avg_latency, min_latency, max_latency, p50_latency, p95_latency, p99_latency


def main():
    parser = argparse.ArgumentParser(description='HTTP Load Testing Tool')
    parser.add_argument('url', type=str, help='The HTTP address to test')
    parser.add_argument('--qps', type=int, default=1, help='Queries per second')
    parser.add_argument('--num-requests', type=int, default=100, help='Number of requests to send')
    parser.add_argument('--interval', type=int, default=5, help='Interval in seconds for reposrting results')
    args = parser.parse_args()

    # print(f'Testing URL: {args.url} with QPS: {args.qps}')
    latencies = []
    # errors = 0
    error_counts = {'network': 0, 'http': 0}
    total_requests = 0

    def worker():
        nonlocal total_requests
        for _ in range(args.num_requests):
            latency, status = send_request(args.url)
            if latency is not None:
                latencies.append(latency)
                if isinstance(status, int) and status >= 400:
                    error_counts['http'] += 1
            else:
                error_counts['network'] += 1
            total_requests += 1
            time.sleep(1 / args.qps)
    
    thread = threading.Thread(target=worker)
    thread.start()

    start_time = time.time()

    try:
        while thread.is_alive():
            time.sleep(args.interval)
            elapsed_time = time.time() - start_time
            if latencies:
                avg_latency, min_latency, max_latency, p50_latency, p95_latency, p99_latency = calculate_statistics(latencies)
                print(f'Time Elapsed: {elapsed_time:.2f}s, Total Requests: {total_requests}, '
                      f'Average Latency: {avg_latency:.2f}s, Min Latency: {min_latency:.2f}s, '
                      f'Max Latency: {max_latency:.2f}s, 50th Percentile: {p50_latency:.2f}s, '
                      f'95th Percentile: {p95_latency:.2f}s, 99th Percentile: {p99_latency:.2f}s, '
                      f'Network Errors: {error_counts["network"]}, HTTP Errors: {error_counts["http"]}')
            else:
                print(f'Time Elapsed: {elapsed_time:.2f}s, Total Requests: {total_requests}, '
                      f'Network Errors: {error_counts["network"]}, HTTP Errors: {error_counts["http"]}')
    except KeyboardInterrupt:
        print('Stopping load test')

    thread.join()


if __name__ == '__main__':
    main()