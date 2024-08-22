from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver import Keys

from time import sleep


desired_capabilities = {
    "platformName": "Android",
    "automationName": 'uiautomator2',
    "platformVersion": "10",
    "deviceName": "Android Emulator",
    "appActivity": "org.wikipedia.main.MainActivity",
    "appPackage": "org.wikipedia",
    "app": "/Users/jkwak/Desktop/QA/python-selenium-automation/mobile_app/wikipedia.apk"
    # "appActivity": "com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity",
    # "appPackage": "com.google.android.youtube",
    # "app": "/Users/jkwak/Desktop/QA/python-selenium-automation/mobile_app/split_config.arm64_v8a.apk"
    # """
    # adb shell pm list packages for available packages
    # adb shell pm list packages -f for app apk files
    # adb pull /data/app/com.google.android.youtube-I9n9Ybv0agQgokR0kvhyYQ==/split_config.arm64_v8a.apk for app package download
    # adb shell cmd package dump com.google.android.youtube |grep -A 1 "Activity" for appActivity
    # """
    # "appActivity": "org.wikipedia.main.MainActivity",
    # "appPackage": "org.wikipedia",
    # "app": "/Users/jkwak/Desktop/QA/python-selenium-automation/mobile_app/wikipedia.apk"
}

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)

driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.implicitly_wait(5)

# Click Skip btn
driver.find_element(AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button').click()

# Click Search icon
driver.find_element(AppiumBy.XPATH, "//*[@content-desc='Search Wikipedia']").click()

# Populate search field:
driver.find_element(AppiumBy.ID, 'org.wikipedia:id/search_src_text').send_keys('Python (programming language)')

# Verification
expected_result = 'Python (programming language)'
actual_result = driver.find_element(AppiumBy.ID, 'org.wikipedia:id/page_list_item_title').text

assert actual_result == expected_result, f'Expected {expected_result} did not match actual {actual_result}'


# driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Search YouTube"]').click()
# search_input = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.google.android.youtube:id/search_edit_text"]')
# search_input.send_keys("jinny's kitchen season 2")
# driver.press_keycode(66)
sleep(5)

# # Populate search field:
# driver.find_element(AppiumBy.ID, 'org.wikipedia:id/search_src_text').send_keys('Python (programming language)')
#
# # Verification
# expected_result = 'Python (programming language)'
# actual_result = driver.find_element(AppiumBy.ID, 'org.wikipedia:id/page_list_item_title').text
#
# assert actual_result == expected_result, f'Expected {expected_result} did not match actual {actual_result}'

driver.quit()