import mock

from django.test import TestCase
from readthedocs.projects.models import Project
from readthedocs.builds.constants import LATEST
from readthedocs.core.templatetags import core_tags


class CoreTagsTests(TestCase):
    fixtures = ["eric", "test_data"]

    def setUp(self):
        with mock.patch('readthedocs.projects.models.update_static_metadata'):
            self.client.login(username='eric', password='test')
            self.pip = Project.objects.get(slug='pip')
            self.pip_fr = Project.objects.create(name="PIP-FR", slug='pip-fr', language='fr', main_language_project=self.pip)

    def test_project_only(self):
        proj = Project.objects.get(slug='pip')
        url = core_tags.make_document_url(proj)
        self.assertEqual(url, '/docs/pip/en/latest/')
        url = core_tags.make_document_url(proj, '')
        self.assertEqual(url, '/docs/pip/en/latest/')

    def test_project_only_htmldir(self):
        proj = Project.objects.get(slug='pip')
        proj.documentation_type = 'sphinx_htmldir'
        url = core_tags.make_document_url(proj)
        self.assertEqual(url, '/docs/pip/en/latest/')
        url = core_tags.make_document_url(proj, '')
        self.assertEqual(url, '/docs/pip/en/latest/')

    def test_project_only_singlehtml(self):
        proj = Project.objects.get(slug='pip')
        proj.documentation_type = 'sphinx_singlehtml'
        url = core_tags.make_document_url(proj)
        self.assertEqual(url, '/docs/pip/en/latest/')
        url = core_tags.make_document_url(proj, '')
        self.assertEqual(url, '/docs/pip/en/latest/')

    def test_translation_project_only(self):
        proj = Project.objects.get(slug='pip-fr')
        url = core_tags.make_document_url(proj)
        self.assertEqual(url, '/docs/pip/fr/latest/')
        url = core_tags.make_document_url(proj, '')
        self.assertEqual(url, '/docs/pip/fr/latest/')

    def test_translation_project_only_htmldir(self):
        proj = Project.objects.get(slug='pip-fr')
        proj.documentation_type = 'sphinx_htmldir'
        url = core_tags.make_document_url(proj)
        self.assertEqual(url, '/docs/pip/fr/latest/')
        url = core_tags.make_document_url(proj, '')
        self.assertEqual(url, '/docs/pip/fr/latest/')

    def test_translation_project_only_singlehtml(self):
        proj = Project.objects.get(slug='pip-fr')
        proj.documentation_type = 'sphinx_singlehtml'
        url = core_tags.make_document_url(proj)
        self.assertEqual(url, '/docs/pip/fr/latest/')
        url = core_tags.make_document_url(proj, '')
        self.assertEqual(url, '/docs/pip/fr/latest/')

    def test_project_and_version(self):
        proj = Project.objects.get(slug='pip')
        url = core_tags.make_document_url(proj, 'abc')
        self.assertEqual(url, '/docs/pip/en/abc/')
        url = core_tags.make_document_url(proj, 'abc', '')
        self.assertEqual(url, '/docs/pip/en/abc/')

    def test_project_and_version_htmldir(self):
        proj = Project.objects.get(slug='pip')
        proj.documentation_type = 'sphinx_htmldir'
        url = core_tags.make_document_url(proj, 'abc')
        self.assertEqual(url, '/docs/pip/en/abc/')
        url = core_tags.make_document_url(proj, 'abc', '')
        self.assertEqual(url, '/docs/pip/en/abc/')

    def test_project_and_version_singlehtml(self):
        proj = Project.objects.get(slug='pip')
        proj.documentation_type = 'sphinx_singlehtml'
        url = core_tags.make_document_url(proj, 'abc')
        self.assertEqual(url, '/docs/pip/en/abc/')
        url = core_tags.make_document_url(proj, 'abc', '')
        self.assertEqual(url, '/docs/pip/en/abc/')

    def test_translation_project_and_version(self):
        proj = Project.objects.get(slug='pip-fr')
        url = core_tags.make_document_url(proj, 'abc')
        self.assertEqual(url, '/docs/pip/fr/abc/')
        url = core_tags.make_document_url(proj, 'abc', '')
        self.assertEqual(url, '/docs/pip/fr/abc/')

    def test_translation_project_and_version_htmldir(self):
        proj = Project.objects.get(slug='pip-fr')
        proj.documentation_type = 'sphinx_htmldir'
        url = core_tags.make_document_url(proj, 'abc')
        self.assertEqual(url, '/docs/pip/fr/abc/')
        url = core_tags.make_document_url(proj, 'abc', '')
        self.assertEqual(url, '/docs/pip/fr/abc/')

    def test_translation_project_and_version_singlehtml(self):
        proj = Project.objects.get(slug='pip-fr')
        proj.documentation_type = 'sphinx_singlehtml'
        url = core_tags.make_document_url(proj, 'abc')
        self.assertEqual(url, '/docs/pip/fr/abc/')
        url = core_tags.make_document_url(proj, 'abc', '')
        self.assertEqual(url, '/docs/pip/fr/abc/')

    def test_project_and_version_and_page(self):
        proj = Project.objects.get(slug='pip')
        url = core_tags.make_document_url(proj, 'abc', 'xyz')
        self.assertEqual(url, '/docs/pip/en/abc/xyz.html')
        url = core_tags.make_document_url(proj, 'abc', 'index')
        self.assertEqual(url, '/docs/pip/en/abc/')

    def test_project_and_version_and_page_htmldir(self):
        proj = Project.objects.get(slug='pip')
        proj.documentation_type = 'sphinx_htmldir'
        url = core_tags.make_document_url(proj, 'abc', 'xyz')
        self.assertEqual(url, '/docs/pip/en/abc/xyz/')
        url = core_tags.make_document_url(proj, 'abc', 'index')
        self.assertEqual(url, '/docs/pip/en/abc/')

    def test_project_and_version_and_page_signlehtml(self):
        proj = Project.objects.get(slug='pip')
        proj.documentation_type = 'sphinx_singlehtml'
        url = core_tags.make_document_url(proj, 'abc', 'xyz')
        self.assertEqual(url, '/docs/pip/en/abc/index.html#document-xyz')
        url = core_tags.make_document_url(proj, 'abc', 'index')
        self.assertEqual(url, '/docs/pip/en/abc/')

    def test_translation_project_and_version_and_page(self):
        proj = Project.objects.get(slug='pip-fr')
        url = core_tags.make_document_url(proj, 'abc', 'xyz')
        self.assertEqual(url, '/docs/pip/fr/abc/xyz.html')
        url = core_tags.make_document_url(proj, 'abc', 'index')
        self.assertEqual(url, '/docs/pip/fr/abc/')

    def test_translation_project_and_version_and_page_htmldir(self):
        proj = Project.objects.get(slug='pip-fr')
        proj.documentation_type = 'sphinx_htmldir'
        url = core_tags.make_document_url(proj, 'abc', 'xyz')
        self.assertEqual(url, '/docs/pip/fr/abc/xyz/')
        url = core_tags.make_document_url(proj, 'abc', 'index')
        self.assertEqual(url, '/docs/pip/fr/abc/')

    def test_translation_project_and_version_and_page_singlehtml(self):
        proj = Project.objects.get(slug='pip-fr')
        proj.documentation_type = 'sphinx_singlehtml'
        url = core_tags.make_document_url(proj, 'abc', 'xyz')
        self.assertEqual(url, '/docs/pip/fr/abc/index.html#document-xyz')
        url = core_tags.make_document_url(proj, 'abc', 'index')
        self.assertEqual(url, '/docs/pip/fr/abc/')

    def test_mkdocs(self):
        proj = Project.objects.get(slug='pip')
        proj.documentation_type = 'mkdocs'
        url = core_tags.make_document_url(proj, LATEST, 'document')
        self.assertEqual(url, '/docs/pip/en/latest/document/')

    def test_mkdocs_no_directory_urls(self):
        proj = Project.objects.get(slug='pip')
        proj.documentation_type = 'mkdocs'
        url = core_tags.make_document_url(proj, LATEST, 'document.html')
        self.assertEqual(url, '/docs/pip/en/latest/document.html')

    def test_mkdocs_index(self):
        proj = Project.objects.get(slug='pip')
        proj.documentation_type = 'mkdocs'
        url = core_tags.make_document_url(proj, LATEST, 'index')
        self.assertEqual(url, '/docs/pip/en/latest/')

    def test_mkdocs_index_no_directory_urls(self):
        proj = Project.objects.get(slug='pip')
        proj.documentation_type = 'mkdocs'
        url = core_tags.make_document_url(proj, LATEST, 'index.html')
        self.assertEqual(url, '/docs/pip/en/latest/')
