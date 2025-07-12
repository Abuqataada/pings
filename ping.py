import requests

def main():
    url = "https://psstech.com.ng/health"
    url_1 = "https://damascusprojects.onrender.com/health"
    try:
        response = requests.get(url, timeout=10)
        print("Successfully pinged:", url)
        print("Status Code:", response.status_code)
        print("Response Body:", response.text[:200])  # print first 200 chars

        response1 = requests.get(url_1, timeout=10)
        print("Successfully pinged:", url_1)
        print("Status Code:", response1.status_code)
        print("Response Body:", response1.text[:200])  # print first 200 chars
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
