--Write a query to fetch employee names and salary records. Display the employee details even if the salary record is not present for the employee.

SELECT
    EmployeeDerails.FullName,
    EmployeeSalary.Salary
FROM
    EmployeeDerails
LEFT JOIN EmployeeSalary ON EmployeeDerails.EmpId = EmployeeSalary.EmpId