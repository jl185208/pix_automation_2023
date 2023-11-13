Feature: Dashboard page
	Scenario: Validate dashboard page
		Given dashboard page is accessed
		Then welcome back is displayed in dashboard
		#When recent order is clicked
		#And marked as notification is solved
		#Then should be listed in archived
		And updates test results for OCS-T1290 