import csv
import requests
import bs4

# with open('job_details.csv', mode='w+') as details_file:
#     details_writer = csv.writer(details_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#     details_writer.writerow(
#         ['Title of the position', 'Company/Employer', 'Job Function', 'Industry', 'Benefits', 'Career Level',
#          'Years of experience', 'Qualification', 'Job Type'])

base_url = "https://hk.jobsdb.com/hk/en/job/job-"
# job_id_num = 100003008438605
csv_columns = ['Title of the position', 'Company/Employer', 'Job Function', 'Industry', 'Benefits', 'Career Level',
               'Years of experience', 'Qualification', 'Job Type']
csv_file = "job_details.csv"


# url = base_url + str(job_id_num)


# def get_url(job_id):
#     return base_url + job_id.__str__()


def get_job_details(url):
    no_str = "Not available"
    result = requests.get(url)
    soup1 = bs4.BeautifulSoup(result.text, "lxml")
    rtn_dict = {'Title of the position': soup1.select("h1")[0].getText(),
                'Company/Employer': soup1.select(".FYwKg._6Gmbl_0")[3].getText()}
    items = [item.getText() for item in soup1.select(".FYwKg.zoxBO_0")]
    try:
        rtn_dict['Job Function'] = items[items.index('Job Functions') + 1]
    except ValueError:
        rtn_dict['Job Function'] = no_str
    try:
        rtn_dict['Industry'] = items[items.index('Industry') + 1]
    except ValueError:
        rtn_dict['Industry'] = no_str
    try:
        rtn_dict['Benefits'] = items[items.index('Benefits & Others') + 1]
    except ValueError:
        rtn_dict['Benefits'] = no_str
    try:
        rtn_dict['Career Level'] = items[items.index('Career Level') + 1]
    except ValueError:
        rtn_dict['Career Level'] = no_str
    try:
        rtn_dict['Years of experience'] = items[items.index('Years of Experience') + 1]
    except ValueError:
        rtn_dict['Years of experience'] = no_str
    try:
        rtn_dict['Qualification'] = items[items.index('Qualification') + 1]
    except ValueError:
        rtn_dict['Qualification'] = no_str
    try:
        rtn_dict['Job Type'] = items[items.index('Job Type') + 1]
    except ValueError:
        rtn_dict['Job Type'] = no_str
    return rtn_dict


def csv_append(url1):
    l_url = url1
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            # writer.writeheader()
            writer.writerow(get_job_details(l_url))
    except IOError:
        print("I/O error")


def check_url(c_url):
    result = requests.get(c_url)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    return not ("Hmm... we can't seem to load the screen" in soup.getText())


for run_id in range(100003008479000, 100003008479053):
    ch_url = base_url + run_id.__str__()
    print(run_id)
    if check_url(ch_url):
        csv_append(ch_url)
