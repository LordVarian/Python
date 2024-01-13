import bs4, requests

res = requests.get("https://www.amazon.com/Platinum-Battery-48-12v-Automotive-Warranty/dp/B0BXSQDNVZ/?_encoding=UTF8&pd_rd_w=vO6uk&content-id=amzn1.sym.35cab78c-35e3-4fc1-aab0-27eaa6c86063%3Aamzn1.symc.e5c80209-769f-4ade-a325-2eaec14b8e0e&pf_rd_p=35cab78c-35e3-4fc1-aab0-27eaa6c86063&pf_rd_r=9ARYXCT7WT2YK5DB23TZ&pd_rd_wg=5d50o&pd_rd_r=af9d1ed1-8d6c-4a0f-81fc-7f9b6410a8e7&ref_=pd_gw_ci_mcx_mr_hp_atf_m")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('#corePrice_feature_div > div > div > span.a-price.aok-align-center')
print(elems[0].text)
