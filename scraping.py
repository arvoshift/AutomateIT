from lxml import html
import requests

# create page object which gets() the github pricing page
page = requests.get('https://github.com/pricing')

# interpret the string page.content as html and assign it to the tree object.
tree = html.fromstring(page.content)

print("Page object:", tree)

# what does xpath do?
plans = tree.xpath('//h2[@class="alt-h3"]/text()')
pricing = tree.xpath('//span[@class="local-currency"]/text()')

print("Plans:", plans, "\nPricing:", pricing)


# TODO(benp): scrape from other sites.

# EOF
