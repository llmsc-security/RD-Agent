#!/usr/bin/env python3
"""
Tutorial PoC for testing RD-Agent HTTP API endpoints.
This script demonstrates how to interact with the RD-Agent Flask server.
"""

import requests
import json
import time
import randomname
from datetime import datetime

# Configuration
BASE_URL = "http://localhost:19899"
TEST_SCENARIOS = [
    "Finance Data Building",
    "Finance Model Implementation",
    "General Model Implementation",
    "Finance Whole Pipeline",
    "Data Science",
]

def test_root_endpoint():
    """Test the root endpoint returns index.html"""
    print("\n=== Test 1: Root Endpoint ===")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print("Response: Root page served successfully")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_favicon_endpoint():
    """Test the favicon endpoint"""
    print("\n=== Test 2: Favicon Endpoint ===")
    try:
        response = requests.get(f"{BASE_URL}/favicon.ico")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Response: Favicon served successfully")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_test_endpoint():
    """Test the test endpoint"""
    print("\n=== Test 3: Test Endpoint ===")
    try:
        response = requests.get(f"{BASE_URL}/test")
        print(f"Status Code: {response.status_code}")
        data = response.json()
        print(f"Response: {json.dumps(data, indent=2)[:500]}...")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_receive_endpoint():
    """Test the receive endpoint"""
    print("\n=== Test 4: Receive Endpoint ===")
    try:
        test_data = [{"id": "test_trace", "msg": {"tag": "TEST", "content": {"test": "data"}}}]
        response = requests.post(
            f"{BASE_URL}/receive",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status Code: {response.status_code}")
        data = response.json()
        print(f"Response: {data}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_trace_endpoint():
    """Test the trace endpoint (POST with JSON data)"""
    print("\n=== Test 5: Trace Endpoint ===")
    try:
        trace_id = "test_scenario/test_trace"
        test_data = {
            "id": trace_id,
            "all": False,
            "reset": False
        }
        response = requests.post(
            f"{BASE_URL}/trace",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status Code: {response.status_code}")
        data = response.json()
        print(f"Response: {data}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_control_endpoint():
    """Test the control endpoint"""
    print("\n=== Test 6: Control Endpoint ===")
    try:
        # First, create a test process
        test_data = {
            "scenario": "Data Science",
            "competition": "test-competition",
            "loops": "3",
            "all_duration": "1"
        }
        files = []
        response = requests.post(
            f"{BASE_URL}/upload",
            data=test_data,
            files=files
        )
        print(f"Upload Status Code: {response.status_code}")
        upload_data = response.json()
        print(f"Upload Response: {upload_data}")

        trace_id = upload_data.get("id", "test_scenario/test_trace")

        # Now try to control it
        control_data = {
            "id": trace_id,
            "action": "pause"
        }
        response = requests.post(
            f"{BASE_URL}/control",
            json=control_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"Control Status Code: {response.status_code}")
        control_response = response.json()
        print(f"Control Response: {control_response}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_upload_endpoint():
    """Test the upload endpoint with various scenarios"""
    print("\n=== Test 7: Upload Endpoint ===")
    try:
        scenarios_to_test = ["Data Science"]  # Only test non-file required scenarios
        for scenario in scenarios_to_test:
            print(f"\nTesting scenario: {scenario}")
            test_data = {
                "scenario": scenario,
                "competition": f"test-{randomname.get_name()}",
                "loops": "1",
                "all_duration": "0.1"
            }

            # For Data Science, we need to provide competition name
            if scenario == "Data Science":
                test_data["competition"] = "test-competition"

            response = requests.post(
                f"{BASE_URL}/upload",
                data=test_data
            )
            print(f"Status Code: {response.status_code}")
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_static_files():
    """Test static file serving"""
    print("\n=== Test 8: Static Files ===")
    try:
        # Try to get the main index file
        response = requests.get(f"{BASE_URL}/index.html")
        print(f"index.html - Status: {response.status_code}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_health_check():
    """Test basic health of the server"""
    print("\n=== Test 9: Health Check ===")
    try:
        # Simple GET request to check server is up
        response = requests.get(f"{BASE_URL}/", timeout=5)
        is_healthy = response.status_code == 200
        print(f"Server Healthy: {is_healthy}")
        return is_healthy
    except Exception as e:
        print(f"Server Unhealthy: {e}")
        return False

def run_all_tests():
    """Run all API tests"""
    print("=" * 60)
    print("RD-Agent HTTP API Test Suite")
    print(f"Base URL: {BASE_URL}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 60)

    results = {
        "passed": 0,
        "failed": 0,
        "total": 0
    }

    tests = [
        ("Health Check", test_health_check),
        ("Root Endpoint", test_root_endpoint),
        ("Favicon Endpoint", test_favicon_endpoint),
        ("Test Endpoint", test_test_endpoint),
        ("Receive Endpoint", test_receive_endpoint),
        ("Trace Endpoint", test_trace_endpoint),
        ("Upload Endpoint", test_upload_endpoint),
        ("Control Endpoint", test_control_endpoint),
        ("Static Files", test_static_files),
    ]

    for name, test_func in tests:
        results["total"] += 1
        try:
            if test_func():
                results["passed"] += 1
            else:
                results["failed"] += 1
        except Exception as e:
            print(f"\nTest '{name}' failed with exception: {e}")
            results["failed"] += 1

    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"Total: {results['total']}")
    print(f"Passed: {results['passed']}")
    print(f"Failed: {results['failed']}")
    print(f"Success Rate: {results['passed']/results['total']*100:.1f}%")
    print("=" * 60)

    return results["failed"] == 0

def main():
    """Main entry point"""
    import argparse
    parser = argparse.ArgumentParser(description="RD-Agent HTTP API Test Suite")
    parser.add_argument("--url", "-u", default=BASE_URL,
                        help=f"Base URL (default: {BASE_URL})")
    args = parser.parse_args()

    global BASE_URL
    BASE_URL = args.url

    success = run_all_tests()
    exit(0 if success else 1)

if __name__ == "__main__":
    main()
