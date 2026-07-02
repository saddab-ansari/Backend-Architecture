class Subscription:
    def __init__(self, name : str, monthly_cost : float, billing_date : str) -> None:
        self.name = name
        self.monthly_cost = monthly_cost
        self.billing_date = billing_date

        self.__is_active = True

    def __str__(self) -> str:
        return(f"Name : {self.name} \nMonthly cost : {self.monthly_cost} \nBilling date : {self.billing_date}")

    def get_annual_cost(self) -> float:
        return(self.monthly_cost * 12)

    def cancel(self) -> None:
        self.__is_active = False

    def check_status(self) -> bool:
        return self.__is_active

class DigitalSub(Subscription):
    def __init__(self, name : str, monthly_cost : float, billing_date : str, device_limit : int) -> None:
        super().__init__(name, monthly_cost, billing_date)
        self.device_limit = device_limit

    def __str__(self) -> str:
        return(f"Name : {self.name} \nMonthly cost : {self.monthly_cost} \nBilling date : {self.billing_date} \nDevice limit : {self.device_limit}")

class PhysicalSub(Subscription):
    def __init__(self, name : str, monthly_cost : float, billing_date : str, location : str) -> None:
        super().__init__(name, monthly_cost, billing_date)
        self.location = location

    def __str__(self) -> str:
        return(f"Name : {self.name} \nMonthly cost : {self.monthly_cost} \nBilling date : {self.billing_date} \nlocation : {self.location}")



def print_separator() -> None:
    print("\n" + "-" * 40 + "\n")

