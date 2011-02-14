""" Gulu comments module admin definitions """

# This code was taken from the built-in comments app, django.contrib.comments

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: admin.py 388 2010-12-16 06:59:01Z ben $"

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _, ungettext
from django.contrib.comments import get_model
from django.contrib.comments.views.moderation import perform_flag, perform_approve, perform_delete

from gcomments.models import GComment

class GCommentsAdmin(admin.ModelAdmin):
	fieldsets = (
		(None,
			{'fields': ('content_type', 'object_pk', 'site')}
		),
		(_('Content'),
			{'fields': ('commenter', 'user_name', 'user_email', 'user_url', 'comment')}
		),
		(_('Metadata'),
			{'fields': ('submit_date', 'ip_address', 'is_public', 'is_removed')}
		),
	 )

	list_display = ('name', 'content_type', 'object_pk', 'ip_address', 'submit_date', 'is_public', 'is_removed')
	list_filter = ('submit_date', 'site', 'is_public', 'is_removed')
	date_hierarchy = 'submit_date'
	ordering = ('-submit_date',)
	raw_id_fields = ('commenter',)
	search_fields = ('comment', 'commenter__username', 'user_name', 'user_email', 'user_url', 'ip_address')
	actions = ["flag_comments", "approve_comments", "remove_comments"]

	def get_actions(self, request):
		actions = super(GCommentsAdmin, self).get_actions(request)
		# Only superusers should be able to delete the comments from the DB.
		if not request.user.is_superuser:
			actions.pop('delete_selected')
		if not request.user.has_perm('comments.can_moderate'):
			actions.pop('approve_comments')
			actions.pop('remove_comments')
		return actions

	def flag_comments(self, request, queryset):
		self._bulk_flag(request, queryset, perform_flag,
						lambda n: ungettext('flagged', 'flagged', n))
	flag_comments.short_description = _("Flag selected comments")

	def approve_comments(self, request, queryset):
		self._bulk_flag(request, queryset, perform_approve,
						lambda n: ungettext('approved', 'approved', n))
	approve_comments.short_description = _("Approve selected comments")

	def remove_comments(self, request, queryset):
		self._bulk_flag(request, queryset, perform_delete,
						lambda n: ungettext('removed', 'removed', n))
	remove_comments.short_description = _("Remove selected comments")

	def _bulk_flag(self, request, queryset, action, done_message):
		"""
		Flag, approve, or remove some comments from an admin action. Actually
		calls the `action` argument to perform the heavy lifting.
		"""
		n_comments = 0
		for comment in queryset:
			action(request, comment)
			n_comments += 1

		msg = ungettext(u'1 comment was successfully %(action)s.',
						u'%(count)s comments were successfully %(action)s.',
						n_comments)
		self.message_user(request, msg % {'count': n_comments, 'action': done_message(n_comments)})

admin.site.register(GComment, GCommentsAdmin)
