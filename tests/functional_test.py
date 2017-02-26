from splinter import Browser

with Browser('chrome') as browser:
    # Visit URL
    base_url = "http://127.0.0.1:5000"
    browser.visit(base_url)
    # Find and click the 'search' button
    assert(browser.is_text_present('Starfighter'))
