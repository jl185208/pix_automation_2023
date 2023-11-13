Feature: Notifications page
	Scenario: Validate fired notifications and mark as solved
		Given that notifications page is accessed
		When notification is open and less than 1 minute
		And the notification is clicked
		And marked as notification is solved
		Then should be listed in archived
		And updates test results for OCS-T1289 