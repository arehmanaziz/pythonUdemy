import webbrowser
#
# webbrowser.open("https://www.python.org/", new=1)
#
# help(webbrowser)
chrome = webbrowser.get('chrome')
chrome.open_new_tab("https://www.python.org/")

# safari = webbrowser.get(using='safari')
# safari.open("https://www.python.org/")
