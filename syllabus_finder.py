import requests

course_code = input("Write course code: ").upper()
section = input("Write section code (01, 02 etc.): ")
summer = input("Include summer semester? Y/N? ").upper()
summer_check = True if summer == "Y" else False

liste = ["2021-2022", "2020-2021", "2019-2020", "2018-2019", "2017-2018"]
for i in liste:
    term = 3 if summer_check else 2
    for j in range(1, term + 1):
        name = f"{i}-{j} - {course_code + section}"
        st = ".pdf"
        response = requests.get(f"https://registration.boun.edu.tr/scripts/instructor/coursedescriptions/{i}-{j}/{course_code + section}.PDF")
        response.raise_for_status()
        if "File not found!" in str(response.content):
            response = requests.get(f"https://registration.boun.edu.tr/scripts/instructor/coursedescriptions/{i}-{j}/{course_code + section}.DOCX")
            response.raise_for_status()
            st = ".docx"
        if "File not found!" in str(response.content):
            print(f"{name} Syllabus not found")
        else:
            print(f"{name} Syllabus found")
            with open(name + st, 'wb') as f:
                f.write(response.content)