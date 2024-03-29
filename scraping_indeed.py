from bs4 import BeautifulSoup
import requests

url = 'https://remote.co/remote-jobs/developer/'
base_url = 'https://remote.co'
#url = 'https://au.indeed.com/?from=jobsearch-empty-whatwhere' 

status = requests.get(url)
soup = BeautifulSoup(status.content, 'html.parser')
result_job = soup.find_all(class_='card')[1] # find the block that contains the jobs and focus and it
#print(result_job.prettify())
jobs_posting = result_job.find_all('a', class_='card') # all jobs
# but we want to focus on python developer jobs so we have to filter a little bit
"""
    for n in jobs_posting:
    filtering = n.p.span.text
    job_want = 'python'
    #if job_want in filtering.lower():
        #pri
        #print(f'{filtering}')
        #print(n.get_text().replace('  ', ''))

    #for n in python_jobs:
    #print(n.text)
    
"""
# filter jobs result with python in the title
python_jobs = result_job.find_all('span', string=lambda text: 'python' in text.lower())
for job in python_jobs:
    root = job.parent.parent.parent.parent.parent.parent
    title = root.find('span')
    date_pub = root.find('date').text
    company = root.find('p', class_='m-0 text-secondary').text
    contract_type = root.find_all('small')[1].text
    position_modality = root.find_all('small')[2].text
    job_location = root.find_all('img', class_='card-img')[0]['alt']
    #root_parent = root.parent
    #link = root_parent.find('a', class_='card m-0 border-left-0 border-right-0 border-top-0 border-bottom')['href']
    print(title.text)
    print(company.split()[0])
    print(base_url + root['href'])
    #print(base_url + link)
    print(contract_type)
    print(position_modality)
    print(job_location)
    print(date_pub)
    print()
