import json

def create_resume():
    # Collect user input for each component of the resume
    # Using cvil IDL
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    summary = input("Enter a summary of your qualifications: ")
    objective = input("Enter an objective: ")

    # Create a dictionary to store the resume data
    resume_data = {
        "name": name,
        "email": email,
        "phone": phone,
        "summary": summary,
	    "objective": objective,
        "experience": [],
        "education": [],
        "skills": []
    }

    # Collect user input for experience section
    num_experience = int(input("How many past experiences would you like to add? "))
    for i in range(num_experience):
        print(f"Experience {i+1}:")
        title = input("\tTitle: ")
        company = input("\tCompany: ")
        start_date = input("\tStart Date (YYYY-MM-DD): ")
        end_date = input("\tEnd Date (YYYY-MM-DD): ")
        responsibilities = input("\tResponsibilities: ")

        experience_data = {
            "title": title,
            "company": company,
            "start_date": start_date,
            "end_date": end_date,
            "responsibilities": responsibilities
        }
        
        # Add experience data to the resume data
        resume_data["experience"].append(experience_data)

    # Collect user input for education section
    num_education = int(input("How many education entries would you like to add? "))
    for i in range(num_education):
        print(f"Education {i+1}:")
        institution = input("\tInstitution: ")
        major = input("\tMajor: ")
        degree = input("\tDegree: ")
        graduation_date = input("\tGraduation Date (YYYY): ")

    education_data = {
	    "institution": institution,
	    "major": major,
	    "degree": degree,
	    "graduation_date": graduation_date
	}

	# Add education data to the resume data
    resume_data["education"].append(education_data)

# Collect user input for skills section
    num_skills = int(input("How many skills entries would you like to add? "))
    for i in range(num_skills):
        print(f"Skills {i+1}:")
        name =   input("\tSkill Name: ")
        aptitude = input("\tAptitude (Scale 1/10): ")
        years_exp = input("\tYears of Experience: ")
        training = input("\tSource of Training: ")

    skills_data = {
        "name": name,
        "aptitude": aptitude,
        "years_exp": years_exp,
        "training": training
    }

    # Add skills data to the resume data
    resume_data["skills"].append(num_skills)