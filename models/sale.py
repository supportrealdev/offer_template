# -*- coding: utf-8 -*-


from odoo import api, fields, models,  _
class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    offer_page2 = fields.Html('Offer Page2')
    offer_title2 = fields.Html('Objet de l’offre')
    offer_title21 = fields.Html('Historique des Versions')
    offer_title22 = fields.Html('Documents de Référence')
    offer_title31 = fields.Html('Data Integrity')
    offer_title32 = fields.Html('Cybersecruity ')
    offer_title33 = fields.Html('3.3Stratégie de Validation')
    offer_title34 = fields.Html('Scope du projet')
    offer_title35 = fields.Html('Liste des délivrables')
    offer_title41 = fields.Html('Planning')
    offer_title42 = fields.Html('Pilote de projet')
    offer_title43 = fields.Html('Acteurs du projet')
    offer_title43img = fields.Binary('Image Acteurs du projet')
    offer_title44 = fields.Html('Gestion du turnover')
    offer_title451 = fields.Html('Prérequis')
    offer_title452 = fields.Html('Spécification et standards client')
    offer_title453 = fields.Html('Coordination')
    offer_title454 = fields.Html('Remarques générales')
    offer_title46 = fields.Html('Formations')
    offer_title47 = fields.Html('Formation utilisateur')
    offer_title51 = fields.Html('Disponibilité et Support RealDev')
    offer_title52 = fields.Html('Garantie de continuité de projet')
    offer_title53 = fields.Html('Confidentialité')
    offer_title54 = fields.Html('Ne sont pas compris dans nos prix (Exclusions)')
    offer_title55 = fields.Html('Voyage')
    offer_title56 = fields.Html('Conditions de paiement')


class SaleOrder(models.Model):
    _inherit = "sale.order"

    offer_page2 = fields.Html('Offer Page2')
    offer_title2 = fields.Html('Objet de l’offre')
    offer_title21 = fields.Html('Historique des Versions')
    offer_title22 = fields.Html('Documents de Référence')
    offer_title31 = fields.Html('Data Integrity')
    offer_title32 = fields.Html('Cybersecruity ')
    offer_title33 = fields.Html('3.3Stratégie de Validation')
    offer_title34 = fields.Html('Scope du projet')
    offer_title35 = fields.Html('Liste des délivrables')
    offer_title41 = fields.Html('Planning')
    offer_title42 = fields.Html('Pilote de projet')
    offer_title43 = fields.Html('Acteurs du projet')
    offer_title43img = fields.Binary('Image Acteurs du projet')
    offer_title44 = fields.Html('Gestion du turnover')
    offer_title451 = fields.Html('Prérequis')
    offer_title452 = fields.Html('Spécification et standards client')
    offer_title453 = fields.Html('Coordination')
    offer_title454 = fields.Html('Remarques générales')
    offer_title46 = fields.Html('Formations')
    offer_title47 = fields.Html('Formation utilisateur')
    offer_title51 = fields.Html('Disponibilité et Support RealDev')
    offer_title52 = fields.Html('Garantie de continuité de projet')
    offer_title53 = fields.Html('Confidentialité')
    offer_title54 = fields.Html('Ne sont pas compris dans nos prix (Exclusions)')
    offer_title55 = fields.Html('Voyage')
    offer_title56 = fields.Html('Conditions de paiement')

    @api.onchange('sale_order_template_id')
    def onchange_sale_order_template_id_tis(self):
        if self.sale_order_template_id:
            self.offer_page2 = self.sale_order_template_id.offer_page2
            self.offer_title2 = self.sale_order_template_id.offer_title2
            self.offer_title56 =  self.sale_order_template_id.offer_title56
            self.offer_title55 =  self.sale_order_template_id.offer_title55
            self.offer_title54 =  self.sale_order_template_id.offer_title54
            self.offer_title53 =  self.sale_order_template_id.offer_title53
            self.offer_title52 =  self.sale_order_template_id.offer_title52
            self.offer_title51 =  self.sale_order_template_id.offer_title51
            self.offer_title47 =  self.sale_order_template_id.offer_title47
            self.offer_title46 =  self.sale_order_template_id.offer_title46
            self.offer_title454 =  self.sale_order_template_id.offer_title454
            self.offer_title453 =  self.sale_order_template_id.offer_title453
            self.offer_title452 =  self.sale_order_template_id.offer_title452
            self.offer_title451 =  self.sale_order_template_id.offer_title451
            self.offer_title44 =  self.sale_order_template_id.offer_title44
            self.offer_title43img =  self.sale_order_template_id.offer_title43img
            self.offer_title43 =  self.sale_order_template_id.offer_title43
            self.offer_title42 =  self.sale_order_template_id.offer_title42
            self.offer_title41 =  self.sale_order_template_id.offer_title41
            self.offer_title35 =  self.sale_order_template_id.offer_title35
            self.offer_title34 =  self.sale_order_template_id.offer_title34
            self.offer_title33 =  self.sale_order_template_id.offer_title33
            self.offer_title32 =  self.sale_order_template_id.offer_title32
            self.offer_title31 =  self.sale_order_template_id.offer_title31
            self.offer_title22 =  self.sale_order_template_id.offer_title22
            self.offer_title21 =  self.sale_order_template_id.offer_title21

