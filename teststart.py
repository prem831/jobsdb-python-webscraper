import csv
with open('job_details.csv', mode='w+') as details_file:
    details_writer = csv.writer(details_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    details_writer.writerow(
        ['Title of the position', 'Company/Employer', 'Job Function', 'Industry', 'Benefits', 'Career Level',
         'Years of experience', 'Qualification', 'Job Type'])