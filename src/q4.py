"""
This question has no starter code.

Create a class called BankAccount which stores a bank account balance.

The class should:

- Store balance internally, but provide read-only access via a balance property
- Allows the client to add money to the account through a method called deposit
- Allows the client to withdraw money from the account through a method called withdraw
- Maintain a private transaction log and provide read-only access via a transactions property that returns a copy (not the original list)
- Have an is_frozen property that can be set, and when frozen, prevents all transactions
"""