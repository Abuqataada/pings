import requests

def main():
    url = "https://psstech.com.ng/health"
    try:
        response = requests.get(url, timeout=10)
        print("Successfully pinged:", url)
        print("Status Code:", response.status_code)
        print("Response Body:", response.text[:200])  # print first 200 chars
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
