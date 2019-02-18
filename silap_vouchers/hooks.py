# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "silap_vouchers"
app_title = "Silap Vouchers"
app_publisher = "Frank Nyarkoh"
app_description = "Payment and Request Voucher"
app_icon = "fa fa-user"
app_color = "grey"
app_email = "frank.nyarkoh@hotmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/silap_vouchers/css/silap_vouchers.css"
# app_include_js = "/assets/silap_vouchers/js/silap_vouchers.js"

# include js, css files in header of web template
# web_include_css = "/assets/silap_vouchers/css/silap_vouchers.css"
# web_include_js = "/assets/silap_vouchers/js/silap_vouchers.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "silap_vouchers.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "silap_vouchers.install.before_install"
# after_install = "silap_vouchers.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "silap_vouchers.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"silap_vouchers.tasks.all"
# 	],
# 	"daily": [
# 		"silap_vouchers.tasks.daily"
# 	],
# 	"hourly": [
# 		"silap_vouchers.tasks.hourly"
# 	],
# 	"weekly": [
# 		"silap_vouchers.tasks.weekly"
# 	]
# 	"monthly": [
# 		"silap_vouchers.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "silap_vouchers.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "silap_vouchers.event.get_events"
# }

