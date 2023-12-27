class Choice:
    def __init__(self):
        print("Welcome to the Registration Form")

    def menu(self):
        while True:
            dictio = {
                1: "Enroll",
                2: "select_course",
                3: "exit",
                4: "portal",
            }
            choice = input(f"Enter your choice {dictio}")

            if choice == "1":
                self.enroll()
            elif choice == "2":
                self.select_course()
            elif choice == "exit":
                break
            elif choice == "4":
                self.student_portal()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
            
    def enroll(self):
        self.name = input("Enrollment form \n Enter your name:")
        self.prev_institute = input("Enter your previous institute: ")
        print(f"\nThank you, {self.name}! You are now enrolled.")

    def select_course(self):        
        course_choice = input("Enter your course choice (1. science, 2.enginering, 3.medical, 4.back to manu): ")

        if course_choice == "1":
            self.course = "Science"
            self.fees = input(f"{self.course} has fees 8500, Agree type yes")
        elif course_choice == "2":
            self.course = "Engineering"
            self.fees = input(f"{self.course} has fees 8500, Agree type yes")
        elif course_choice == "3":
            self.course = "Medical"
            self.fees = input(f"{self.course} has fees 8500, Agree type yes")
        elif course_choice == "4":
            self.course = "Back to menu"
            # print("4. Back to menu")

    def student_portal(self):
        portalDict = {
            "Student Name": {self.name},
            "enroll id": 12345,
            "Previous Education": {self.prev_institute},
            "Enrolled Course": {self.course},
            "Fees Paid": {self.fees},
        }
        print(portalDict)
        self.user_portal = input(f"{portalDict}")
    

    def show_fee_details(self, course, fees):
        print(f"\nCourse: {course}")
        print(f"Fees: {fees}")
        print("Thank you for the course!")

choi = Choice()
choi.menu()
choi.student_portal()