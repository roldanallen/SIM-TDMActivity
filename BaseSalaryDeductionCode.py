def get_valid_salary():
    while True:
        try:
            salary = float(input("Enter your monthly salary: "))
            if salary <= 0:
                raise ValueError("Salary must be greater than zero.")
            return salary
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid numeric salary.")

def compute_philhealth_deduction(salary):
    return (salary * 0.05) / 2

def compute_deductions(salary):
    SSS_CONTRIBUTION = salary * 0.15 # assume the range of % cut is at maximum
    
    if salary <= 1500:
        PAGIBIG_CONTRIBUTION = salary * 0.01
    else:
        PAGIBIG_CONTRIBUTION = salary * 0.02

    FIXED_TAX = 1875
    philhealth = compute_philhealth_deduction(salary)

    total_deductions = SSS_CONTRIBUTION + philhealth + PAGIBIG_CONTRIBUTION + FIXED_TAX
    net_salary = salary - total_deductions

    return {
        "gross_salary": salary,
        "sss": SSS_CONTRIBUTION,
        "philhealth": philhealth,
        "pagibig": PAGIBIG_CONTRIBUTION,
        "tax": FIXED_TAX,
        "total_deductions": total_deductions,
        "net_salary": net_salary
    }

def display_salary_details(details):
    print("\nSalary Breakdown:")
    print(f"Gross Salary: {details['gross_salary']:.2f}")
    print(f"SSS Deduction: {details['sss']:.2f}")
    print(f"PhilHealth Deduction: {details['philhealth']:.2f}")
    print(f"Pag-IBIG Deduction: {details['pagibig']:.2f}")
    print(f"Tax Deduction: {details['tax']:.2f}")
    print(f"Total Deductions: {details['total_deductions']:.2f}")
    print(f"Net Salary: {details['net_salary']:.2f}")

def main():
    salary = get_valid_salary()
    salary_details = compute_deductions(salary)
    display_salary_details(salary_details)

if __name__ == "__main__":
    main()
