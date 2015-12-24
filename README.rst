=========================
Django Resource Scheduler
=========================

The Django Resource Scheduler (DRS) is a Django app for scheduling the
use of shared physical resources.

Quick Start
-----------
1. Add "resource_scheduler" to your INSTALLED_APPS, like this::
	
	INSTALLED_APPS = [
		...
		'resource_scheduler',
	]

2. Include the DRS URLConf in your project urls.py, like this::

	url(r'^drs/', include('resource_scheduler.urls')),

3. Run `python manage.py migrate` to create the DRS models.
