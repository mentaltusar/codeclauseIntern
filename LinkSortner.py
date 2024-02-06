import pyshorteners

sorter = pyshorteners.Shortener()
URL = input("Enter The Url : ")
SORT_URL = sorter.tinyurl.short(URL)
print(f"Your Sorted URL is : {SORT_URL}")
