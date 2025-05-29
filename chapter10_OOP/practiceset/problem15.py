class Instructor:
    def __init__(self):
        self.__instructor_name = None
        self.__experience = None
        self.__avg_feedback = None
        self.__technology_skill = None

    def check_eligibility(self):
        if self.__experience > 3:
            return self.__avg_feedback >= 4.5
        else:
            return self.__avg_feedback >= 4

    def allocate_course(self, technology):
        return technology in self.__technology_skill
    

    # Getters and Setters
    # Getters
    def get_instructor_name(self):
        return self.__instructor_name
    def get_experience(self):
        return self.__experience
    def get_avg_feedback(self):
        return self.__avg_feedback
    def get_technology_skill(self):
        return self.__technology_skill
    # Setters
    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name
    def set_experience(self, experience):
        self.__experience = experience
    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback
    def set_technology_skill(self, technology_skill):
        self.__technology_skill = technology_skill


    # String representation
    # __str__ and __repr__ methods
    def __repr__(self):
        return f"Instructor({self.__instructor_name}, {self.__experience}, {self.__avg_feedback}, {self.__technology_skill})"
    def __str__(self):
        return f"Instructor Name: {self.__instructor_name}, Experience: {self.__experience}, Average Feedback: {self.__avg_feedback}, Technology Skills: {', '.join(self.__technology_skill)}"
    


# Example usage
instructor1 = Instructor()
instructor1.set_instructor_name("John Doe")
instructor1.set_experience(5)
instructor1.set_avg_feedback(4.8)
instructor1.set_technology_skill(["Python", "Java", "C++"])
instructor2 = Instructor()
instructor2.set_instructor_name("Jane Smith")
instructor2.set_experience(2)
instructor2.set_avg_feedback(4.2)
instructor2.set_technology_skill(["JavaScript", "HTML", "CSS"])


print(instructor1)
print(instructor2)
print(f"Is {instructor1.get_instructor_name()} eligible? {instructor1.check_eligibility()}")
print(f"Is {instructor2.get_instructor_name()} eligible? {instructor2.check_eligibility()}")
print(f"Can {instructor1.get_instructor_name()} teach Python? {instructor1.allocate_course('Python')}")
print(f"Can {instructor2.get_instructor_name()} teach Python? {instructor2.allocate_course('Python')}")

