import requests
import json

BASE_URL = "http://localhost:8080"

def menu():
    print("\nSelect an API route to call:")
    print("1. Root greeting (/)")
    print("2. Hello with query (/Hello?name=John&age=30)")
    print("3. Hello with path (/hello/John/30)")
    print("4. Hello via JSON POST (/hello_personclass)")
    print("5. Get time (/time)")
    print("6. Greet with city (/greet?name=John&city=Boston)")
    print("7. Square a number (/Square?number=5)")
    print("8. Reverse string (/reverse?string=test)")
    print("9. Status check (/status?is_online=true)")
    print("10. User info (/user/1)")
    print("11. Header info (/header-info)")
    print("12. Cookie info (/cookie-info)")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "0":
            break

        try:
            match choice:
                case "1":
                    print(requests.get(f"{BASE_URL}/").json())
                case "2":
                    print(requests.get(f"{BASE_URL}/Hello", params={"name": "John", "age": 30}).json())
                case "3":
                    print(requests.get(f"{BASE_URL}/hello/John/30").json())
                case "4":
                    payload = {"name": "John", "age": 30}
                    print(requests.post(f"{BASE_URL}/hello_personclass", json=payload).json())
                case "5":
                    print(requests.get(f"{BASE_URL}/time").json())
                case "6":
                    print(requests.get(f"{BASE_URL}/greet", params={"name": "John", "city": "Boston"}).json())
                case "7":
                    print(requests.get(f"{BASE_URL}/Square", params={"number": 5}).json())
                case "8":
                    print(requests.get(f"{BASE_URL}/reverse", params={"string": "Cloud"+ "Computing"}).json())
                case "9":
                    print(requests.get(f"{BASE_URL}/status", params={"is_online": "true"}).json())
                case "10":
                    print(requests.get(f"{BASE_URL}/user/1").json())
                case "11":
                    headers = {"User-Agent": "CustomBrowser/1.0"}
                    print(requests.get(f"{BASE_URL}/header-info", headers=headers).json())
                case "12":
                    cookies = {"session_id": "abc123"}
                    print(requests.get(f"{BASE_URL}/cookie-info", cookies=cookies).json())
                case _:
                    print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
