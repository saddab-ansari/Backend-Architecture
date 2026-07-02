# Problem Statement: Subscription Graveyard CLI
 
## Objective
 
The developer is required to build a command-line system that tracks different types of subscriptions, calculates their combined annual cost, and allows the user to cancel them safely. This project serves as a practical exercise in inheritance, encapsulation, abstraction, and multi-file architecture in Python.
 
## Requirements
 
### 1. The Base Class: `Subscription`
 
The foundational blueprint for all subscription types.
 
**Constructor (`__init__`):** Must accept `name`, `monthly_cost`, and `billing_date` as arguments.
 
**Encapsulation:** A private variable `__is_active` must be set to `True` by default, preventing accidental external mutation of a subscription's active state.
 
**Abstraction:** Two clean methods must be implemented:
- `get_annual_cost()` — multiplies the monthly cost by 12 and returns the result.
- `cancel()` — safely sets the private `__is_active` variable to `False`.
---
 
### 2. Child Classes via Inheritance
 
Two subclasses must inherit from `Subscription`, each extending the base with type-specific attributes.
 
**`DigitalSub(Subscription)`**
- Adds a `device_limit` attribute to the constructor.
- Overrides `__str__` to include the device limit in its output.
**`PhysicalSub(Subscription)`**
- Adds a `location` attribute to the constructor.
- Overrides `__str__` to include the location in its output.
---
 
### 3. The Main CLI Loop
 
An interactive loop must be implemented in `main.py`.
 
- An empty list `my_subs` is initialised to store subscription objects at runtime.
- A `while True` loop keeps the terminal active until the user chooses to exit.
- The user is prompted with four options: Add, View All, Cancel, and Exit.
- On selecting **View All**, the program iterates through `my_subs`, prints the stats of every active subscription, and displays the combined annual cost of all active subscriptions.
## Scope
 
Persistent data storage is out of scope. All subscription data exists only for the duration of the program's runtime.
