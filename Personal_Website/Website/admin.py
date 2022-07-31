from django.contrib import admin
from .models import Website_content, Website_steps, content2, steps2, Contact

# # Register your models here.


# # Contact form
# class Contact_form1(admin.TabularInline):
#     model = Contact
#
# class ContactAdmin(admin.ModelAdmin):
#     inlines = [
#         Contact_form1,
#     ]

# Start project 1
class StepInline(admin.TabularInline):
    model = Website_steps.website_cont.through


class Website_contentAdmin(admin.ModelAdmin):
    inlines = [
        StepInline,
    ]

class Website_stepsAdmin(admin.ModelAdmin):
    inlines = [
        StepInline,
    ]
    exclude = ('website_cont',)

# End project1

# Start project2
class StepInline2(admin.TabularInline):
    model = steps2.website_cont2.through


class Website_contentAdmin2(admin.ModelAdmin):
    inlines = [
        StepInline2,
    ]

class Website_stepsAdmin2(admin.ModelAdmin):
    inlines = [
        StepInline2,
    ]
    exclude = ('website_cont2',)
#End project 2

# admin.site.register(Contact, ContactAdmin)

admin.site.register(Website_content, Website_contentAdmin)
admin.site.register(Website_steps, Website_stepsAdmin,)

admin.site.register(content2, Website_contentAdmin2)
admin.site.register(steps2, Website_stepsAdmin2,)
