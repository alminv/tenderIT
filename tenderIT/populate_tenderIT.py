import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tenderIT.settings')

import django
django.setup()

from TenderITApp.models import Company, Project, Rating, ProjectApplication

def populate():
    company1 = add_company('06382444', "IT SOLUTIONS LTD", "Canal View 2a",
                           "Chester", "United Kingdom", "CH3 6AN", "itsolutions@gmail.com",
                           "48853124568", "www.itsolutions.co.uk", "itsolutions", "it1234")

    company2 = add_company("04217916", "SKYSCANNER LIMITED", "Fore Street",
                           "London", "United Kingdom", "EC2Y 5EJ", "info@scyscanner.co.uk",
                           "44882156785", "www.skyscanner.co.uk", "skyscanner", "sky1234")

    company3 = add_company("SC327000", "Bank of Scotland", "The Mound", "Edinburgh", "United Kingdom", "EH1 1YZ", "info@bankofscotland.co.uk", "48573554897", "www.bankofscotland.co.uk", "bankofscotland", "bos1234")

    company4 = add_company("4201193140009", "Devlogic D.O.O", "Kolodvorska 11a", "Sarajevo", "Bosnia and Herzegovina", "71000", "info@devlogic.ba", "003873312346", "www.devlogic.ba", "devlogic", "dev1234")

    project1 = add_project(company3, "Web page development", "Develop a web page for our company", 500000, '2016-03-01', "2016-09-01")

    project2 = add_project(company1, "ERP System add on", "Create an accouting add on for the existing ERP system. Add on needs to be able to connect to the employees github account and count the number of commits.", 100000, "2016-04-15", "2016-12-31")

    project3 = add_project(company2, "Azerbaijan Airlines API analyzer", "Develop an app that will connect to the Azerbaijan Airlines API and collect details about flights. App needs to organize collected information so that it can be used in our existing systems.", 80000, "2016-05-01", "2016-08-30")

    add_application(project1, company4, 450000, "We would love to work on this project.")
    add_application(project2, company4, 95960, "This project looks really interesting. We will dedicate our best programmers to this project and make sure we finish the necessary work in time.")
    add_application(project1, company1, 460000, "We will deliver the best solution.")

    add_rating(company1, company4, 5, "Great experience.")
    add_rating(company2, company4, 4, "Very good job.")
    add_rating(company4, company1, 5, "Excellent employer.")
    add_rating(company3, company2, 2, "Poor job, had a lot of problems on our project.")
    add_rating(company3, company4, 5, "Very professional. Great people and great company. Highly recommended to work with.")

    for c in Company.objects.all():
        print c
    for p in Project.objects.all():
	print p
    for a in ProjectApplication.objects.all():
  	print a
    for r in Rating.objects.all():
	print r

def add_company(nationalID, name, street, city, country, postcode, email, phone, website, username, password):
    c = Company.objects.get_or_create(nationalID=nationalID)[0]
    c.name = name
    c.street = street
    c.city = city
    c.country = country
    c.postcode = postcode
    c.email = email
    c.phone = phone
    c.website = website
    c.username = username
    c.password = password
    c.save()
    return c

def add_project(company, title, description, budget, startDate, endDate):
    p = Project.objects.get_or_create(company=company, title=title, budget=budget, startDate=startDate, endDate=endDate)[0]
    p.description = description; 
    p.save()
    return p

def add_application(project, applicant, price, description):
    a = ProjectApplication.objects.get_or_create(project=project, applicant=applicant, price=price)[0]
    a.description = description
    a.save()
    return a;

def add_rating(provider, receiver, value, comment):
    r = Rating.objects.get_or_create(provider=provider, receiver=receiver, value=value, comment=comment)[0]
    r.save()
    return r

if __name__ == '__main__':
   	print "Starting tender IT population script..."
   	populate()