Feature: Settings page
	Scenario: Validate settings page
		Given settings page is accessed
		Then welcome message is displayed
		And user can fire notification
		When fire notification button is clicked
		Then You have new notifications! is displayed
		And creates a "Pixel Functional Test" testcycle in zephyr
		And updates test results for OCS-T1288 