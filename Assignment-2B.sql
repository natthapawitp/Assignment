--Write an SQL query to fetch employee names having a salary greater than or equal to 5000 and less than or equal to 10000.

SELECT 
	EmployeeDerails.FullName,
	EmployeeSalary.Salary
FROM 
	EmployeeDerails, EmployeeSalary
WHERE 
	EmployeeDerails.EmpId = EmployeeSalary.EmpId
AND
	EmployeeSalary.Salary BETWEEN 5000 AND 10000