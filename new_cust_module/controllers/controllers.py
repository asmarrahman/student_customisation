from odoo import http
from odoo.http import request
import base64

class Student(http.Controller):
    @http.route('/school/student_registration', type='http', auth='public', website=True)
    def student_reg(self):
        return request.render('new_cust_module.student_reg_page_template', {})
    
    @http.route('/school/student_registration/success', type='http', auth='public', website=True)
    def student_submit(self, **kw):
        request.env['new_cust_module.student'].create(kw)
        return request.render('new_cust_module.student_reg_page_template', {})






class StudentNew(http.Controller):
    @http.route('/school/student_registration_new', type='http', auth='public', website=True)
    def student_reg(self):
        return request.render('new_cust_module.student_new_reg_page_template', {})

    @http.route('/school/student_registration/submitted', type='http', auth='public', website=True)
    def student_submit(self, **kw):
        image_data = kw.get('image')
        image = base64.b64encode(image_data.read())
        kw.update({'image': image})
        request.env['new_cust_module.student'].create(kw)
        return http.request.render('new_cust_module.student_new_reg_page_template', {})