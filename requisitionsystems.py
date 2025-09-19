'''
This code was done using Object-oriented programming and all of the codes from previous task were combined with few changes to meet the requirements, in the output, statistics is given as output and manager can also decide wheter to Approve/Not Approve/Pending 
'''
class RequisitionSystem():
#this is a class and below are empty variables with no values, which later will help us complete the statistics
    counter = 0
    staffs = []
    total_requisitions = 0
    total_approved = 0 
    total_pending = 0
    total_notapproved = 0

    def __init__(self):
#this is a constructor which helps us in assigning values (Open/Closed is applied since we can make extension but no modification)
        self.date = None
        self.staff_id = None
        self.staff_name = None
        self.status = None
        self.unique_id = None
        self.cost = 0
        self.approval_num = "Not Assigned"
        RequisitionSystem.staffs.append(self)
    
    def staff_info(self):
#staff functions allows user to input basic staff information and assign a unique ID (YAGNI can be applied in line 40 and 45, since that line is only a cosmetic feature and its not important as of now)
        print("Printing Staff Information: ")
        RequisitionSystem.counter += 1
        self.date = input("Date: ")
        
        while True:
            self.staff_id = input("Staff ID: ")
            if self.staff_id:
                break
            else:
                print("Enter valid input")
        
        self.staff_name = input("Staff Name: ")
        self.unique_id = 10000 + RequisitionSystem.counter
        
        print("\n-------- Printing Staff Information: --------")
        print(f"Date: {self.date}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Requisition ID: {self.unique_id}")
        print("---------------------------------------------")

    def requisitions_details(self): 
#this function allows user to enter number of items and their price (clean code > clever code is used here because its easy to read and maintain)
        self.cost = 0
        num_items = int(input("How many items are you buying: "))
        for i in range(num_items):
            items = input("Enter your requisition items: ")
            price = float(input("Enter the price: $"))
            self.cost += price
            
        print(f"Total cost is ${self.cost}")

    def requisition_approval(self):
#this function checks if the total is greater than, equal or less than 500, and based on that approval is granted or denied (KISS is used here because verything is simple and straightforward)
        RequisitionSystem.total_requisitions += 1
        if self.cost >= 500:
            self.status = "Pending"
            self.approval_num = "Not Assigned"
            RequisitionSystem.total_pending += 1
        else:
            self.status = "Approved"
            first = self.staff_id
            last3 = str(self.unique_id)[-3:]
            self.approval_num = first + last3
            RequisitionSystem.total_approved += 1

    def respond_requisition(self):
#this function allows manager to respond to all the requistions and decide whether to approve/deny a requisiton (Refactor can be used in the future for this function to improve it)   
        for staff in RequisitionSystem.staffs:
            if staff.status == "Pending":
                decision = input("Enter decision-Approved/Not Approved/Pending: ").lower()
                if decision == "approved":
                    staff.status = "Approved"
                    staff.approval_num = staff.staff_id + str(staff.unique_id)[-3:]
                    RequisitionSystem.total_pending -= 1
                    RequisitionSystem.total_approved += 1
                elif decision == "not approved":
                    staff.status = "Not Approved"
                    staff.approval_num = "Not Assigned"
                    RequisitionSystem.total_pending -= 1
                    RequisitionSystem.total_notapproved += 1
                else:
                    staff.status = "Pending"
                    staff.approval_num = "Not Assigned"

    def display_requisitions(self):
#this function displays all the information of the staff (KISS is used here because verything is simple and straightforward)
        for staff in RequisitionSystem.staffs:
            print("\nPrinting Requisitions: ")
            print(f"Date: {staff.date}")
            print(f"Requisition ID: {staff.unique_id}")
            print(f"Staff ID: {staff.staff_id}")
            print(f"Staff Name: {staff.staff_name}")
            print(f"Total: ${staff.cost}")
            print(f"Status: {staff.status}")
            print(f"Approval Reference number: {staff.approval_num}")

    def requisition_statistic(self):
#this function displays all the statistics (KISS is used here because verything is simple and straightforward)
        print("\nStatistics:")
        print("Displaying the Requisition Statistics")
        print(f"The total number of requisitions submitted: {RequisitionSystem.total_requisitions}")
        print(f"The total number of approved requisitions: {RequisitionSystem.total_approved}")
        print(f"The total number of pending requisitions: {RequisitionSystem.total_pending}")
        print(f"The total number of not approved requisitions: {RequisitionSystem.total_notapproved}")

#these are objects with instaces 
r1 = RequisitionSystem()
r1.staff_info()
r1.requisitions_details()
r1.requisition_approval()

r2 = RequisitionSystem()
r2.staff_info()
r2.requisitions_details()
r2.requisition_approval()

r3 = RequisitionSystem()
r3.staff_info()
r3.requisition_approval()
r3.requisitions_details()

r4 = RequisitionSystem()
r4.staff_info()
r4.requisitions_details()
r4.requisition_approval()

r5 = RequisitionSystem()
r5.staff_info()
r5.requisitions_details()
r5.requisition_approval()

r5.respond_requisition()
r5.display_requisitions()

r5.requisition_statistic()
