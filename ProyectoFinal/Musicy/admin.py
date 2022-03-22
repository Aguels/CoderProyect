from django.contrib import admin
import Musicy.models as md

admin.site.register(md.Musician)
admin.site.register(md.BlogEntry)
admin.site.register(md.Song)