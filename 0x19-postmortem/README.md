# Postmortem

Postmortem Report: Tiketi Tamasha Outage on August 14, 2024
Issue Summary:
Duration:

Start: August 14, 2024, 02:00 AM EAT
End: August 14, 2024, 05:15 AM EAT
Total Duration: 3 hours 15 minutes
Impact:

The Tiketi Tamasha platform was completely inaccessible during the outage. Users experienced HTTP 500 Internal Server Errors when attempting to access any page on the platform, including the event search, ticket purchasing, and user login. Approximately 95% of users were affected, leading to a significant disruption in service.
Root Cause:

The root cause of the outage was a corrupted .htaccess file in the Apache web server configuration, caused by a misconfigured Puppet script that inadvertently introduced syntax errors during a routine configuration update.
Timeline:
02:00 AM: Issue detected by automated monitoring system which flagged a significant drop in web traffic and an increase in HTTP 500 errors.
02:05 AM: On-call engineer received an alert from the monitoring system and began investigating the issue.
02:15 AM: Initial assumption was that there was a database connection issue, as the error logs showed repeated failures in database connections.
02:30 AM: Engineer restarted the PostgreSQL database, but the issue persisted. The database logs were clean, indicating the problem was not with the database itself.
02:45 AM: Further investigation revealed that the Apache server was failing to serve any requests. Attention shifted to the Apache configuration.
03:00 AM: Puppet configuration was reviewed, and it was discovered that a recent deployment had updated the .htaccess file.
03:15 AM: The team attempted to roll back the recent configuration changes, but the issue remained unresolved.
03:30 AM: The incident was escalated to the web infrastructure team.
04:00 AM: Web infrastructure team identified syntax errors in the .htaccess file, caused by an incorrect Puppet script.
04:30 AM: The corrupted .htaccess file was manually corrected, and Apache was restarted.
04:45 AM: Service was restored, and traffic began returning to normal levels.
05:15 AM: Final checks confirmed the system was fully operational.
Root Cause and Resolution:
Root Cause:

The Puppet script responsible for deploying configuration updates to the Apache web server contained a syntax error in the .htaccess file. This error was introduced during a routine update intended to optimize caching rules for the platform. The misconfiguration caused Apache to fail when attempting to parse the .htaccess file, resulting in a complete service outage.
Resolution:

The web infrastructure team manually corrected the syntax errors in the .htaccess file and restarted the Apache server. This immediately restored service to the platform. The faulty Puppet script was also rolled back to a previous version to prevent recurrence.
Corrective and Preventative Measures:
Improvements/Fixes:

Review and improve the Puppet configuration testing process to catch syntax errors before deployment.
Implement additional monitoring to detect Apache configuration issues before they cause outages.
Enhance the logging mechanism to provide clearer insights into server-side issues, particularly related to configuration files.
Tasks:

 Patch the Puppet script to fix the syntax error and re-test in a staging environment.
 Add a pre-deployment syntax check for Apache configuration files in the CI/CD pipeline.
 Set up monitoring alerts for failed Apache server restarts.
 Conduct training for engineers on best practices for managing configuration files and automated deployments.
This postmortem highlights the importance of thorough testing and monitoring in automated configuration management. By implementing the corrective measures outlined above, we aim to prevent similar incidents from occurring in the future.
