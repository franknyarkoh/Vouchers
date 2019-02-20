# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frank Nyarkoh and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RequestLine(Document):
	quantity = int(input("Quantity: "))
	price = int(input"Price: "))
	amount = quantity * price
	total = sum(amount)
