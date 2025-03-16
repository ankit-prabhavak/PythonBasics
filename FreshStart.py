class NewJourney:
    def __init__(self, name, goals, dreams, mindset="growth", focus="clarity"):
        self.name = name
        self.goals = goals
        self.dreams = dreams
        self.mindset = mindset
        self.focus = focus
        self.current_step = 1
        self.progress = 0

    def set_mindset(self, new_mindset):
        print(f"Shifting mindset from {self.mindset} to {new_mindset}.")
        self.mindset = new_mindset

    def define_goals(self):
        print(f"Setting clear goals: {', '.join(self.goals)}")
        self.progress += 10

    def define_dreams(self):
        print(f"Visualizing dreams: {', '.join(self.dreams)}")
        self.progress += 10

    def take_action(self):
        print(f"Taking action: Step {self.current_step} in pursuit of goals.")
        self.progress += 20
        self.current_step += 1

    def reflect_and_adjust(self):
        print(f"Reflecting on journey. Current progress: {self.progress}%")
        if self.progress < 100:
            print("Adjusting course for better alignment.")
            self.progress += 15
        else:
            print("You're on track! Keep going.")

    def celebrate_success(self):
        print("Celebrating milestones! You've made incredible progress.")
        self.progress = 100

    def start_journey(self):
        print(f"Starting your journey, {self.name}!")
        self.define_goals()
        self.define_dreams()
        self.take_action()

        while self.progress < 100:
            self.take_action()
            self.reflect_and_adjust()
        
        self.celebrate_success()

# Create your personal journey
my_journey = NewJourney(
    name="Your Name",
    goals=["Learn new skills", "Build a better future", "Stay healthy", "Embrace change"],
    dreams=["Be financially free", "Travel the world", "Build meaningful relationships", "Create impact"]
)

# Start your journey
my_journey.start_journey()
