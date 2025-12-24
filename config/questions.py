'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
'''


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "config/avriResume.pdf"      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "4"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = "https://avri-portfolio.netlify.app/?user=avri"                        # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/avraham-yom-tov-a74525231/"       # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Other"



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 216000          # 18,000 ILS/month * 12 months = 216,000 ILS/year (~$62,000/year)
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 216000            # 18,000 ILS/month * 12 months = 216,000 ILS/year
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 45                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "Backend / Full Stack Engineer | Node.js | Python | AWS | Kubernetes | Docker | React" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
Backend / Full Stack Engineer with extensive experience in Python and Node.js, designing and operating scalable, production-grade microservices and distributed systems in cloud environments. Early adopter of AI and LLM technologies, integrating AI-driven tools into backend systems to improve development velocity, testing, and operational workflows. Proficient in designing RESTful APIs, deploying and operating services on Docker & Kubernetes, and working extensively with AWS cloud services. Hands-on experience with PostgreSQL, Redis, and Elasticsearch, with strong focus on performance, observability, and scalability.
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Dear Hiring Manager,

I am writing to express my interest in this position. As a Backend / Full Stack Engineer with 4+ years of experience at NICE LTD, I have developed extensive expertise in building scalable, production-grade microservices and distributed systems using Node.js, Python, and AWS cloud services.

Throughout my career, I have successfully designed and maintained RESTful APIs, optimized complex distributed workflows (improving system latency by 30% and reducing operational costs by 50%), and deployed production workloads on Docker and Kubernetes. I am also an early adopter of AI and LLM technologies, having integrated AI-driven tools to improve automated testing, monitoring, and incident resolution.

My technical stack includes Node.js, Python, JavaScript, TypeScript, React.js, FastAPI, Django, Express.js, AWS, PostgreSQL, Redis, MongoDB, Elasticsearch, Docker, Kubernetes, Terraform, and CI/CD tools like Jenkins and GitHub Actions. I am passionate about continuous learning and seeking challenging opportunities to drive innovation and deliver impactful solutions.

I look forward to the opportunity to contribute to your team.

Best regards,
Avraham Yom Tov
"""
##> ------ Dheeraj Deshwal : dheeraj9811 Email:dheeraj20194@iiitd.ac.in/dheerajdeshwal9811@gmail.com - Feature ------

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc. 
user_information_all ="""
Avraham Yom Tov - Backend / Full Stack Engineer with 4+ years of experience at NICE LTD. Expert in Node.js, Python, Java, AWS, Kubernetes, Docker, React. Designed and maintained scalable backend microservices and RESTful APIs in distributed architecture. Built cloud-native backend services on AWS including serverless and event-driven architectures. Optimized complex distributed workflow improving system latency by 30% and reducing operational costs by 50%. Deployed production workloads on Docker and Kubernetes. Implemented CI/CD pipelines using Jenkins and GitHub Actions. Integrated LLM-based and AI-driven tools. Skills: Node.js, Python, JavaScript, TypeScript, React.js, FastAPI, Django, Express.js, AWS, Serverless, PostgreSQL, Redis, MongoDB, Elasticsearch, DynamoDB, MySQL, Docker, Kubernetes, Terraform, CloudFormation, Git, Jenkins, GitHub Actions, TDD, Cypress, Jest, Cucumber, Generative AI, MCP. Education: Full stack developer bootcamp at Ort Singalovski College (2020-2022). Location: Israel. Languages: Hebrew (native), English (full professional proficiency). Contact: yoti1492@gmail.com, 053-3300845.
"""
##<
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer
recent_employer = "NICE LTD" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "9"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = False         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive







############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Sai Vignesh Golla
'''
############################################################################################################