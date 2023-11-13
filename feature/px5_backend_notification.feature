Feature: Backend notification
	Scenario: Validate new notification fired from backend
		Given pwa is accessed
		When notification is fired in dynamodb
		And notification is open and less than 1 minute
		And the notification is clicked
		And marked as notification is solved
		Then should be listed in archived
		#And updates test results for OCS-T1325 
		And should execute OCS-T1325