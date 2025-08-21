from django.contrib import admin

from uploads.models import Upload


class UploadAdmin(admin.ModelAdmin):
    list_display = ["slug", "file", "created_at", "updated_at"]
    search_fields = ["slug", "file"]

    readonly_fields = ["created_at", "updated_at"]
    fieldsets = [
        (None, {"fields": ["slug", "file"]}),
        (
            "Administrative",
            {
                "fields": ["created_at", "updated_at"],
            },
        ),
    ]


admin.site.register(Upload, UploadAdmin)
