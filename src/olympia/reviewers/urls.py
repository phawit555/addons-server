from django.conf.urls import url

from olympia.addons.urls import ADDON_ID
from olympia.reviewers import views, views_themes


# All URLs under /editors/
urlpatterns = (
    url(r'^$', views.home, name='reviewers.home'),
    url(r'^queue$', views.queue, name='reviewers.queue'),
    url(r'^queue/new$', views.queue_nominated,
        name='reviewers.queue_nominated'),
    url(r'^queue/updates$', views.queue_pending,
        name='reviewers.queue_pending'),
    url(r'^queue/reviews$', views.queue_moderated,
        name='reviewers.queue_moderated'),
    url(r'^queue/application_versions\.json$', views.application_versions_json,
        name='reviewers.application_versions_json'),
    url(r'^queue/auto_approved', views.queue_auto_approved,
        name='reviewers.queue_auto_approved'),
    url(r'^queue/content_review', views.queue_content_review,
        name='reviewers.queue_content_review'),
    url(r'^unlisted_queue$', views.unlisted_queue,
        name='reviewers.unlisted_queue'),
    url(r'^unlisted_queue/all$', views.unlisted_list,
        name='reviewers.unlisted_queue_all'),
    url(r'^logs$', views.eventlog, name='reviewers.eventlog'),
    url(r'^log/(\d+)$', views.eventlog_detail,
        name='reviewers.eventlog.detail'),
    url(r'^reviewlog$', views.reviewlog, name='reviewers.reviewlog'),
    url(r'^beta_signed_log$', views.beta_signed_log,
        name='reviewers.beta_signed_log'),
    url(r'^queue_version_notes/%s?$' % ADDON_ID, views.queue_version_notes,
        name='reviewers.queue_version_notes'),
    url(r'^queue_review_text/(\d+)?$', views.queue_review_text,
        name='reviewers.queue_review_text'),  # (?P<addon_id>[^/<>"']+)
    url(r'^queue_viewing$', views.queue_viewing,
        name='reviewers.queue_viewing'),
    url(r'^review_viewing$', views.review_viewing,
        name='reviewers.review_viewing'),
    # 'content' is not a channel, but is a special kind of review that we only
    # do for listed add-ons, so we abuse the channel parameter to handle that.
    url(r'^review(?:-(?P<channel>listed|unlisted|content))?/%s$' % ADDON_ID,
        views.review, name='reviewers.review'),
    url(r'^whiteboard/(?P<channel>listed|unlisted|content)/%s$' % ADDON_ID,
        views.whiteboard, name='reviewers.whiteboard'),
    url(r'^performance/(?P<user_id>\d+)?$', views.performance,
        name='reviewers.performance'),
    url(r'^motd$', views.motd, name='reviewers.motd'),
    url(r'^motd/save$', views.save_motd, name='reviewers.save_motd'),
    url(r'^abuse-reports/%s$' % ADDON_ID, views.abuse_reports,
        name='reviewers.abuse_reports'),
    url(r'^leaderboard/$', views.leaderboard, name='reviewers.leaderboard'),

    url('^themes$', views_themes.home,
        name='reviewers.themes.home'),
    url('^themes/pending$', views_themes.themes_list,
        name='reviewers.themes.list'),
    url('^themes/flagged$', views_themes.themes_list,
        name='reviewers.themes.list_flagged',
        kwargs={'flagged': True}),
    url('^themes/updates$', views_themes.themes_list,
        name='reviewers.themes.list_rereview',
        kwargs={'rereview': True}),
    url('^themes/queue/$', views_themes.themes_queue,
        name='reviewers.themes.queue_themes'),
    url('^themes/queue/flagged$', views_themes.themes_queue_flagged,
        name='reviewers.themes.queue_flagged'),
    url('^themes/queue/updates$', views_themes.themes_queue_rereview,
        name='reviewers.themes.queue_rereview'),
    url('^themes/queue/commit$', views_themes.themes_commit,
        name='reviewers.themes.commit'),
    url('^themes/queue/single/(?P<slug>[^ /]+)$', views_themes.themes_single,
        name='reviewers.themes.single'),
    url('^themes/history/(?P<username>[^ /]+)?$',
        views_themes.themes_history, name='reviewers.themes.history'),
    url(r'^themes/logs$', views_themes.themes_logs,
        name='reviewers.themes.logs'),
    url('^themes/release$', views_themes.release_locks,
        name='reviewers.themes.release_locks'),
    url('^themes/logs/deleted/$', views_themes.deleted_themes,
        name='reviewers.themes.deleted'),
    url('^themes/search/$', views_themes.themes_search,
        name='reviewers.themes.search'),
)