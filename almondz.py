def get_person_details():
    name = input("Enter person's name: ")
    user_id = input("Enter user ID: ")
    email = input("Enter email ID: ")
    phone_number = input("Enter phone number: ")
    return name, user_id, email, phone_number

def main():
    # Initialize an empty list to store details of 4 people
    people_details = []

    # Loop to get details for 4 people
    for i in range(4):
        print(f"\nEnter details for person {i+1}:")
        details = get_person_details()
        people_details.append(details)

    # Display the details of all 4 people
    print("\nDetails of all people:")
    for i, details in enumerate(people_details):
        print(f"\nPerson {i+1}:")
        print("Name:", details[0])
        print("User ID:", details[1])
        print("Email ID:", details[2])
        print("Phone Number:", details[3])
if __name__ == "__main__":
    main()
    
    
def distribute_amount(people_details):
    # Find the index of the person who got 1000
    index_with_1000 = -1
    for i, details in enumerate(people_details):
        if details[1] == "1000":
            index_with_1000 = i
            break

    if index_with_1000 == -1:
        print("No user with ID 1000 found.")
        return

    # Remove the person who got 1000 from the list
    person_with_1000 = people_details.pop(index_with_1000)

    # Calculate the amount to be distributed equally among the remaining three people
    amount_to_distribute = 1000 / 3

    # Add the amount to each person's details
    for i, details in enumerate(people_details):
        people_details[i] = (details[0], details[1], details[2], details[3], amount_to_distribute)

    # Display the details of all 4 people after distribution
    print("\nDetails of all people after amount distribution:")
    for i, details in enumerate(people_details):
        print(f"\nPerson {i+1}:")
        print("Name:", details[0])
        print("User ID:", details[1])
        print("Email ID:", details[2])
        print("Phone Number:", details[3])
        print("Amount Received:", details[4])

@csrf_exempt
def add_expense(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        description = data.get('description')
        amount = data.get('amount')
        date = data.get('date')
        user_id = data.get('payer')
        participants_ids = data.get('participants')
        
        user = User.objects.get(id=payer_id)
        participants = User.objects.filter(id__in=participants_ids)
        
        expense = Expense.objects.create(description=description, amount=amount, date=date, payer=payer)
        expense.participants.add(*participants)
        
        # Update balances
        update_balances(payer, participants, amount)
        
        return JsonResponse({'message': 'Expense added successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def update_balances(payer, participants, amount):
    for participant in participants:
        balance, created = Balance.objects.get_or_create(user1=payer, user2=participant)
        balance.balance += amount / len(participants)
        balance.save()

 # Update balances
        update_balances(payer, participants, amount)
        
        return JsonResponse({'message': 'Expense added successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def update_balances(payer, participants, amount):
    total_participants = len(participants)
    # Calculate amount each participant owes
    share_amount = amount / total_participants
    
    # Update balances for payer and participants
    for participant in participants:
        balance, created = Balance.objects.get_or_create(user1=payer, user2=participant)
        balance.balance += share_amount
        balance.save()
        
        # Update balances for participants to payer
        reverse_balance, created = Balance.objects.get_or_create(user1=participant, user2=payer)
        reverse_balance.balance -= share_amount
        reverse_balance.save()

    # Update balances for existing dues
    for participant in participants:
        existing_balance = Balance.objects.get(user1=participant, user2=payer)
        existing_balance.balance -= share_amount
        existing_balance.save()

        reverse_existing_balance = Balance.objects.get(user1=payer, user2=participant)
        reverse_existing_balance.balance += share_amount
        reverse_existing_balance.save()
        
        # Display the details of all 4 people after distribution
    print("\nDetails of all people after amount distribution:")
    for i, details in enumerate(people_details):
        print(f"\nPerson {i+1}:")
        print("Name:", details[0])
        print("User ID:", details[1])
        print("Email ID:", details[2])
        print("Phone Number:", details[3])
        print("Amount Received:", details[4])
 
