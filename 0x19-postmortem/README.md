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





You said:
We are constantly stormed by a quantity of information, it’s tough to get people to read you.

Make your post-mortem attractive by adding humour, a pretty diagram or anything that would catch your audience attention.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.
ChatGPT said:
ChatGPT
Postmortem Report: The Great Tiketi Tamasha "Where Did Everyone Go?" Outage of August 14, 2024
Issue Summary:
Duration:

Start: August 14, 2024, 02:00 AM EAT
End: August 14, 2024, 05:15 AM EAT
Total Duration: 3 hours and 15 minutes, but it felt like 3 weeks for the team on call.
Impact:

What Happened: Tiketi Tamasha’s grand digital doors slammed shut, and instead of tickets, users were handed shiny new HTTP 500 errors. The result? 95% of our users were left out in the cold, wondering why they couldn’t book their tickets to the hottest events.
User Experience: A whole lot of "Huh?" and frantic refreshing. There were reports of desperate users refreshing their browsers more times than they did during last year’s New Year’s Eve sale.
Root Cause:

The culprit? A rogue .htaccess file corrupted by a misbehaving Puppet script. In layman's terms, we essentially tripped over our own shoelaces while trying to update our Apache server, sending our site face-first into a 500-error abyss.
Timeline:
02:00 AM: The first alarm bells rang in the data center: web traffic nosedived while HTTP 500 errors skyrocketed. The bots were panicking.

Imagine this but with a "Houston, we have a problem" meme.

02:05 AM: Our on-call engineer was rudely awoken by their pager. Coffee intake increased by 200%.

02:15 AM: Initial diagnosis pointed to the database, but it was a false alarm—PostgreSQL was as innocent as a kitten.

02:30 AM: PostgreSQL restarted. No change. The mystery deepened.

02:45 AM: The investigation pivoted to Apache, and the .htaccess file came under suspicion.
Picture Sherlock Holmes with a magnifying glass, staring intently at a server rack.

03:00 AM: Recent Puppet script changes were scrutinized—something smelled fishy (spoiler: it was the .htaccess file).

03:15 AM: Rolling back the changes didn’t fix the issue, adding to the confusion.

03:30 AM: The cavalry arrived! The web infrastructure team was called in.

04:00 AM: The root cause was finally identified: a small typo in the .htaccess file was causing all the chaos. (Yes, one tiny typo!)

04:30 AM: The syntax error was corrected manually, and Apache was revived.
Cue dramatic defibrillator scene.

04:45 AM: Service was restored, and users began to trickle back in. Phew!

05:15 AM: Final checks confirmed the system was back on its feet, and the team sighed in relief (and exhaustion).

Root Cause and Resolution:
Root Cause:

The outage was caused by a syntax error in the .htaccess file, introduced by a Puppet script during a routine update. This mistake was like putting a square peg in a round hole—it just didn’t work, and Apache wasn’t happy about it.
Resolution:

The error in the .htaccess file was manually corrected, and Apache was restarted, bringing the site back online. The Puppet script was also rolled back, and a fresh pot of coffee was brewed for the team.
Corrective and Preventative Measures:
Improvements/Fixes:

Test, Test, Test: Enhance our Puppet script testing process to catch errors before they go live. Because typos should be caught by computers, not humans at 3 AM.
Monitor Everything: Introduce more robust monitoring, particularly for Apache configurations, to detect issues before they become full-blown outages.
Log Like a Pro: Improve logging to provide clearer insights into configuration errors—so the next detective can solve the case faster.
TODO List:

 Patch the Puppet script and run it through rigorous testing.
 Add pre-deployment syntax checks for Apache configurations.
 Set up a new alert system for failed Apache restarts (complete with its own theme tune).
 Organize a training session on avoiding late-night configuration catastrophes.
And remember, folks, a single typo can cause hours of headaches. But hey, at least we’ve got a good story for the next company all-hands!
