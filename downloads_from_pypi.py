# Get total downloads for a package provided via pypi.
# Usage: python3 downloads_from_pypi.py <package_name>

import requests, sys

package_name = sys.argv[1]

request = requests.get("https://pypistats.org/api/packages/cwlab/overall")

data = request.json()["data"]

counts = [d["downloads"] for d in data if d["category"] == "without_mirrors"]
total_counts = sum(counts)

print(f"Total downloads without mirrors: {total_counts}")