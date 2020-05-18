

import xlrd 
loc = ("16-5-2020-gamil.xlsx") 
from selenium import webdriver
import threading
import time
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
profile = FirefoxProfile()
from selenium.webdriver import DesiredCapabilities
desired = DesiredCapabilities.FIREFOX
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
options = Options()



def test_logic(username,password,video_url):

   options.headless = True
   PROXY_HOST = "1.1.164.70"
   PROXY_PORT = "8080"
   profile.set_preference("network.proxy.type", 1)
   profile.set_preference("network.proxy.http", PROXY_HOST)
   profile.set_preference("network.proxy.http_port", int(PROXY_PORT))
   profile.set_preference("dom.webdriver.enabled", False)
   profile.set_preference('useAutomationExtension', False)
   driver = webdriver.Firefox(options=options,firefox_profile=profile, desired_capabilities=desired)
        ############## CODING LOGIC ############
   driver.get(video_url)
   time.sleep(7)
   form=driver.find_element_by_link_text("SIGN IN")
   form.click()

   form=driver.find_element_by_id("identifierId")
   form.send_keys(username)

   form=driver.find_element_by_id("identifierNext").click()
   time.sleep(2)
   form=driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
   form.send_keys(password)
   form=driver.find_element_by_id("passwordNext").click()
   time.sleep(15)
   if driver.current_url=='https://myaccount.google.com/signinoptions/recovery-options-collection?utm_source=Web&utm_medium=Web&utm_campaign=interstitial&oev=lytf%3D7%26wvtx%3D2%26trs%3Dli%26stel%3D1&hl=en&continue=https://accounts.google.com/ServiceLogin?continue%3Dhttps%253A%252F%252Fwww.youtube.com%252Fsignin%253Faction_handle_signin%253Dtrue%2526app%253Ddesktop%2526hl%253Den%2526next%253Dhttps%25253A%25252F%25252Fwww.youtube.com%25252Fwatch%25253Fv%25253D_qUID8JFti8%26service%3Dyoutube%26hl%3Den%26authuser%3D0%26passive%3Dtrue%26sarp%3D1%26aodrpl%3D1%26checkedDomains%3Dyoutube%26checkConnection%3Dyoutube%253A226%253A1%26pstMsg%3D1&service=youtube&rapt=AEjHL4OegTNKTAyDjimrygolQI8xiZcwO7ZEnpFJoIDRrQK9lX2eSWPB4X1luNa93cDZxf9Sh65u2D8ZpX6C8uKBqoqnMID2Gw&pli=1':
      form=driver.find_element_by_xpath("/html/body/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div").click()
   time.sleep(15)
   form=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/button').click()


video_url_list=['https://www.youtube.com/watch?v=bIUzjOm18mc','https://www.youtube.com/watch?v=ZX4QAIuxARU','https://www.youtube.com/watch?v=54gUzAMH4NM']
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
N = range(sheet.nrows)
thread_list = list()

for j in range(len(video_url_list)):
    for i in (N):
        t = threading.Thread(name='Test {}'.format(i), target=test_logic((sheet.cell_value(i, 2)),(sheet.cell_value(i, 3)),video_url_list[j]))
        t.start()
        time.sleep(1)
        print (t.name + ' started!')
        thread_list.append(t)

    # Wait for all thre<ads to complete
    for thread in thread_list:
        thread.join()

    print('Test completed!')

#(610) 570-0996
