{
    'name': 'food delivery',
    'depends' : [
        'base',
        'base_setup',
        'sale',
        'hr',
    ],
    'application': True,
    'data':[
        'security/ir.model.access.csv',
        'data/food_order_view.xml',
        'data/food_item_views.xml',
        'data/employee_view.xml',
        'data/department_view.xml',
        'data/customers_view.xml',
        'data/food_item_category_view.xml',
        'data/order_status_view.xml',
        'data/job_view.xml',
        'views/restaurant_menus.xml',
        'views/employee.xml',
        'views/department.xml',
        # 'views/job.xml',
     ]
}