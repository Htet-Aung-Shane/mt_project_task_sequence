from odoo import fields, models, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    task_num = fields.Char(string='Task Number', readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'task_num' not in vals or not vals['task_num']:
                vals['task_num'] = self.compute_task_num(vals['project_id'])
        return super(ProjectTask, self).create(vals_list)



    def compute_task_num(self,project_id):
        project = self.env['project.project'].browse(project_id)
        padding = '0' * project.sequence_padding
        task_num = f"{project.short_code}-{padding}{project.task_sequence}"
        project.task_sequence += 1
        return task_num


    @api.onchange('name', 'task_num')
    def _compute_display_name(self):
        for task in self:
            task.display_name = f"[{task.task_num}] - {task.name}"