class Company():
    """
    Docstirng >> This is a class that defines a general type of company.

    Args:
    name: string
    industry_type: string
    num_employees: integer
    total_revenue: float
    """
    def __init__(self, name, industry_type, num_employees, total_revenue):
        self.name = name
        self.industry_type = industry_type
        self.num_employees = num_employees
        self.total_revenue = total_revenue

    def serve_customer(self):
        """
        Docstring >> this method will take in a float that is equal to
        the cost of serving some customer, and then adjust the total_revenue
        by that cost.

        Args:

        """
        pass

    def gain_employees(self):
        """
        Docstring >> this method will take in a list that contains new employees
        that the company has just brought on, and will update the num_employees
        attribute to take account of that.

        Args:

        """
        pass

"""
################
Test Code
################
Denver Beer Co.
Qdoba
Chipotle
"""
