from odoo import fields, models, api

class ProjectProject(models.Model):
    _inherit = 'project.project'
    
    short_code = fields.Char(string='Short Code')
    task_sequence = fields.Integer(string='Task Sequence', default=1)
    sequence_padding = fields.Integer(string='Sequence Padding', default=4)
    sample_task_num = fields.Char(string='Sample Task Number',readonly=True, compute='_compute_sample_task_num')

    @api.onchange('short_code', 'task_sequence', 'sequence_padding')
    def _compute_sample_task_num(self):
        for project in self:
            if project.task_sequence and project.short_code:
                padding = '0' * project.sequence_padding
                project.sample_task_num = f"{project.short_code}-{padding}{project.task_sequence}"
            else:
                project.sample_task_num = 'Sample Task Number'