--Write an SQL query to display the total salary of each employee adding the Salary with Variable value

SELECT 
	EmployeeDerails.FullName,
	EmployeeSalary.Salary,
    EmployeeSalary.Variable,
    EmployeeSalary.Salary + EmployeeSalary.Variable AS Total_Salary
FROM 
	EmployeeDerails, EmployeeSalary
WHERE 
	EmployeeDerails.EmpId = EmployeeSalary.EmpId