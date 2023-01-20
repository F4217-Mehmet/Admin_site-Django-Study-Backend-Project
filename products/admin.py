from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    list_editable = ( "is_in_stock", )
    # list_display_links = ("create_date", ) # default olarak listin ilki link gelir. hem link hem editable olmaz
    list_filter = ("is_in_stock", "create_date")
    ordering = ("name",) 
    search_fields = ("name",)
    prepopulated_fields = {'slug' : ('name',)} #nameden slug üretiyor
    list_per_page = 25
    date_hierarchy = "update_date"
    # fields = (('name', 'slug'), 'description', "is_in_stock") #fieldset kullandığımız zaman bunu kullanamayız
    fieldsets = (
        (None, {
            "fields": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description",),
            'description' : "You can use this section for optionals settings"
        })
    )
    actions = ("is_in_stock", )

    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} kinds of product added to stocks")
    is_in_stock.short_description = 'Add selected products to stock' # bu şekilde tanımlama yaptık, adminde daha mantıklı görünmesi için

    

admin.site.register(Product, ProductAdmin)

admin.site.site_title = "Coredinat Title"
admin.site.site_header = "Coredinat Admin Portal"  
admin.site.index_title = "Welcome to Coredinat Admin Portal"