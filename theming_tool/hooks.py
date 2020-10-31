# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
import os
from theming_tool.theming_tool.doctype.theme_settings.theme_settings import get_site_name

app_name = "theming_tool"
app_title = "Theming Tool"
app_publisher = "Ahmed Al-Farran"
app_description = "Theming tool for frappe"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "afarran1992@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

app_include_css = "/assets/" + get_site_name() + "/theme/css/custom_theme.css"
# include js, css files in header of desk.html
# app_include_css = "/assets/theming_tool/css/theming_tool.css"
# app_include_js = "/assets/theming_tool/js/theming_tool.js"
web_include_css = "/assets/" + get_site_name() + "/theme/css/custom_theme.css"
# include js, css files in header of web template
# web_include_css = "/assets/theming_tool/css/theming_tool.css"
# web_include_js = "/assets/theming_tool/js/theming_tool.js"

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
# get_website_user_home_page = "theming_tool.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "theming_tool.install.before_install"
# after_install = "theming_tool.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "theming_tool.notifications.get_notification_config"

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
# 		"theming_tool.tasks.all"
# 	],
# 	"daily": [
# 		"theming_tool.tasks.daily"
# 	],
# 	"hourly": [
# 		"theming_tool.tasks.hourly"
# 	],
# 	"weekly": [
# 		"theming_tool.tasks.weekly"
# 	]
# 	"monthly": [
# 		"theming_tool.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "theming_tool.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "theming_tool.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "theming_tool.task.get_dashboard_data"
# }
