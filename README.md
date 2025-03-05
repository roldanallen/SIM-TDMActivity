Role:
1. Refactoring Specialist - Assigned to "Allen S Roldan"
2. Lead Developer - Assigned to "Allen S Roldan"
3. Lead Developer - Assigned to "Allen S Roldan"
4. Tester & Documenter - Assigned to "Allen S Roldan"

TASK:
1. Improve code readability 
2. Convert to modular functions
3. Implement OOP (if applicable)
4. Add input validation & error handling

Refactored Changes:
------Improve Code readability (Refactoring Specialist)------
1. Improved Naming Conventions
Functions now clearly describe their purpose:
    get_valid_salary(), compute_philhealth_deduction(), compute_deductions(), display_salary_details(), main()

------Convert to Modular Functions and OOP (Lead Developer)------
2. Modular Functions for Maintainability:
Split logic into separate functions:
    a. compute_philhealth_deduction(salary) to calculate PhilHealth contribution.
    b. compute_deductions(salary) to handle all deduction calculations.
    c. display_salary_details(details) for formatted output.

3. Replaced Hardcoded Values with Constants:
    Defined SSS, Pag-IBIG, and Tax as constants inside compute_deductions() for easier updates.

4.  Encapsulated Execution Logic in main():
    Organized program flow using a main() function, improving readability and usability.

------Add Input Validation & Error Handling  (Tester and Documenter)------
5. Implemented Input Validation & Error Handling:
    get_valid_salary() ensures only positive numeric values are accepted, preventing crashes due to invalid input.


-----Identified Technical Debt-------
1. Poor Naming Conventions - Function and variable names were unclear.
2. Lack of Modular Functions - Single function handling all logic made it hard to maintain.
3. Hardcoded Values - Fixed values (SSS, Tax, etc.) were directly embedded.
4. No Error Handling - No validation for user input, leading to potential crashes.
5. Code Duplication - PhilHealth computation was inline without reuse.

-----CHALLENGES FACED & SOLUTIONS------
1. The original code had a few issues. Everything was inside one function making it hard to reuse. 
2. Some values like SSS and tax were fixed and I need to do some research and changing them required editing the code. 
3. There was no check for wrong inputs which could cause issues in the program. 
4. Function and variable names weren't clear such as SSS but it was used for SSS deduction. 
5. These were fixed by using separate functions, adding input validation, and making names easier to understand.