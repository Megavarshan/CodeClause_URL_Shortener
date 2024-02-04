#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, long_url):
        hash_object = hashlib.md5(long_url.encode())
        short_url = hash_object.hexdigest()[:8]
        self.url_mapping[short_url] = long_url
        return f"short.url/{short_url}"

    def expand_url(self, short_url):
        short_code = short_url.split("/")[-1]
        long_url = self.url_mapping.get(short_code)
        return long_url if long_url else "URL not found"

def main():
    shortener = URLShortener()

    while True:
        print("\nURL Shortener")
        print("1. Shorten URL")
        print("2. Expand Short URL")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            long_url = input("Enter the long URL: ")
            short_url = shortener.shorten_url(long_url)
            print(f"Shortened URL: {short_url}")
        elif choice == '2':
            short_url = input("Enter the short URL: ")
            long_url = shortener.expand_url(short_url)
            print(f"Expanded URL: {long_url}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


# In[ ]:




