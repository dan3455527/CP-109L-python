interview_letter = """
Dear {} Applicant,

Thank you for applying for the position of engineer with YZ Company. We are impressed 
with your expertise in microcontroller programming.

We would like to invite you to come to our office to interview for the position. Your 
interview has been scheduled for {}, at Room 3205, Building 3, 135 Yuan-dong Road, 
Zhong-Li District, Tao-Yuan City.

Please call me at 03-463-8800 or email me at johnsmith@yz.com.tw if you have any 
questions or need to reschedule.

Sincerely,
John Smith
Regional Manager
YZ Company

"""

N = int(input("input the count of name be entered"))
name_list = []
for i in range(N):
    name = input(f"input name no.{i} : ")
    name_list.append(name)
name_list.sort()

for j in range(N):
    if j % 2 == 0:
        time = "2022/01/10 15:30"
        name = name_list[j]
        print(interview_letter.format(name, time))
        print("="*72)
        pass
    else:
        time = "2022/01/11 9:30"
        name = name_list[j]
        print(interview_letter.format(name, time))
        print("="*72)
        pass



