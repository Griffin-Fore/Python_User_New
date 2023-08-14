class User:
    # attributes
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # methods
    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards member status: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    def enroll(self):
        if(self.is_rewards_member == True):
            print("User already a member")
        else:
            print(f"Signing you up, {self.first_name}!")
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"Member status: {self.is_rewards_member}")
            print(f"Gold Card Points: {self.gold_card_points}")

    def spend_points(self, amount):
        if(amount < self.gold_card_points):
            print(f"Hello {self.first_name}, Withdrawing points. Current Points: {self.gold_card_points}")
            self.gold_card_points -= amount
            print(f"New point balance: {self.gold_card_points}")
        else:
            print(f"Insufficient points. Points: {self.gold_card_points}.")
            print(f"Amount to withdraw: {amount}")
    pass

user_Griffin = User("Griffin", "Fore", "griffinfore@gmail.com", 27)
user_Griffin.display_info()
user_Griffin.enroll()
user_Griffin.spend_points(50)

user_Ada = User("Ada", "Lovelace", "alove@gmail.com", 35)
user_Ada.display_info()
user_Ada.enroll()
user_Ada.spend_points(80)

user_Michael = User("Michael", "Scott", "mscott@dmifflin.net", 40)
user_Michael.display_info()

user_Griffin.enroll()

user_Michael.enroll()
user_Michael.spend_points(160)
user_Michael.spend_points(160)