from celery.task import task
from django.core.mail import EmailMessage
from django.shortcuts import reverse
from django.template.loader import render_to_string

from common.models import Comment, User


@task
def send_email_user_mentions(comment_id, called_from, domain='demo.django-crm.io', protocol='http'):
    """ Send Mail To Mentioned Users In The Comment """
    comment = Comment.objects.filter(id=comment_id).first()
    if comment:
        comment_text = comment.comment
        comment_text_list = comment_text.split()
        recipients = []
        for comment_text in comment_text_list:
            if comment_text.startswith('@'):
                if comment_text.strip('@').strip(',') not in recipients:
                    if User.objects.filter(username=comment_text.strip('@').strip(',')).exists():
                        email = User.objects.filter(
                            username=comment_text.strip('@').strip(',')).first().email
                        recipients.append(email)

        context = {}
        context["name"] = comment.commented_by
        context["comment_description"] = comment.comment
        if called_from == 'accounts':
            context["url"] = protocol + '://' + domain + \
                reverse('accounts:view_account', args=(comment.account.id,))
        elif called_from == 'contacts':
            context["url"] = protocol + '://' + domain + \
                reverse('contacts:view_contact', args=(comment.contact.id,))
        elif called_from == 'leads':
            context["url"] = protocol + '://' + domain + \
                reverse('leads:view_lead', args=(comment.lead.id,))
        elif called_from == 'opportunity':
            context["url"] = protocol + '://' + domain + \
                reverse('opportunity:opp_view', args=(comment.opportunity.id,))
        elif called_from == 'cases':
            context["url"] = protocol + '://' + domain + \
                reverse('cases:view_case', args=(comment.case.id,))
        elif called_from == 'tasks':
            context["url"] = protocol + '://' + domain + \
                reverse('tasks:task_detail', args=(comment.task.id,))
        else:
            context["url"] = ''
        html_content = render_to_string('comment_email.html', context=context)
        subject = 'Django CRM : comment '
        if recipients:
            msg = EmailMessage(
                subject,
                html_content,
                from_email=comment.commented_by.email,
                to=recipients
            )
            msg.content_subtype = "html"
            msg.send()
