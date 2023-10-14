from selenium import webdriver

# Given a default runninng browser
browser = webdriver.Firefox()
browser.get("http://localhost:8000")

# The title of the default page should be "Congratulations"
assert("Congratulations!" in browser.title)
print("OK")