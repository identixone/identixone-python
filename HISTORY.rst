History
=================

0.1.3 (2019-04-05)
------------------

* Fixed several API calls where default values should not be provided.
* Fixed places where default values were different than default API values.

0.1.2 (2019-04-01)
------------------

* API Changelog is now constantly updated here: https://kb.identix.one/#/apichangelog
* Updated documentation to show how to configure client with env variables
* Records endpoints are now deprecated
* Added new Entries and Entries Stats endpoints for RESTful manipulation with data (meant to replace and enhance records functionality)
* Added new Person Entries endpoint: create new person by providing id of NM entry
* Added examples of newly added endpoints

0.1.1 (2019-03-16)
------------------

* Updated docstrings for main functions
* New type of exception ImproperlyConfigured that replaces more general error in several places
* Added conf choices where applicable
* Added missing methods to bulk delete tokens with filtration (permanent/temporary/both)
* Added new source option `store_images_for_confs`, introduced in 1.9.0 API
* Added choices `NotificationHTTPMethod` of notifications http_method parameter for convenience
* Utility compare function now has default conf which equals HA. It reflects now default API behaviour
* Removed CHANGES.md because it is redundant. All changes are going to be reflected here, there's no need to duplicate info.
* Fixed a bug with env variables (fixed one typo & inability to override vars by setting env variables instead of providing them as parameters to init of Client)
* Fixed: previously you could provide your own http_client to the Client instance, but it required instance with already supplied token (so you basically needed to provide token in two places). Now you provide only class in http_client and initialization in Client will create instance with provided token for you.

0.1.0 (2019-02-18)
------------------

* First release on PyPI.
