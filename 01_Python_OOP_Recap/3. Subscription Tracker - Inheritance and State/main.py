from subscription import *

# Runtime-only storage: holds all Subscription objects (both DigitalSub
# and PhysicalSub instances) for as long as the program is running.
my_subs = []

# Interactive CLI loop: keeps the menu running until the user picks
# the "Exit" option, which triggers the `break` at the bottom.
while True:
    print_separator()
    print("Make a Choice :")
    print_separator()
    print("1. Add a Subscription \n2. View all Subscription \n3. Cancel a subscription \n4. Exit")
    print_separator()
    try:
        choice = int(input("Enter your Choice (1 , 2 , 3 , 4) : "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if choice == 1:
        print_separator()
        print("Adding a new subscription.")
        print_separator()
        name = input("Name of Subscription: ")
        
        try:
            monthly_cost = float(input("Monthly Cost : "))
        except ValueError:
            print("Enter valid numbers")
            continue
        
        billing_date = input("Billing Date : ")
        print_separator()
        print("What Kind of subscription is it? :")
        print_separator()
        print("1. Digital Subscription \n2. Physical Subscription\n")

        try:
            sub_class = int(input("Enter your choice (1 / 2) : "))
            print_separator()
        except ValueError:
            print("Please enter a valid number")
            continue
        
        # Instantiating the DigitalSub subclass - this runs DigitalSub's
        # __init__, which internally calls super().__init__() to set up
        # the inherited name/monthly_cost/billing_date/__is_active fields.
        if sub_class == 1:
            device_limit = input("What is the 'devices connected' limit : ")
            new_sub = DigitalSub(name, monthly_cost ,billing_date, device_limit)
            my_subs.append(new_sub)

        # Instantiating the PhysicalSub subclass - same inheritance flow
        # as above, but adds the location attribute instead of device_limit.
        elif sub_class == 2:
            location = input("Location : ")
            new_sub = PhysicalSub(name, monthly_cost ,billing_date, location)
            my_subs.append(new_sub)

        else:
            print("Enter a valid option")

        print_separator()
        print("New Subscription was Successfully Added!")

    elif choice == 2:
        print_separator()
        print("Displaying all your subscriptions:")
        if len(my_subs) > 0:
            total_cost = 0
            for sub in my_subs:
                # Getter method call: check_status() reads the private
                # __is_active flag through the class's public interface
                # instead of accessing sub.__is_active directly.
                if sub.check_status():
                    print_separator()
                    # This calls __str__ on the object - Python automatically
                    # dispatches to DigitalSub's or PhysicalSub's overridden
                    # version depending on the object's actual type.
                    print(sub)
                    total_cost += sub.monthly_cost
            print_separator()
            print(f"Your Annual Cost for Subscriptions is : {total_cost * 12}")
        else:
            print("NO SUBSCRIPTION FOUND")    

    elif choice == 3:
        print_separator()
        print("Cancelling your subscription...")
        print_separator()
        remove_sub = input("Enter the name of the subscription : ")
        flag = 0

        for sub in my_subs:
            if remove_sub == sub.name:
                # State mutation via method call: cancel() is the only
                # sanctioned way to flip __is_active to False, keeping the
                # encapsulation boundary intact instead of setting it directly.
                sub.cancel()
                flag = 1
        
        if flag == 1:
            print_separator()
            print("The Subscription was Cancelled")
        else:
            print("No such subscription found.")
            

    # Exit option: any choice other than 1, 2, or 3 ends the while loop.
    else:
        break
