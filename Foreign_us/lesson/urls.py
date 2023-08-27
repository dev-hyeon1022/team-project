from django.urls import path
from django.views.generic import TemplateView

from lesson.views import LessonListView, LessonDetailView, LessonWriteView, LessonReviewDetailView, \
    LessonReviewWriteView, LessonListAPI
from member.views import MemberLoginView
from profilepage.views import ProfileView, HostView

app_name = 'lesson'

urlpatterns = [
    path('list/', LessonListView.as_view(), name='list-init'),
    path('list/<int:page>/<str:type>', LessonListAPI.as_view(), name='list'),
    path('detail/', LessonDetailView.as_view(), name='detail'),
    path('write/', LessonWriteView.as_view(), name='write-init'),
    path('write/<int:post_id>', LessonWriteView.as_view(), name='write'),
    path('review/detail/', LessonReviewDetailView.as_view(), name='review-detail'),
    path('review/write/', LessonReviewWriteView.as_view(), name='review-write'),





# # 공지사항
#     path('list/', NoticeListView.as_view(), name='list-init'),
#     path('list/<int:page>', NoticeListAPI.as_view(), name='list'),
#     path('detail/<int:post_id>', NoticeDetailView.as_view(), name='detail'),
#     # 공지사항 댓글
#     path('replies/list/<int:post_id>', NoticeReplyListAPI.as_view(), name='list-init'),
#     path('replies/list/<int:post_id>/<int:page>', NoticeReplyListAPI.as_view(), name='list'),
#     path('replies/write/', NoticeReplyWriteAPI.as_view(), name='write'),
#     path('replies/modify/', NoticeReplyModifyAPI.as_view(), name='modify'),
#     path('replies/delete/<int:id>/', NoticeReplyDeleteAPI.as_view(), name='delete_get'),
#     # 공지사항 좋아요
#     path('likes/add/', NoticeLikeAddAPI.as_view(), name='add'),
#     path('likes/delete/', NoticeLikeDeleteAPI.as_view(), name='delete'),
#     path('likes/count/<int:id>/', NoticeLikeCountAPI.as_view(), name='count'),
#     path('likes/exist/<int:id>/', NoticeLikeExistAPI.as_view(), name='exist'),
]
