import unittest
from unittest.mock import patch
import main

class TestHttpLoadTester(unittest.TestCase):

    @patch('main.requests.get')
    def test_send_request_success(self, mock_get):
        mock_get.return_value.status_code = 200
        latency, status = main.send_request('http://example.com')
        self.assertIsNotNone(latency)
        self.assertEqual(status, 200)

    @patch('main.requests.get', side_effect=ConnectionError('Network error'))
    def test_send_request_failure(self, mock_get):
        with self.assertRaises(ConnectionError) as context:
            main.send_request('http://example.com')

        self.assertEqual(str(context.exception), 'Network error')


    def test_calculate_statistics(self):
        latencies = [0.1, 0.2, 0.3, 0.4, 0.5]
        avg_latency, min_latency, max_latency, p50_latency, p95_latency, p99_latency = main.calculate_statistics(latencies)
        self.assertAlmostEqual(avg_latency, 0.3)
        self.assertEqual(min_latency, 0.1)
        self.assertEqual(max_latency, 0.5)
        self.assertAlmostEqual(p50_latency, 0.3)
        self.assertAlmostEqual(p95_latency, 0.5, delta=0.05)
        self.assertAlmostEqual(p99_latency, 0.5, delta=0.05)


if __name__ == '__main__':
    unittest.main()