# Generated by Django 2.0.3 on 2018-03-28 19:32

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0016_auto_20160901_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionpage',
            name='body',
            field=wagtail.core.fields.StreamField((('section', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.TextBlock(help_text='Write a title for this section.')), ('subheadline', wagtail.core.blocks.TextBlock(help_text='Write a subheadline for this section (optional).', required=False)), ('body', wagtail.core.blocks.StreamBlock((('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/heading.html')), ('smaller_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smaller_heading.html')), ('smallest_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smallest_heading.html')), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))))), ('download', wagtail.documents.blocks.DocumentChooserBlock(icon='fa-download', template='blocks/download.html')), ('accordion', wagtail.core.blocks.StructBlock((('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))), label='Panel'))),))), ('notice', wagtail.core.blocks.StructBlock((('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], help_text='Choose what type of notice this is.', required=False))))), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('button', wagtail.core.blocks.StructBlock((('button_target', wagtail.core.blocks.PageChooserBlock(help_text='Choose where this button should link to.', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='What should the button say?', required=False)))))), help_text='The section content goes here.'))))),)),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/heading.html')), ('smaller_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smaller_heading.html')), ('smallest_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smallest_heading.html')), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))))), ('download', wagtail.documents.blocks.DocumentChooserBlock(icon='fa-download', template='blocks/download.html')), ('accordion', wagtail.core.blocks.StructBlock((('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))), label='Panel'))),))), ('notice', wagtail.core.blocks.StructBlock((('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], help_text='Choose what type of notice this is.', required=False))))), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('button', wagtail.core.blocks.StructBlock((('button_target', wagtail.core.blocks.PageChooserBlock(help_text='Choose where this button should link to.', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='What should the button say?', required=False))))))),
        ),
    ]
