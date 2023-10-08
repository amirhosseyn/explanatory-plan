from django.db import models

class Plan(models.Model):

    # Fixed Costs
    land = models.FloatField(verbose_name='زمین', default=0)
    landscaping = models.FloatField(verbose_name='محوطه سازی', default=0)
    construction = models.FloatField(verbose_name='ساختمان سازی', default=0)
    machinery = models.FloatField(verbose_name='ماشین آلات', default=0)
    facilities = models.FloatField(verbose_name='تاسیسات', default=0)
    transportation = models.FloatField(verbose_name='وسایل حمل و نقل', default=0)
    office_equipment = models.FloatField(verbose_name='وسایل اداری', default=0)

    @property
    def unforeseen_items(self):
        return 0.1 * (self.land + self.landscaping + self.construction + self.machinery + self.facilities + self.transportation + self.office_equipment)

    @property
    def total(self):
        return self.land + self.landscaping + self.construction + self.machinery + self.facilities + self.transportation + self.office_equipment + self.unforeseen_items

    # Variable costs

    raw_materials_packaging = models.FloatField(verbose_name='هزینه مواد اولیه و بسته بندی', default=0)
    salaries_wages = models.FloatField(verbose_name='هزینه حقوق و دستمزد', default=0)
    energy_consumption = models.FloatField(verbose_name='هزینه انرژی مصرفی', default=0)
    maintenance_repairs = models.FloatField(verbose_name='هزینه تعمیر و نگهداری', default=0)

    @property
    def unforeseen_expenses(self):
        # Your arithmetic function for unforeseen expenses goes here
        pass

    @property
    def administrative_sales(self):
        # Your arithmetic function for administrative and sales expenses goes here
        pass

    @property
    def factory_insurance(self):
        # Your arithmetic function for factory insurance expenses goes here
        pass

    @property
    def depreciation(self):
        # Your arithmetic function for depreciation expenses goes here
        pass

    @property
    def total_variable_costs(self):
        # Your arithmetic function for total variable costs goes here
        pass
    
    # Sale
    annual_production = models.FloatField(verbose_name='میزان تولید سالانه', default=0)
    unit_price = models.FloatField(verbose_name='قیمت فروش یک واحد محصول', default=0)

    # Validation
    @property
    def total_investment(self):
        # Your arithmetic function for total investment goes here
        pass

    @property
    def total_cost_per_product(self):
        # Your arithmetic function for total cost per product goes here
        pass

    @property
    def selling_price_per_product(self):
        # Your arithmetic function for selling price per product goes here
        pass

    @property
    def annual_sales(self):
        # Your arithmetic function for annual sales goes here
        pass

    @property
    def payback_period(self):
        # Your arithmetic function for payback period goes here
        pass

    @property
    def return_rate(self):
        # Your arithmetic function for return rate goes here
        pass

    fieldsets = [
        ('هزینه‌های ثابت', {'fields': ('land', 'landscaping', 'construction', 'machinery', 'facilities', 'transportation', 'office_equipment')}),
        ('هزینه‌های متغیر', {'fields': ('raw_materials_packaging', 'salaries_wages', 'energy_consumption', 'maintenance_repairs')}),
        ('فروش', {'fields': ('annual_production', 'unit_price')}),
        ('اعتبارسنجی', {'fields': ('total_investment', 'total_cost_per_product', 'selling_price_per_product', 'annual_sales', 'payback_period', 'return_rate')}),
    ]