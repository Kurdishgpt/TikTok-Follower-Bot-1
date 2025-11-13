
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyfiglet
from time import sleep
import os
from twocaptcha import TwoCaptcha

def loop1():
    global i
    sleep(10)
    try:
        driver.find_element_by_xpath("//*[@id=\"main\"]/div/div[4]/div/button").click()
    except:
        print("Captcha detected. Attempting AI solve...")
        if captcha_solver:
            solve_captcha_automatically()
            sleep(3)
        else:
            print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop1()
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/div/button").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        sleep(10)
        driver.refresh()
        i += 1
        total = i * 500
        print("Views success delivered! Total", total,"views")
        sleep(360)
        loop1()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(20)
        loop1()

def loop2():
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
    except:
        print("Captcha detected. Attempting AI solve...")
        if captcha_solver:
            solve_captcha_automatically()
            sleep(3)
        else:
            print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop2()
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div/div/button").click()
        sleep(10)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div[1]/div/form/button").click()
        sleep(10)
        hearts = driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text
        sleep(55)
        print(hearts," Success delivered! Thank me with a $ 1 donation on GitHub")
        sleep(100)
        driver.refresh()
        sleep(200)
        loop2()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(355)
        loop2()

def loop3():
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[3]/div/button").click()
    except:
        print("Captcha detected. Attempting AI solve...")
        if captcha_solver:
            solve_captcha_automatically()
            sleep(3)
        else:
            print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop3()
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/form/div/div/button").click()
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/form/button").click()
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/div/form/ul/li/div/button").click()
        sleep(47)
        driver.refresh()
        print("Success delivered! Thank me with a $ 1 donation on GitHub")
        loop3()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(50)
        loop3()

def loop4():
    sleep(20)
    wait_time = 660 #11 minutes
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click() #Followers
    except:
        print("Captcha detected. Attempting AI solve...")
        if captcha_solver:
            solve_captcha_automatically()
            sleep(3)
        else:
            print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop4()
    try:
        sleep(20)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/form/div/input").send_keys(vidUrl) #Write
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid\"]/div/div/div/form/div/div/button").click() #Search
        sleep(20)
        driver.find_element_by_xpath("//*[@id=\"c2VuZF9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button").click() #AddFollowers
        sleep(wait_time/3)
        print("Success delivered! Thank me with a $ 1 donation on GitHub")
        sleep(wait_time/3)
        driver.refresh()
        sleep(wait_time/3)
        loop4()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(wait_time)
        loop4()

def loop5():
    sleep(20)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button").click()
    except:
        print("Captcha detected. Attempting AI solve...")
        if captcha_solver:
            solve_captcha_automatically()
            sleep(3)
        else:
            print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop5()
    try:
        sleep(2000)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/form/div/input").send_keys(vidUrl) # Write
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/form/div/div/button").click() # Search
        sleep(20)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/div/div/div/div[1]/div/form/button").click() # AddShares
        sleep(60)
        print("Shares sent! Thank me with a $ 1 donation on GitHub")
        sleep(1700)
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(300)
        loop5()

def loop6():
    sleep(1000)
    driver.refresh()
    print("Reload")
    loop5()

print("Author: https://github.com/NoNameoN-A")

# Get settings from environment variables (can be set in Replit Secrets)
vidUrl = os.getenv("TIKTOK_VIDEO_URL", "https://www.tiktok.com/@github_nonameon/video/6898692248968400130")
bot_choice = os.getenv("BOT_CHOICE", "")
captcha_api_key = os.getenv("CAPTCHA_API_KEY", "")

# Initialize 2Captcha solver if API key is provided
captcha_solver = None
if captcha_api_key:
    captcha_solver = TwoCaptcha(captcha_api_key)
    print("✓ AI Captcha Solver enabled!")
else:
    print("⚠ No CAPTCHA_API_KEY found - you'll need to solve captchas manually")
    print("  Get one at: https://2captcha.com (Starting at $0.50 per 1000 captchas)")

def solve_captcha_automatically():
    """Automatically solve reCAPTCHA using 2Captcha AI service"""
    if not captcha_solver:
        print("⚠ Captcha solver not configured. Waiting for manual solve...")
        return False
    
    try:
        print("🤖 AI is solving the captcha...")
        # Find the reCAPTCHA iframe and get the site key
        driver.switch_to.default_content()
        
        # Wait for reCAPTCHA to load
        try:
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='google.com/recaptcha']"))
            )
            driver.switch_to.default_content()
        except:
            pass
        
        # Get the site key from the page
        site_key = driver.execute_script("""
            var iframe = document.querySelector('iframe[src*="google.com/recaptcha"]');
            if (iframe) {
                var src = iframe.src;
                var match = src.match(/k=([^&]*)/);
                return match ? match[1] : null;
            }
            return null;
        """)
        
        if site_key:
            print(f"🔑 Found captcha site key, solving...")
            result = captcha_solver.recaptcha(
                sitekey=site_key,
                url=driver.current_url
            )
            
            # Inject the solution into the page
            driver.execute_script(f"""
                document.getElementById('g-recaptcha-response').innerHTML = '{result['code']}';
            """)
            
            print("✅ Captcha solved by AI!")
            sleep(2)
            return True
        else:
            print("⚠ Could not find captcha site key")
            return False
            
    except Exception as e:
        print(f"⚠ Captcha solving failed: {str(e)}")
        print("  Waiting for manual solve...")
        return False

if bot_choice:
    bot = int(bot_choice)
    print(f"Using bot choice from environment: {bot}")
else:
    bot = int(input("What do you want to do?\n1 - Auto views(500)\n2 - Auto hearts\n3 - Auto (FIRST) comments heart\n4 - Auto followers\n5 - Auto Share\n6 - Simple reload\n"))
i = 0

print(f"Starting bot with video URL: {vidUrl}")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# Performance optimizations to reduce VNC lag
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--window-size=1280,720')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://vipto.de/")

if bot == 1:
    loop1()
elif bot == 2:
    loop2()
elif bot == 3:
    loop3()
elif bot == 4:
    loop4()
elif bot == 5:
    loop5()
elif bot == 6:
    loop5()
else:
    print("You can insert just 1, 2, 3, 4, 5 or 6")
