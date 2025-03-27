-- Start a transaction
START TRANSACTION;

-- Try to update employee salaries
BEGIN TRY

    UPDATE Employees
    SET Salary = Salary * 1.10
    WHERE Department = 'Sales'; 
    -- Commit the transaction if the update is successful
    COMMIT;
    PRINT 'Salary update successful.';
END TRY
BEGIN CATCH
    -- If an error occurs, rollback the transaction
    ROLLBACK;
    PRINT 'Error occurred. Transaction rolled back.';
    -- You can capture the error details here if needed
    -- SELECT ERROR_MESSAGE() AS ErrorMessage;
END CATCH;
